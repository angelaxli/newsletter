**10. Centralization watch: threatening the value of your ETH**

  * **Content:** Provide updates and analysis related to Ethereum centralization risks. Each item should be a bullet point.
  * **Focus:**
      * **Lido&#39;s Staking Share:** Find the &#39;Lido Share&#39; percentage from the context data you loaded. **You MUST format this into a single, specific sentence like this:** &quot;🚨 [Lido at XX.X%](https://dune.com/hildobby/eth2-staking), still too close to the [33.3% threshold](https://notes.ethereum.org/@djrtwo/risks-of-lsd).&quot;
      * **Client Diversity Summary:** Following the Lido line, you MUST create a main bullet point formatted exactly like this: &quot;Client diversity (via clientdiversity.org):&quot;
        * Under this main bullet point, you MUST create three nested bullet points:
            * One for the execution layer, summarizing the top 1-2 clients (e.g., Execution layer: Geth ~XX% & Nethermind ~YY%).
            * One for the consensus layer, summarizing the top 1-2 clients (e.g., Consensus layer: Prysm XX%).
            * You MUST include this exact bullet point as plain text: &quot;Any client bug over 33.3% could mean loss of finality.&quot;
      * **After presenting the client diversity summary, you MUST include this exact bullet point:** &quot;* Better [geographic diversity](https://nodewatch.io/) is optimal, particularly outside of North America &amp; Europe.&quot;
  * **Sourcing Client Percentages:** For any specific client diversity percentages mentioned, YOU MUST use the data provided in the &#39;Manually Updated Client Diversity Data&#39; section which you have loaded from `scripts/prompt_context.md`. Attribute the source as specified in your context data. Do not attempt to scrape this data from the web yourself.

**12. EIPs/Standards**

  * **Content:** Summarize newly introduced Ethereum Improvement Proposals (EIPs) and application-level standards (ERCs), or those with significant status changes or active discussions in the past 7 days. Information **MUST be primarily sourced by monitoring activity (new PRs for Drafts, merged PRs for status changes) directly from the official `https://github.com/Ethereum/EIPs` repository.** Use `https://ethereum-magicians.org` for supplementary discussion context. Each item should be a bullet point.
  * **Focus:**
      * New EIPs/ERCs (identified by merged Draft PRs in `Ethereum/EIPs`).
      * EIPs/ERCs moving to "Review," "Last Call," "Final," or "Stagnant" (identified by merged PRs reflecting these status changes in `Ethereum/EIPs`).
      * Significant community discussions (link to `ethereum-magicians.org` or relevant GitHub Issues/PRs within the EIPs repo).
      * Breakdowns or explanations of important or complex EIPs/ERCs.
  * **Primary Sources for this Section:**
      * `https://github.com/Ethereum/EIPs` (for new proposals, status changes via merged PRs, and official EIP content).
      * `https://ethereum-magicians.org` (for community discussions and context around EIPs/ERCs).
  * **Keywords for Search (Starting Points):** "New EIP," "ERC [number] update," "Ethereum Improvement Proposal discussion," "Ethereum Magicians EIP."


**Output Format:**
The final output should be a well-formatted newsletter in Markdown, suitable for publication, with all original links and references preserved. All list items must use bullet points.
