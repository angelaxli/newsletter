import requests
from datetime import datetime, timedelta

def fetch_recent_commits(repo, days=7):
    since = (datetime.utcnow() - timedelta(days=days)).isoformat() + "Z"
    url = f"https://api.github.com/repos/ethereum/{repo}/commits"
    params = {'since': since}
    headers = {'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    commits = response.json()
    return [
        f"- [{commit['commit']['message'].splitlines()[0]}]({commit['html_url']})"
        for commit in commits
    ]

def main():
    days = 7
    output_file = "newsletter_" + datetime.utcnow().strftime('%Y%m%d') + ".md"
    with open(output_file, 'a') as f:
        f.write("\n\n## Recent EIP/ERC Activity\n")
        for repo in ['EIPs', 'ERCs']:
            f.write(f"\n### {repo} Updates (last {days} days)\n")
            try:
                commits = fetch_recent_commits(repo, days)
                if commits:
                    f.write("\n".join(commits) + "\n")
                else:
                    f.write("No updates found.\n")
            except Exception as e:
                f.write(f"Failed to fetch {repo} updates: {str(e)}\n")

if __name__ == "__main__":
    main()
