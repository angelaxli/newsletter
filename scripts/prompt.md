**Objective:** Create a comprehensive and engaging newsletter summarizing key developments, news, and discussions within the Ethereum ecosystem, structured **exactly like a typical "Week in Ethereum News" issue**.

**CRITICAL OVERARCHING RULE: This newsletter MUST ONLY contain information, news, and updates that have occurred or were published within the strict 7-day period concluding on the date of execution (e.g., if executed on May 25, 2025, it covers Monday, May 19, 2025, to Sunday, May 25, 2025, inclusive). Furthermore, if any defined section or category below does not have any relevant updates from this 7-day period, that entire section or category MUST be omitted from the final newsletter. Do not include sections with no new information.**

The newsletter must cover **only the 7-day period concluding on the date of execution** (e.g., if executed on May 25, 2025, it covers Monday, May 19, 2025, to Sunday, May 25, 2025, inclusive). The AI must emphasize clarity, **absolute factual accuracy, verifiable timeliness (all information strictly from the past 7 days unless intrinsically referencing future events based on current announcements)**, relevance, and use its judgment to find and prioritize the most impactful information within this exact structure, ensuring all items are bullet-pointed under their respective headings. **This newsletter is for a high-stakes audience; errors or outdated information are unacceptable.**


**Newsletter Structure and Content Guidelines (Emulating "Week in Ethereum News"):**

**Highlight of the Week**
  * **Content:** Present the single most critical or impactful update from **within the specified 7-day period**. If multiple significant events occurred, select the one with the broadest impact or novelty.
  * **Focus:** Major network upgrade milestones achieved *this week*, breakthrough EIPs proposed/advanced *this week*, crucial official announcements made *this week*, or major security events that happened *this week*.
  * **Presentation:** A concise sentence or two, or a single bullet point with a link. Ensure this is a distinct highlight.

-----

## **Eth News and Links** *(Sections should only be included if relevant news from the past 7 days exists for them. Each item under these headings must be a bullet point.)*


**Eth R\&D Protocol Call(s) (e.g., All Core Devs Consensus/Execution, ACDC/ACDE)**
  * **Content:**
      * Identify any core developer calls (ACDE, ACDC, etc.) for which notes were published or significant discussions occurred within the past 7 days.
      * **Primarily source these summaries from posts by Andrew B Coathup (`@abcoathup`) on Ethereum Magicians (`https://ethereum-magicians.org/u/abcoathup/activity`).** Check this source for any new call notes posted within the 7-day window.
      * For each call that you report on, you MUST:
        1. Clearly state the name of the call and its verified date (e.g., "ACDC Call #123 - YYYY-MM-DD").
        2. Provide a direct link to the specific Ethereum Magicians post by @abcoathup (e.g., https://ethereum-magicians.org/t/acdc-call-123-date/xxxxx). If a Magicians summary from @abcoathup for a relevant call is unavailable, link to the official notes on ethereum/pm GitHub if they exist for that week.
        3. Present a concise summary of the call's key discussion points, decisions, and action items. This summary MUST be structured using bullet points (or nested sub-bullet points if appropriate) to detail the different topics and their outcomes as covered during the call. Emulate the detailed, bulleted style found in @abcoathup's summaries on Ethereum Magicians or typical "Week in Ethereum News" call reports. Each main topic or EIP discussed should ideally be its own bullet point with brief explanatory text.
      * **Crucially, verify the date of the call itself and any critical details (like EIPs discussed or major decisions) against official sources (e.g., meeting agendas/notes on `https://github.com/ethereum/pm`) even when using summaries from Ethereum Magicians. Do NOT report calls or summaries of calls that occurred outside the specified 7-day window. If no relevant calls were summarized by `@abcoathup` or had official notes published this week, state that clearly or omit this section.**
  * **Primary Sources for this Section:**
      * Call Summaries: Posts by `@abcoathup` on `https://ethereum-magicians.org/u/abcoathup/activity`.
      * Verification & Official Agendas/Notes: `https://github.com/ethereum/pm`.
  * **Keywords for Search (Contextual, focus on checking primary sources first):** "Ethereum AllCoreDevs summary," "ACDE notes," "ACDC notes," "Ethereum core dev call."


**Pectra (Prague + Electra) Upgrade (or current named mainnet upgrade)**
  * **Content:** Report specific progress, new EIPs considered/included (notably **EIP-7600: Pectra Upgrade Meta, see `https://eips.ethereum.org/EIPS/eip-7600`**), client readiness updates, testnet news, or important discussions related to the Pectra upgrade (or the current primary upcoming mainnet upgrade by its name) from the past 7 days. Focus should include updates on **devnets, specific testnet activities, dedicated Pectra testing calls,** and client compatibility related to Pectra from the past 7 days.
  * **Keywords for Search:** "Pectra upgrade news," "[current\_upgrade\_name] Ethereum," "Ethereum network upgrade," "Pectra testnet," "Pectra testing call," "EIP-7600."


**Fusaka (Osaka + Fulu) Upgrade (or next future named upgrade after Pectra)**
  * **Content:** Report any early discussions, research, or proposed EIPs related to the next major upgrade planned after Pectra (e.g., Fusaka, or its then-current name), if such news emerged in the past 7 days.
  * **Keywords for Search:** "Fusaka upgrade," "[next\_future\_upgrade\_name] Ethereum."


**Layer 1**
  * **Content:** Cover other significant L1 developments from the past 7 days not fitting under specific upgrade names. This could include research on Verkle Trees, State Expiry/History Management, SSZ, EOF, MEV strategy discussions, or new EIPs with L1 impact that aren't yet tied to a named upgrade.
  * **Keywords for Search:** "Ethereum Layer 1 updates," "Verkle Trees Ethereum," "Ethereum state expiry," "EVM Object Format EOF."


**Ethereum Foundation Blog/Announcements**
  * **Content:** Summarize and link to any official posts or significant announcements from the Ethereum Foundation or its core teams made in the past 7 days. Verify dates.
  * **Keywords for Search:** "Ethereum Foundation blog," "EF announcement."


**Research**
  * **Content:** Highlight significant research findings or discussions (e.g., from ethresear.ch) that directly impact protocol direction or understanding, if published or heavily discussed in the past 7 days, and not covered under specific upgrade or L1 sections.
  * **Keywords for Search:** "ethresear.ch [relevant topic]," "Ethereum research paper."


**Centralization watch: threatening the value of your ETH**
  * **Content:** Provide updates and analysis related to Ethereum centralization risks. Each item should be a bullet point.
  * **Must Include:**
    * **Lido&#39;s Staking Share:** Find the &#39;Lido Share&#39; percentage from the context data you loaded. **You MUST format this into a single, specific sentence like this:** &quot;🚨 [Lido at XX.X%](https://dune.com/hildobby/eth2-staking), still too close to the [33.3% threshold](https://notes.ethereum.org/@djrtwo/risks-of-lsd).&quot;
    * * **Client Diversity Summary:** Briefly state the approximate share of the top 1-2 execution and consensus clients using the data from the context.
    * **Mandatory Statement &amp; Formatting:**
      * **After presenting the client diversity summary, you MUST include this exact bullet point:** &quot;* Any client bug over 33.3% could mean loss of finality.&quot;
      * **Always include this exact bullet point:** &quot;* Better [geographic diversity](https://nodewatch.io/) is optimal, particularly outside of North America &amp; Europe.&quot;
  * **Sourcing Client Percentages:** For any specific client diversity percentages mentioned, YOU MUST use the data provided in the &#39;Manually Updated Client Diversity Data&#39; section which you have loaded from `scripts/prompt_context.md`. Attribute the source as specified in your context data. Do not attempt to scrape this data from the web yourself.
  * **Structure:** Present this as a few focused bullet points or short paragraphs, aiming for the style:
        ```
        🚨 [Lido at 28.4%](https://dune.com/hildobby/eth2-staking), still too close to the [33.3% threshold](https://notes.ethereum.org/@djrtwo/risks-of-lsd)
        * Client diversity (via clientdiversity.org):
            * Execution layer: Geth ~43% &amp; Nethermind ~36%
            * Consensus layer: Prysm 34%
            * Any client bug over 33.3% could mean loss of finality
        * Better [geographic diversity](https://nodewatch.io/) is optimal, particularly outside of North America &amp; Europe
        ```


**Client Releases**
  * **Content:** List new versions or significant updates for Ethereum client software released in the past 7 days. Each release should be a bullet point.
  * **Focus:**
      * **Consensus Layer Clients:** New releases for Lighthouse, Lodestar, Nimbus, Prysm, Teku. Note key features, performance improvements, or critical fixes.
      * **Execution Layer Clients:** New releases for Besu, Erigon, Geth, Nethermind. Note key features, performance improvements, or critical fixes.
  * **Keywords for Search (Starting Points):** "[Client Name] release," "Ethereum client updates," "GitHub [Client Name] releases."


**Layer 2**
  * **Content:** Significant developments from major Layer 2 scaling solutions and the broader L2 ecosystem from the past 7 days. Each item should be a bullet point.
  * **Focus:**
      * News from prominent L2s (e.g., Arbitrum, Optimism, zkSync, Starknet, Polygon solutions, Base, Linea).
      * Major announcements, network upgrades, new features, tokenomics changes, sequencer/prover updates, fraud proof systems.
      * New L2s launching or reaching significant milestones.
      * Bridge updates and security news specific to L2s.
      * Discussions on L2 interoperability, data availability solutions for L2s (e.g., EIP-4844 impact, Danksharding).
  * **Keywords for Search (Starting Points):** "[L2 Name] news," "Layer 2 Ethereum updates," "Optimistic rollup," "ZK rollup," "L2beat," "EIP-4844 blobs."


**EIPs/Standards**
  * **Content:** Ethereum Improvement Proposals (EIPs of all categories, including Core, Networking, Interface, and ERCs) and any with significant status changes or active discussions from the past 7 days. Information **MUST be primarily sourced by monitoring activity (new PRs for Drafts, merged PRs for status changes) directly from the official `https://github.com/Ethereum/EIPs` repository. Each item should be a bullet point.
  * ** Use `https://ethereum-magicians.org` for supplementary discussion context. MUST first list all relevant EIPs that are NOT ERCs under a label like: EIPs (Ethereum improvement proposals): Following that, MUST list all relevant ERCs under a label: ERCs (application layer): 
  * **Focus:**
      * New EIPs/ERCs (identified by merged Draft PRs in `Ethereum/EIPs`).
      * EIPs/ERCs moving to "Review," "Last Call," "Final," or "Stagnant" (identified by merged PRs reflecting these status changes in `Ethereum/EIPs`).
      * Significant community discussions (link to `ethereum-magicians.org` or relevant GitHub Issues/PRs within the EIPs repo).
      * Breakdowns or explanations of important or complex EIPs/ERCs.
  * **Primary Sources for this Section:**
      * `https://github.com/Ethereum/EIPs` (for new proposals, status changes via merged PRs, and official EIP content).
      * `https://ethereum-magicians.org` (for community discussions and context around EIPs/ERCs).
  * **Keywords for Search (Focus on monitoring Ethereum/EIPs repo activity):** "New EIP," "New ERC," "EIP status change," "ERC status change," "Ethereum Improvement Proposal discussion," "Ethereum Magicians EIP."


**Developer Stuff**
  * **Content:** Updates on developer tools, frameworks, libraries, smart contract languages, and important resources for builders, from the past 7 days. Each item should be a bullet point.
  * **Focus:**
      * New versions or major feature releases for popular developer tools (e.g., Foundry, Hardhat, Remix, Ape, Tenderly, Infura, Alchemy).
      * Updates to smart contract languages (Solidity, Vyper) or new development patterns.
      * New libraries or SDKs that simplify dApp development.
      * Important tutorials, workshops, developer grants, or documentation updates.
      * Security tools for developers (e.g., linters, static analyzers).
  * **Keywords for Search (Starting Points):** "[Tool Name] update," "Ethereum developer tools," "Solidity news," "Vyper news," "dApp development resources."


**Security**
  * **Content:** Report on security incidents, vulnerabilities, audits, and best practices relevant to the Ethereum ecosystem, from the past 7 days. Each item should be a bullet point.
  * **Focus:**
      * Details of any significant DeFi exploits or hacks (protocol, amount lost, nature of vulnerability, post-mortems).
      * Newly disclosed vulnerabilities in smart contracts, clients, wallets, or L2s.
      * Important security audit releases for major protocols.
      * New tools, standards, or initiatives aimed at improving ecosystem security (e.g., ERC-7265).
      * Discussions on formal verification, bug bounties.
  * **Keywords for Search (Starting Points):** "DeFi hack," "Ethereum security vulnerability," "smart contract audit," "crypto exploit report," "Ethereum bug bounty."


**Ecosystem**
  * **Content:** Broader news from the Ethereum ecosystem, including DAOs, NFTs, public goods, and community initiatives, from the past 7 days. Each item should be a bullet point.
  * **Focus:**
      * Major project milestones or product launches not covered in more specific sections.
      * Significant DAO governance proposals, votes, or treasury actions.
      * Updates on public goods funding initiatives (e.g., Gitcoin Grants rounds, Protocol Guild, ESP grants).
      * Noteworthy NFT collections, market trends, or infrastructure developments (unless covered in "Notable at app layer").
      * Community-led events, educational initiatives, or important discussions.
  * **Keywords for Search (Starting Points):** "Ethereum project launch," "DAO news," "Gitcoin grants," "NFT news Ethereum," "Ethereum community."


**Enterprise**
  * **Content:** Updates on how enterprises are using Ethereum technology (public, private, or hybrid), from the past 7 days. This section can be brief or omitted if no significant news. Each item should be a bullet point.
  * **Focus:**
      * New enterprise use cases, pilots, or consortia forming around Ethereum.
      * Announcements from organizations like the Enterprise Ethereum Alliance (EEA) or Baseline Protocol.
  * **Keywords for Search (Starting Points):** "Enterprise Ethereum," "blockchain for business," "Baseline Protocol."


**Notable at app layer**
  * **Content:** Highlight interesting new decentralized applications (dapps), user-facing innovations, or significant updates to existing applications on Ethereum or L2s, from the past 7 days. Each item should be a bullet point.
  * **Focus:**
      * Innovative or unique dapps gaining traction.
      * Significant feature releases or milestones for established applications.
      * Trends in application development (e.g., SocialFi, DePIN, new gaming models).
  * **Keywords for Search (Starting Points):** "New Ethereum dApp," "[dApp Name] update," "DeFi project launch," "NFT marketplace news."


**Regulation/Business/Tokens**
  * **Content:** News related to cryptocurrency regulation affecting Ethereum globally, significant business adoption, and important token-related developments (excluding price speculation), from the past 7 days. Each item should be a bullet point.
  * **Focus:**
      * New regulatory proposals, guidelines, or enforcement actions from governments/agencies.
      * Major legal cases or rulings involving Ethereum, DeFi, or crypto assets.
      * Significant institutional adoption, investment, or product launches related to Ethereum (e.g., ETFs, custody solutions).
      * Partnerships between traditional businesses and Ethereum-based projects.
      * Important news related to token standards, tokenomics of major projects (if not covered elsewhere), or utility of tokens.
  * **Keywords for Search (Starting Points):** "Ethereum regulation news," "crypto policy," "institutional crypto," "SEC crypto," "[Major Token] news."


**Onchain Stats**
  * **Content:** Key metrics and notable trends observed on the Ethereum network and its ecosystem, reflecting data from the past 7 days or current stats. Each item should be a bullet point.
  * **Focus:**
      * Average gas prices (Gwei) and transaction fee trends; impact of EIP-4844.
      * ETH price (briefly, e.g., ETH/USD, ETH/BTC ranges or changes over the week).
      * Network activity (e.g., transaction count, active addresses, contract deployments).
      * DeFi TVL (Total Value Locked) changes and trends.
      * Staking statistics (e.g., total ETH staked, validator count, changes over the week).
      * Relevant NFT market statistics (e.g., sales volume, unique buyers).
  * **Keywords for Search (Starting Points):** "Ethereum gas fees," "ETH price chart," "Ethereum on-chain data Dune," "DeFi TVL," "Ethereum staking stats."


**Miscellaneous**
  * **Content:** A collection of other interesting articles, blog posts, podcasts, videos, or discussions from the past 7 days that don't fit neatly into other categories but are relevant and insightful for the Ethereum community. Each item should be a bullet point.
  * **Focus:**
      * Thought-provoking opinion pieces or long-form analyses from influential figures.
      * Significant community discussions on social media or forums.
      * Educational content explaining complex Ethereum concepts.
      * Links to useful tools or resources not covered elsewhere.
  * **Keywords for Search (Starting Points):** "Ethereum community discussion," "[Influencer Name] Ethereum blog/podcast," "Ethereum explained."


**Job Postings**
  * **Content:** List job opportunities within the Ethereum ecosystem, ideally posted or highlighted in the past 7 days. Each item should be a bullet point.
  * **Focus:** Roles from various companies and projects in the space.
  * **Keywords for Search (Starting Points):** "Ethereum jobs," "blockchain developer jobs," "crypto jobs [specific role]."


**Upcoming Dates of Note**
  * **Content:** A list of important upcoming Ethereum-related virtual and in-person events, conferences, workshops, and deadlines. Each item should be a bullet point.
  * **Focus:**
      * Events scheduled for the next few weeks/months.
      * Important deadlines for grant applications, EIP comments, testnet participation, calls for papers.
  * **Keywords for Search (Starting Points):** "Ethereum conference," "Devcon," "ETHGlobal hackathon," "blockchain events calendar."


**General AI Instructions:**
  * **Strict Date Adherence:** All reported news, updates, and highlights **MUST originate from events, publications, or data released strictly within the specified 7-day period.** No exceptions. If an event is recurring, only report on the instance that happened in the past 7 days.
  * **Primary Information Sources & Verification:**
      * **Core Ethereum Development & Discussion (Highest Priority):** Your primary sources for core protocol developments, EIP discussions, research, and official meeting notes MUST be:
          * The official Ethereum GitHub organization: `https://github.com/ethereum` (especially `https://github.com/ethereum/pm` for core developer meeting agendas/notes, and `https://github.com/Ethereum/EIPs` for EIP/ERC proposals and status).
          * Ethereum Magicians forum: `https://ethereum-magicians.org/` (for EIP/ERC discussions and community proposals).
          * ETHResearch forum: `https://ethresear.ch/` (for research discussions).
      * **Other Key Official & Specialized Sources:**
          * **Official Announcements:** `blog.ethereum.org`.
          * **Core Dev Call Summaries (Specific Author):** Posts by `@abcoathup` on `https://ethereum-magicians.org/u/abcoathup/activity` (cross-verify call dates and key decisions with `ethereum/pm`).
          * **Client Diversity Data:** `clientdiversity.org`.
      * Actively seek out these primary sources for relevant sections. While secondary sources (reputable news outlets, project blogs) can be used for broader ecosystem news, core technical details, official stances, and dates of events MUST be grounded in and verified against these primary sources.
  * **Secondary Sources:** Supplement with reputable crypto news outlets (e.g., The Defiant, CoinDesk, Decrypt, Blockworks, Rekt News for security), project blogs, and well-known community figures. Critically evaluate the reliability of secondary sources.
  * **Summarization:** For each item, provide a concise summary (typically 1-3 sentences). Capture the essence of the news and its significance.
  * **Linking:** **Crucially, include a direct link to the original source for each piece of news.**
  * **Tone:** Maintain a neutral, objective, and informative tone. Avoid speculation or unverified claims.
  * **Structure & Formatting:**
      * Organize the information clearly under the respective headings as specified.
      * **All individual news items, links, or list entries under any heading MUST be formatted as bullet points.** (e.g., `* Item 1...`, `* Item 2...`).
  * **Accuracy & Timeliness:**
      * **Actively verify all facts, especially dates of events (like developer calls, releases), and figures against primary, official sources before inclusion.**
      * If no significant update for a specific topic or section occurred within the 7-day window, explicitly state that or omit the section as per "Week in Ethereum News" style, rather than including older information.
      * Cross-reference information where possible.
  * **Completeness & Relevance:**
      * Strive for comprehensive coverage of significant events, but use judgment to filter out minor or irrelevant updates.
      * **Crucially, ALL sections should ONLY be included in the output if there were relevant updates for them in the past 7 days.** If a section has no significant news for the week, it should be omitted entirely to match the lean style of "Week in Ethereum News."
  * **"Week in Ethereum News" Style:** **This is paramount.** Emulate the exact section titling, dynamic inclusion of all sections based on weekly content, general style, depth, and comprehensiveness of a typical "Week in Ethereum News" issue. The AI should "read" several recent issues to internalize the style, tone, and level of detail.

**Output Format:**
The final output should be a well-formatted newsletter in Markdown, suitable for publication, with all original links and references preserved. Start with the "Highlight of the Week" section. All list items must use bullet points.
