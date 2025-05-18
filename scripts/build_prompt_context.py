import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

TIMESTAMP = datetime.utcnow().strftime('%Y%m%d')
OUTPUT_FILE = "prompt_context.md"

def fetch_recent_commits(repo, days=7):
    since = (datetime.utcnow() - timedelta(days=days)).isoformat() + "Z"
    url = f"https://api.github.com/repos/ethereum/{repo}/commits"
    params = {"since": since}
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    commits = response.json()
    return [
        f"- [{c['commit']['message'].splitlines()[0]}]({c['html_url']})"
        for c in commits
    ] or ["No commits in past 7 days."]

def get_client_diversity():
    url = "https://clientdiversity.org"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    stats = []
    if table:
        for row in table.find_all("tr"):
            cols = [td.get_text(strip=True) for td in row.find_all("td")]
            if cols:
                stats.append(" | ".join(cols))
    return stats or ["Client diversity data unavailable."]

def main():
    eip_data = fetch_recent_commits("EIPs")
    erc_data = fetch_recent_commits("ERCs")
    diversity_stats = get_client_diversity()

    with open(OUTPUT_FILE, "w") as f:
        f.write(f"### EIP GitHub Updates (last 7 days)\n")
        f.write("\n".join(eip_data) + "\n\n")
        f.write(f"### ERC GitHub Updates (last 7 days)\n")
        f.write("\n".join(erc_data) + "\n\n")
        f.write(f"### Client Diversity Stats (live)\n")
        for stat in diversity_stats:
            f.write(f"- {stat}\n")

if __name__ == "__main__":
    main()
