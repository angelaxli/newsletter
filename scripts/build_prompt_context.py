import requests
from datetime import datetime, timedelta
import os

# --- Configuration ---
OUTPUT_FILE = "scripts/prompt_context.md"
DAYS = 7
REQUEST_TIMEOUT = 15 # seconds
HTTP_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/vnd.github.v3+json'
}
# If you are hitting API rate limits, provide a GitHub token as an environment variable
# GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
# if GITHUB_TOKEN:
#     HTTP_HEADERS['Authorization'] = f'token {GITHUB_TOKEN}'

MANUAL_CLIENT_DIVERSITY_DATA = {
    "section_title": "Manually Updated Client Diversity Data",
    "source_checked": "clientdiversity.org (verified via execution-clients.com and Miga Labs)",
    "date_data_pulled": "2025-06-09",
    "data_as_of_date": "2025-06-09",
    "key_staking_entity_share": {
        "entity_name": "Lido",
        "share_percentage": "25.68%",
        "source_link": "https://dune.com/hildobby/eth2-staking"
    },
    "consensus_clients_note": "Sourced from Miga Labs via clientdiversity.org",
    "consensus_clients": [
        "Lighthouse: 42.71%", "Prysm: 30.91%", "Teku: 13.86%",
        "Nimbus: 8.74%", "Lodestar: 2.67%", "Grandine: 1.04%", "Other/Unknown: 0.07%"
    ],
    "execution_clients_note": "Sourced from execution-clients.com",
    "execution_clients": [
        "Geth: 41%", "Nethermind: 38%", "Besu: 16%",
        "Erigon: 3%", "Reth: 2%", "Other/Unknown: 0%"
    ],
}

def fetch_repo_updates(repo_name):
    """Fetches recently merged pull requests from a GitHub repository."""
    print(f"Fetching updates for {repo_name}...")
    since_date = (datetime.utcnow() - timedelta(days=DAYS)).isoformat()
    # Query for pull requests closed and updated in the last week to catch merges
    url = f"https://api.github.com/repos/{repo_name}/pulls"
    params = {'state': 'closed', 'sort': 'updated', 'direction': 'desc', 'per_page': 50}

    updates = []
    try:
        response = requests.get(url, headers=HTTP_HEADERS, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        prs = response.json()
        
        for pr in prs:
            # Check if 'merged_at' exists (is not None) and is within our date range
            if pr.get('merged_at') and pr['merged_at'] > since_date:
                updates.append(f"Merged PR #{pr['number']}: \"{pr['title']}\" - Link: {pr['html_url']}")
                
        if not updates:
            return [f"No recently merged PRs found for {repo_name}."]
            
    except requests.exceptions.RequestException as e:
        return [f"Error fetching updates for {repo_name}: {e}"]
    except Exception as e:
        return [f"An unexpected error occurred fetching updates for {repo_name}: {e}"]
    return updates

def main():
    """Main function to build the context file."""
    print("Starting context build...")
    
    # Fetch dynamic data
    eip_updates = fetch_repo_updates("ethereum/EIPs")
    erc_updates = fetch_repo_updates("ethereum/ERCs")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Raw Context Data for Ethereum Newsletter\n\n")
        f.write("This file contains raw data gathered for the weekly newsletter. The AI's job is to process, summarize, and format this information.\n\n")

        # --- Write Manual Data ---
        f.write(f"## {MANUAL_CLIENT_DIVERSITY_DATA['section_title']}\n\n")
        f.write(f"**Date Data Pulled:** {MANUAL_CLIENT_DIVERSITY_DATA['date_data_pulled']}\n")
        staking_data = MANUAL_CLIENT_DIVERSITY_DATA.get("key_staking_entity_share")
        if staking_data:
            f.write(f"**Lido Share:** {staking_data['share_percentage']}\n")
            f.write(f"**Lido Dune Link:** {staking_data['source_link']}\n")
        
        f.write("\n**Consensus Clients:**\n")
        for client in MANUAL_CLIENT_DIVERSITY_DATA['consensus_clients']:
            f.write(f"- {client}\n")
        
        f.write("\n**Execution Clients:**\n")
        for client in MANUAL_CLIENT_DIVERSITY_DATA['execution_clients']:
            f.write(f"- {client}\n")
        f.write("\n\n")

        # --- Write Fetched Data ---
        f.write("## Recent EIP Updates (from GitHub `ethereum/EIPs`)\n\n")
        for update in eip_updates:
            f.write(f"* {update}\n")
        f.write("\n")
        
        f.write("## Recent ERC Updates (from GitHub `ethereum/ERCs`)\n\n")
        for update in erc_updates:
            f.write(f"* {update}\n")
        f.write("\n")
    
    print(f"Context file generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
