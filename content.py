# -*- coding: utf-8 -*-
"""
Page copy for kryptooo. Tokens replaced at build time:
  [[COMPANY]] [[DOMAIN]] [[EMAIL]] [[PRIVACY_EMAIL]] [[PRESS_EMAIL]] [[AD_EMAIL]]
  [[CORR_EMAIL]] [[UPDATED]] [[ADDRESS_LINE]]
"""

# --------------------------------------------------------------------------
# Educational articles (evergreen; no market claims that can go stale)
# --------------------------------------------------------------------------
ARTICLES = [
{
 "slug": "how-to-read-a-stock-quote",
 "title": "How to read a stock quote",
 "tag": "Stocks", "read": 5,
 "desc": "Last price, bid and ask, volume, market cap, 52-week range and P/E explained in plain language.",
 "lede": "A quote packs a dozen numbers into a few lines. Here is what each one measures, and which ones deserve your attention.",
 "takeaways": [
   "The headline price is the last trade, not a price you are guaranteed to get.",
   "Bid, ask and volume tell you how easy it is to trade, not whether a stock is cheap.",
   "Market cap and P/E give context, but only when compared with similar companies."],
 "body": """
<h2>The price and the change</h2>
<p>The large number on a quote is the <strong>last price</strong>: the most recent trade that was reported. The change beside it is measured against the <strong>previous close</strong>, the final price of the prior trading session. If the last price is 102 and the previous close was 100, the quote shows +2.00, or +2.00%.</p>
<p>Because the last price only reflects the latest trade, it can lag the real market in thinly traded stocks. For a stock that trades millions of shares a day, the difference is usually a fraction of a cent.</p>

<h2>Bid, ask and the spread</h2>
<p>The <strong>bid</strong> is the highest price a buyer is currently offering. The <strong>ask</strong> is the lowest price a seller will accept. The gap between them is the <strong>spread</strong>. A buyer who wants shares immediately pays the ask, and a seller who wants out immediately receives the bid.</p>
<p>Tight spreads usually signal an active, liquid market. Wide spreads are a hidden cost, which is why they matter most for small or lightly traded companies.</p>

<h2>Open, high and low</h2>
<p>The <strong>open</strong> is the first price of the session. The <strong>day high</strong> and <strong>day low</strong> mark the extremes reached so far. Together they show the day's range, which helps you judge whether the current price sits near the top, middle or bottom of where the stock has traded.</p>

<h2>Volume</h2>
<p><strong>Volume</strong> is the number of shares traded during the session. A raw number means little on its own, so compare it with the stock's <em>average volume</em>. A move on well above-average volume generally reflects broader participation than the same move on light volume.</p>

<h2>Market capitalization</h2>
<p>Market cap is the share price multiplied by the number of shares outstanding. It measures the market's total valuation of the company, and it is the standard way to compare company size. Our guide to <a href="/learn/what-is-market-capitalization.html">market capitalization</a> covers the details.</p>

<h2>52-week range</h2>
<p>The <strong>52-week high and low</strong> show the highest and lowest prices over the past year. A stock near the top of its range has been rising; one near the bottom has been falling. Neither fact says anything about what happens next.</p>

<h2>The P/E ratio</h2>
<p>The <strong>price-to-earnings ratio</strong> divides the share price by earnings per share. A P/E of 20 means investors are paying 20 for each 1 of annual profit. <em>Trailing</em> P/E uses the last twelve months of reported earnings. <em>Forward</em> P/E uses analyst estimates of future earnings. A high P/E can mean strong growth expectations, and a low one can mean the opposite. P/E is most useful when comparing companies in the same industry, and it is not meaningful for companies with no profits.</p>

<h2>Delayed versus real-time quotes</h2>
<p>Many free quote pages show data that is delayed, commonly by 15 minutes, because real-time exchange data is licensed. Always check whether a quote is delayed before acting on it. The quotes on kryptooo are simulated for demonstration and should never be used for trading decisions.</p>
"""
},
{
 "slug": "what-is-market-capitalization",
 "title": "What is market capitalization?",
 "tag": "Fundamentals", "read": 4,
 "desc": "How market cap is calculated for stocks and crypto, why circulating supply matters, and what the number does not tell you.",
 "lede": "Market cap is the quickest way to compare the size of companies and digital assets, and one of the easiest numbers to misread.",
 "takeaways": [
   "Market cap equals price multiplied by the number of shares or coins in circulation.",
   "It measures size, not value: a larger company is not automatically a better investment.",
   "For crypto, circulating supply and fully diluted value can differ a lot."],
 "body": """
<h2>The formula</h2>
<p>For a listed company, <strong>market capitalization = share price × shares outstanding</strong>. A company with 200 million shares trading at 50 has a market cap of 10 billion. Because the share price changes all day, so does market cap.</p>

<h2>Why price alone is misleading</h2>
<p>A 500 share price does not make a company bigger than one priced at 50. A company can have few shares at a high price or many shares at a low price. Market cap removes that distortion by accounting for the share count, which is why indices and fund managers use it rather than price.</p>

<h2>Size categories</h2>
<p>Providers group companies into <strong>large-cap</strong>, <strong>mid-cap</strong> and <strong>small-cap</strong> tiers. The boundaries vary by index provider and change over time, so treat any single threshold as a convention rather than a rule. In general, larger companies are more established and trade more actively. Smaller companies can grow faster but tend to be more volatile and harder to trade.</p>

<h2>Float-adjusted market cap</h2>
<p>Some shares are held by insiders or governments and rarely trade. <strong>Float-adjusted</strong> market cap counts only the shares available to the public. Many major indices weight companies by float-adjusted market cap because it better reflects what investors can actually buy.</p>

<h2>Market cap in crypto</h2>
<p>For digital assets, market cap is price multiplied by <strong>circulating supply</strong>, the coins currently available. Two related figures are worth knowing:</p>
<ul>
  <li><strong>Total supply</strong>: coins that exist now, including some that may be locked or reserved.</li>
  <li><strong>Maximum supply</strong>: the hard cap, if the protocol has one.</li>
  <li><strong>Fully diluted valuation</strong>: price multiplied by the maximum supply, which shows the implied size if every coin were released.</li>
</ul>
<p>An asset with a small circulating supply and a large maximum supply can look cheap on market cap while being expensive on a fully diluted basis.</p>

<h2>What market cap does not tell you</h2>
<ul>
  <li>It is not the amount of money invested in the asset. Trades at the margin set the price for everything outstanding.</li>
  <li>It does not account for debt. Two companies with the same market cap can have very different balance sheets.</li>
  <li>It says nothing about whether the price is fair. For that you need earnings, cash flow and growth, or in crypto, usage and supply dynamics.</li>
</ul>
"""
},
{
 "slug": "how-stock-market-indices-work",
 "title": "How stock market indices work",
 "tag": "Indices", "read": 5,
 "desc": "What the S&P 500, Dow and Nasdaq Composite actually measure, and how weighting changes what an index tells you.",
 "lede": "Indices summarize a whole market in one number. How that number is built determines what it can and cannot tell you.",
 "takeaways": [
   "An index is a rules-based basket of securities, not an asset you can buy directly.",
   "Price weighting, market-cap weighting and equal weighting give different answers from the same stocks.",
   "Index funds let investors hold a basket that follows an index."],
 "body": """
<h2>What an index is</h2>
<p>A stock market index tracks the performance of a defined group of securities. The group, the rules for choosing it and the formula for combining the prices are all set by an index provider. Because the index level is just a calculation, you cannot buy it directly. You can buy funds that hold the underlying stocks.</p>

<h2>Three common weighting methods</h2>
<table>
<thead><tr><th>Method</th><th>How it works</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Price-weighted</td><td>Stocks with higher share prices have more influence, regardless of company size.</td><td>Dow Jones Industrial Average</td></tr>
<tr><td>Market-cap-weighted</td><td>Larger companies have more influence in proportion to their (often float-adjusted) market cap.</td><td>S&amp;P 500, Nasdaq Composite</td></tr>
<tr><td>Equal-weighted</td><td>Every constituent has the same weight, rebalanced periodically.</td><td>Equal-weight versions of major indices</td></tr>
</tbody></table>

<h2>The major US benchmarks</h2>
<ul>
  <li><strong>S&amp;P 500</strong>: roughly 500 large US companies selected by a committee under published eligibility rules, weighted by float-adjusted market cap. It is widely used as a gauge of the US large-cap market.</li>
  <li><strong>Dow Jones Industrial Average</strong>: 30 large US companies, price-weighted. Its small size and weighting method mean it can behave differently from broader indices.</li>
  <li><strong>Nasdaq Composite</strong>: covers most of the common stocks listed on the Nasdaq exchange, weighted by market cap. It has a heavy technology tilt.</li>
</ul>

<h2>Why weighting matters</h2>
<p>In a market-cap-weighted index, a handful of the biggest companies can drive much of the daily move. When those names rise, the index can climb even if most stocks are flat. That is why analysts also look at <strong>market breadth</strong>, such as the number of stocks rising versus falling, alongside the headline level.</p>

<h2>Price return versus total return</h2>
<p>Most headline index levels are <strong>price return</strong>, which ignores dividends. A <strong>total return</strong> version assumes dividends are reinvested and therefore grows faster over time. When comparing a fund's performance with an index, make sure you are comparing like with like.</p>

<h2>Rebalancing and reconstitution</h2>
<p>Providers periodically review membership. Companies can be added when they grow into eligibility and removed when they shrink, merge or fail to meet criteria. This keeps the index representative, but it also means an index's past composition differs from today's.</p>

<h2>Using indices sensibly</h2>
<p>Indices are useful benchmarks. They show what the market, or a part of it, has done and give you a yardstick for your own results. They do not predict future returns, and a fund tracking an index will differ slightly from it because of fees and trading costs.</p>
"""
},
{
 "slug": "stocks-vs-crypto",
 "title": "Stocks vs crypto: how the two markets differ",
 "tag": "Markets", "read": 6,
 "desc": "Trading hours, settlement, custody, regulation, valuation and volatility compared side by side.",
 "lede": "Both trade on screens with live prices, but stocks and cryptocurrencies are built on different foundations. Knowing the differences helps you read each market correctly.",
 "takeaways": [
   "Crypto trades around the clock; stock exchanges have fixed sessions.",
   "Stocks represent claims on companies; most cryptoassets represent something different, and valuation is harder.",
   "Custody and regulation are very different, and so are the risks."],
 "body": """
<h2>Side-by-side comparison</h2>
<table>
<thead><tr><th>Feature</th><th>Stocks</th><th>Crypto</th></tr></thead>
<tbody>
<tr><td>Trading hours</td><td>Exchange sessions on business days, with limited pre-market and after-hours trading</td><td>Continuous, every day of the year</td></tr>
<tr><td>What you own</td><td>A share of a company, with rights that depend on the share class</td><td>A token or coin whose rights depend on the protocol; often no claim on cash flows</td></tr>
<tr><td>Settlement</td><td>Typically one business day for US equities, handled by clearing houses</td><td>On the network or the platform, often within minutes, depending on the chain</td></tr>
<tr><td>Custody</td><td>Usually held by a broker in your name</td><td>Held on an exchange or in a wallet you control, which brings key-management risk</td></tr>
<tr><td>Regulation</td><td>Mature securities laws and disclosure requirements in most major markets</td><td>Varies widely by country and by asset, and is still evolving</td></tr>
<tr><td>Price drivers</td><td>Earnings, interest rates, economic data, company news</td><td>Adoption, supply schedules, liquidity, sentiment, regulatory news</td></tr>
<tr><td>Typical volatility</td><td>Lower on average for large companies</td><td>Often substantially higher</td></tr>
</tbody></table>

<h2>Valuation is harder in crypto</h2>
<p>A stock can be analyzed using revenue, profit and cash flow. Many cryptoassets have no such cash flows, so analysts rely on other signals: network activity, supply issuance, developer activity and market sentiment. These are useful but less standardized, and disagreements about fair value can be extreme.</p>

<h2>Liquidity and market structure</h2>
<p>Large US stocks trade on regulated exchanges with consolidated price reporting. Crypto trades across many venues, each with its own order book, so the same asset can have slightly different prices in different places. Liquidity for the biggest coins is deep, but it can thin quickly for smaller tokens, especially in a sell-off.</p>

<h2>Risks that are specific to each</h2>
<ul>
  <li><strong>Stocks:</strong> company-specific risk such as weak earnings, management problems or sector downturns, plus broad market risk.</li>
  <li><strong>Crypto:</strong> larger price swings, custody and security risk, exchange failures, protocol bugs and sudden regulatory changes.</li>
</ul>

<h2>Why compare them on one screen</h2>
<p>Seeing both markets together shows how they behave in different conditions. Sometimes they move in the same direction because both respond to liquidity and risk appetite. At other times they diverge. That is the reason kryptooo puts them on a single tape, with a toggle to focus on either one.</p>

<div class="note"><strong>Not advice</strong><p>This article is general education. It does not recommend buying or selling any asset. Consider your own circumstances and speak with a licensed professional before investing.</p></div>
"""
},
{
 "slug": "crypto-fear-and-greed-index-explained",
 "title": "The crypto fear and greed index, explained",
 "tag": "Crypto", "read": 5,
 "desc": "What a fear and greed gauge measures, how kryptooo builds its version, and how to use sentiment indicators with care.",
 "lede": "Sentiment gauges compress many signals into one number from 0 to 100. Useful as context, risky as a trading rule.",
 "takeaways": [
   "Low scores mean fear, high scores mean greed, and the middle is neutral.",
   "Different providers use different inputs, so scores are not comparable across sites.",
   "Sentiment describes the present mood. It does not forecast the future."],
 "body": """
<h2>The idea</h2>
<p>Markets are driven partly by numbers and partly by emotion. A fear and greed index tries to measure the emotional side. Scores near 0 indicate <strong>extreme fear</strong>, near 100 indicate <strong>extreme greed</strong>, and the middle of the range is <strong>neutral</strong>. The usual shorthand is that fear can push prices below what fundamentals justify, while greed can push them above.</p>

<h2>Typical inputs</h2>
<p>Publicly available versions of the gauge generally blend several signals. Common ones include price volatility compared with recent averages, market momentum and trading volume, social media activity, survey data, the share of the market held by the largest asset, and search trends. Each provider chooses its own inputs and weights, so a score on one site can differ from a score on another.</p>

<h2>How the kryptooo gauge is built</h2>
<p>The gauge on our crypto page is computed from the twelve assets we track. It averages five components, each scaled from 0 to 100:</p>
<table>
<thead><tr><th>Component</th><th>What it looks at</th><th>Weight</th></tr></thead>
<tbody>
<tr><td>Momentum</td><td>Average 24-hour price change across the tracked coins</td><td>30%</td></tr>
<tr><td>Breadth</td><td>Share of coins trading above their opening price</td><td>20%</td></tr>
<tr><td>Volatility</td><td>How large the average move is; calmer markets score higher</td><td>20%</td></tr>
<tr><td>Dominance</td><td>Bitcoin's share of total market cap; a rising share is read as risk aversion</td><td>15%</td></tr>
<tr><td>Volume</td><td>Trading volume relative to its typical level</td><td>15%</td></tr>
</tbody></table>
<p>Because kryptooo's data is simulated for demonstration, the gauge reflects that simulation and not the real market.</p>

<h2>Reading the zones</h2>
<ul>
  <li><strong>0 to 24, extreme fear:</strong> broad selling and elevated volatility.</li>
  <li><strong>25 to 44, fear:</strong> caution outweighs optimism.</li>
  <li><strong>45 to 54, neutral:</strong> no strong lean.</li>
  <li><strong>55 to 74, greed:</strong> rising prices and confidence.</li>
  <li><strong>75 to 100, extreme greed:</strong> strong rallies and crowded positioning.</li>
</ul>

<h2>Using it responsibly</h2>
<p>Some investors read extremes as contrarian signals, on the theory that panic creates bargains and euphoria precedes pullbacks. Others use sentiment to confirm a trend. Both approaches can fail: markets can stay fearful or greedy for long stretches. Treat the gauge as one input among many, and never as a standalone reason to trade.</p>
"""
},
{
 "slug": "diversification-basics",
 "title": "Diversification basics",
 "tag": "Investing basics", "read": 5,
 "desc": "Why spreading risk across assets can smooth results, how correlation works, and what diversification cannot do.",
 "lede": "The oldest rule in investing is also one of the most misunderstood. Here is what diversification does, and what it does not.",
 "takeaways": [
   "Diversification reduces the impact of any single holding, not market risk itself.",
   "Assets that move differently from each other offer the most benefit.",
   "Rebalancing keeps your mix aligned with your plan."],
 "body": """
<h2>The core idea</h2>
<p>Diversification means spreading money across different investments so that no single one can sink your whole portfolio. If one company stumbles, the others can offset part of the loss. The goal is not to maximize returns but to improve the balance between return and risk.</p>

<h2>Correlation</h2>
<p><strong>Correlation</strong> measures how two assets move relative to each other, on a scale from -1 to +1. A value near +1 means they tend to rise and fall together. Near 0 means little relationship. Negative values mean they tend to move in opposite directions. Holding ten assets that are all highly correlated provides far less protection than holding a few that are not.</p>

<h2>Layers of diversification</h2>
<ul>
  <li><strong>Across asset classes:</strong> for example equities, bonds, cash and, for some investors, a small allocation to alternatives or digital assets.</li>
  <li><strong>Within an asset class:</strong> multiple companies, sectors and company sizes instead of one stock.</li>
  <li><strong>Geographic:</strong> exposure to more than one country or region.</li>
  <li><strong>Over time:</strong> investing at regular intervals rather than all at once, sometimes called dollar-cost averaging.</li>
</ul>

<h2>Concentration risk</h2>
<p>The opposite of diversification is concentration. A portfolio dominated by one stock, one sector or one asset can deliver outsized gains, and outsized losses. Cap-weighted index funds can themselves become concentrated if a few companies grow to dominate the index, so it is worth looking at what a fund actually holds.</p>

<h2>Rebalancing</h2>
<p>Over time, winners grow and losers shrink, so your mix drifts from your plan. <strong>Rebalancing</strong> means periodically selling some of what has grown and buying what has lagged to restore your target weights. Some investors rebalance on a schedule, such as once a year, and others when an allocation drifts by a set amount. Taxes and trading costs matter here, so consider them.</p>

<h2>What diversification cannot do</h2>
<p>It does not guarantee a profit or protect against loss in a broad downturn. In a severe market stress, correlations between many assets can rise together, which reduces the benefit just when you want it. Diversification manages specific risk. It cannot remove market risk.</p>

<div class="note"><strong>Not advice</strong><p>This is general education. The right mix depends on your goals, time horizon, and tolerance for risk. A licensed financial adviser can help you decide.</p></div>
"""
},
]

# --------------------------------------------------------------------------
# Glossary
# --------------------------------------------------------------------------
GLOSSARY = [
("Ask", "The lowest price at which a seller is currently willing to sell a security."),
("Bid", "The highest price at which a buyer is currently willing to buy a security."),
("Bear market", "A prolonged decline in prices, commonly defined as a fall of 20% or more from a recent peak."),
("Bull market", "A prolonged period of rising prices and generally improving investor confidence."),
("Circulating supply", "The number of coins or tokens currently available to the public. Used to calculate a cryptoasset's market cap."),
("Close", "The final trading price of a security in a session. The previous close is the baseline for the daily change."),
("Cryptocurrency", "A digital asset that uses cryptography and a distributed ledger to record ownership and transfers."),
("Dividend", "A distribution of a portion of a company's profits to its shareholders, usually paid in cash."),
("Dominance", "An asset's share of total cryptocurrency market cap. Bitcoin dominance is the most widely followed."),
("ETF", "Exchange-traded fund. A fund that holds a basket of assets and trades on an exchange like a single stock."),
("Fear and greed index", "A 0 to 100 gauge of market sentiment, where low values signal fear and high values signal greed."),
("Float", "The shares of a company that are available for public trading, excluding those held by insiders or governments."),
("Fully diluted valuation", "Price multiplied by the maximum possible supply of a token. Shows implied size if all coins were issued."),
("Heatmap", "A visual of many assets at once, with tile size showing market cap and color showing price change."),
("Index", "A rules-based measure of a group of securities, such as the S&amp;P 500. It cannot be bought directly."),
("Liquidity", "How easily an asset can be bought or sold without moving its price. Tight spreads and high volume indicate high liquidity."),
("Market capitalization", "The total market value of a company or cryptoasset: price multiplied by shares or coins outstanding."),
("Market order", "An instruction to buy or sell immediately at the best available price."),
("Limit order", "An instruction to buy or sell only at a specified price or better."),
("Momentum", "The tendency of recent price direction to continue. Often measured over days or months."),
("P/E ratio", "Price-to-earnings ratio. The share price divided by earnings per share, used to compare valuations."),
("Previous close", "The closing price from the last completed session."),
("Rebalancing", "Adjusting a portfolio back to its target allocation after price changes have shifted the weights."),
("Sector", "A group of companies in the same broad industry, such as technology or energy."),
("Spread", "The difference between the bid and the ask. A narrower spread usually means a more liquid market."),
("Stablecoin", "A cryptoasset designed to hold a steady value, typically pegged to a currency such as the US dollar."),
("Ticker symbol", "A short code that identifies a security, such as AAPL for Apple or BTC for Bitcoin."),
("Total return", "Performance including both price changes and reinvested dividends or distributions."),
("Volatility", "The degree to which an asset's price fluctuates over time. Higher volatility means larger swings."),
("Volume", "The number of shares, contracts or coins traded in a period."),
("Watchlist", "A personal list of securities you want to track without owning them."),
("52-week range", "The highest and lowest prices of a security over the past year."),
]

# --------------------------------------------------------------------------
# Company, policy and legal pages
# --------------------------------------------------------------------------
PAGES = {

"about": {
 "title": "About kryptooo",
 "desc": "kryptooo is a markets information site that puts stocks, crypto and indices on one tape, with plain-language guides for readers.",
 "lede": "We build tools and write guides that make financial markets easier to read, whether you follow equities, digital assets or both.",
 "toc": True,
 "body": """
<h2>What we do</h2>
<p>kryptooo is a markets information site. Our dashboard puts US large-cap stocks, major cryptocurrencies and benchmark indices on a single live tape, with charts, movers, a market map and a personal watchlist. Alongside it we publish educational guides and a glossary that explain how markets work.</p>

<h2>Why we exist</h2>
<p>Most market sites were designed for one asset class. Stocks and crypto live on different screens, use different vocabulary and are often explained at very different levels. We think readers benefit from seeing them side by side, using one consistent set of terms and one consistent design.</p>

<h2>Our principles</h2>
<ul>
  <li><strong>Clarity first.</strong> Dense data should still be easy to scan. We label things plainly and avoid jargon where a simpler word works.</li>
  <li><strong>Accuracy and honesty.</strong> We explain our methods, state when data is delayed or simulated, and correct mistakes openly. See our <a href="/editorial-policy.html">Editorial Policy</a>.</li>
  <li><strong>Independence.</strong> Advertising never influences what we write. See our <a href="/advertising-policy.html">Advertising Policy</a>.</li>
  <li><strong>Respect for privacy.</strong> We collect as little as we can. Details are in our <a href="/privacy-policy.html">Privacy Policy</a>.</li>
</ul>

<h2>About the data on this site</h2>
<div class="note"><strong>Simulated demonstration data</strong><p>The quotes, volumes, index levels, charts and sentiment gauge currently shown on kryptooo are generated by a simulation engine. They are designed to behave like real markets so the product can be demonstrated, but they are not real prices. Do not use them to make trading or investment decisions. See our <a href="/disclaimer.html">Disclaimer</a>.</p></div>

<h2>What we are not</h2>
<p>kryptooo is not a broker, exchange, bank or investment adviser. We do not hold customer funds, execute trades or offer personalized recommendations. Everything we publish is general information for education.</p>

<h2>Get in touch</h2>
<p>Questions, corrections and feedback are welcome. Visit our <a href="/contact.html">Contact page</a> or write to <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>.</p>
[[ADDRESS_LINE]]
"""
},

"contact": {
 "title": "Contact us",
 "desc": "Contact kryptooo for support, corrections, privacy requests, advertising and press enquiries.",
 "lede": "Choose the right address below, or send us a message with the form. We read everything.",
 "toc": False,
 "body": """
<div class="contact-grid">
  <div><b>General and support</b><span>Questions about the site or how to use it</span><a href="mailto:[[EMAIL]]">[[EMAIL]]</a></div>
  <div><b>Corrections</b><span>Spotted an error in a guide? Tell us</span><a href="mailto:[[CORR_EMAIL]]">[[CORR_EMAIL]]</a></div>
  <div><b>Privacy requests</b><span>Access, deletion and other data rights</span><a href="mailto:[[PRIVACY_EMAIL]]">[[PRIVACY_EMAIL]]</a></div>
  <div><b>Advertising and partnerships</b><span>Sponsorship and media enquiries</span><a href="mailto:[[AD_EMAIL]]">[[AD_EMAIL]]</a></div>
</div>

<h2>Send a message</h2>
<form class="form" id="contactForm" data-to="[[EMAIL]]">
  <div class="field"><label for="name">Your name</label><input id="name" name="name" autocomplete="name" required></div>
  <div class="field"><label for="email">Your email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
  <div class="field"><label for="topic">Topic</label>
    <select id="topic" name="topic"><option>General</option><option>Correction</option><option>Privacy request</option><option>Advertising</option><option>Press</option></select></div>
  <div class="field"><label for="subject">Subject</label><input id="subject" name="subject" required></div>
  <div class="field"><label for="message">Message</label><textarea id="message" name="message" required></textarea></div>
  <button class="btn" type="submit">Prepare email</button>
  <p id="formNote" class="muted" role="status" style="font-size:13.5px"></p>
</form>

<h2>Before you write</h2>
<ul>
  <li>We cannot give personal investment advice or recommend what to buy or sell.</li>
  <li>We do not hold accounts or funds, so we cannot help with trades, deposits or withdrawals at any broker or exchange.</li>
  <li>We aim to reply to messages within five business days.</li>
</ul>
[[ADDRESS_LINE]]
"""
},

"privacy-policy": {
 "title": "Privacy Policy",
 "desc": "How kryptooo collects, uses and protects information, including cookies and Google advertising.",
 "lede": "We collect as little personal information as we can. This policy explains what we do collect, why, and the choices you have.",
 "toc": True,
 "updated": True,
 "body": """
<h2>Who we are</h2>
<p>This policy applies to the website at <strong>[[DOMAIN]]</strong>, operated by [[COMPANY]] ("kryptooo", "we", "us"). You can reach us about privacy at <a href="mailto:[[PRIVACY_EMAIL]]">[[PRIVACY_EMAIL]]</a>.</p>

<h2>Information we collect</h2>
<h3>Information you provide</h3>
<p>You do not need an account to use kryptooo. If you email us, we receive your email address and whatever you include in your message. We use it only to respond and to keep a record of the conversation.</p>
<h3>Information collected automatically</h3>
<p>When you visit, our hosting provider and our servers may log technical data such as your IP address, browser type, device type, pages requested, referring page, and date and time. This is standard for operating and securing a website.</p>
<h3>Information stored on your device</h3>
<p>We store a small amount of data in your browser: your chosen theme (light or dark) and your cookie choice. Your watchlist is kept only in your browser's memory while the page is open, and it is not sent to us.</p>

<h2>How we use information</h2>
<ul>
  <li>To operate, maintain and secure the site.</li>
  <li>To respond to your messages and requests.</li>
  <li>To understand, in aggregate, how the site is used so we can improve it.</li>
  <li>To show advertising that supports the site, as described below.</li>
  <li>To comply with legal obligations.</li>
</ul>

<h2>Legal bases (EEA, UK and Switzerland)</h2>
<p>Where data protection law requires a legal basis, we rely on <strong>consent</strong> for advertising cookies and similar technologies, <strong>legitimate interests</strong> for security and site improvement, and <strong>legal obligation</strong> where applicable. You can withdraw consent at any time using "Cookie preferences" in the footer.</p>

<h2>Advertising and Google</h2>
<p>We may display ads served by third parties, including Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites.</p>
<ul>
  <li>Google's use of advertising cookies enables it and its partners to serve ads to you based on your visit to our site and/or other sites on the internet.</li>
  <li>You can opt out of personalized advertising by visiting <a href="https://adssettings.google.com" rel="noopener" target="_blank">Google Ads Settings</a>. You can also opt out of some third-party vendors' use of cookies for personalized advertising at <a href="https://www.aboutads.info" rel="noopener" target="_blank">aboutads.info</a>.</li>
  <li>To learn how Google uses data from sites that use its services, see <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">How Google uses information from sites or apps that use our services</a>.</li>
</ul>
<p>We load advertising scripts only after you accept advertising cookies. If you choose "Essential only", ad scripts are not loaded.</p>

<h2>Cookies</h2>
<p>Our <a href="/cookie-policy.html">Cookie Policy</a> lists the cookies and storage we and our partners use, and how to control them.</p>

<h2>Sharing of information</h2>
<p>We do not sell your personal information for money. We share information only with: service providers that host and secure the site; advertising partners, if you consent to advertising cookies; and authorities, when required by law or to protect rights and safety.</p>

<h2>International transfers</h2>
<p>Our providers may process data in countries other than your own. Where required, we use safeguards such as standard contractual clauses to protect transferred data.</p>

<h2>Retention</h2>
<p>We keep server logs for a limited period needed for security and operations, and correspondence for as long as needed to handle your request and meet legal obligations. Browser-stored settings remain until you clear them.</p>

<h2>Your rights</h2>
<p>Depending on where you live, you may have the right to access, correct, delete or export your personal data, to object to or restrict certain processing, and to withdraw consent. Residents of California may also have the right to know what personal information is collected and to opt out of its "sale" or "sharing" for cross-context behavioral advertising. To exercise a right, email <a href="mailto:[[PRIVACY_EMAIL]]">[[PRIVACY_EMAIL]]</a>. You may also lodge a complaint with your local data protection authority.</p>

<h2>Children</h2>
<p>kryptooo is not directed to children under 16, and we do not knowingly collect personal information from them. If you believe a child has sent us personal information, contact us and we will delete it.</p>

<h2>Security</h2>
<p>We use reasonable technical and organizational measures, including encrypted connections, to protect information. No method of transmission or storage is completely secure.</p>

<h2>External links</h2>
<p>Our pages may link to other websites. We are not responsible for their privacy practices, and we encourage you to read their policies.</p>

<h2>Changes to this policy</h2>
<p>We may update this policy from time to time. The "Last updated" date above shows when it last changed. Material changes will be highlighted on the site.</p>

<h2>Contact</h2>
<p>Privacy questions: <a href="mailto:[[PRIVACY_EMAIL]]">[[PRIVACY_EMAIL]]</a>.</p>
"""
},

"terms-of-service": {
 "title": "Terms of Service",
 "desc": "The terms that govern your use of the kryptooo website, content and tools.",
 "lede": "By using kryptooo, you agree to these terms. Please read them, especially the sections on financial information and liability.",
 "toc": True,
 "updated": True,
 "body": """
<h2>Acceptance of terms</h2>
<p>These Terms of Service ("Terms") govern your access to and use of [[DOMAIN]] and related content and tools (the "Site"), operated by [[COMPANY]]. By using the Site, you agree to these Terms and to our <a href="/privacy-policy.html">Privacy Policy</a>. If you do not agree, do not use the Site.</p>

<h2>Informational purposes only</h2>
<p>The Site provides general financial and market information and education. It is <strong>not</strong> investment, legal, tax or accounting advice, and nothing on the Site is an offer or solicitation to buy or sell any security, cryptoasset or other instrument. Market data on the Site is currently simulated for demonstration. See our <a href="/disclaimer.html">Disclaimer</a>.</p>

<h2>Eligibility</h2>
<p>You must be at least 16 years old, or the age of digital consent in your country if higher, to use the Site.</p>

<h2>Acceptable use</h2>
<p>You agree not to:</p>
<ul>
  <li>use the Site unlawfully or in violation of any applicable regulations;</li>
  <li>scrape, copy or redistribute content or data at scale without written permission;</li>
  <li>interfere with or disrupt the Site, its servers or its security features;</li>
  <li>attempt to gain unauthorized access to any part of the Site or related systems;</li>
  <li>generate artificial ad impressions or clicks, or encourage others to do so;</li>
  <li>use the Site to transmit malware or misleading, defamatory or infringing material.</li>
</ul>

<h2>Intellectual property</h2>
<p>The Site's text, graphics, logos, icons, software and design are owned by or licensed to us and are protected by intellectual property laws. You may view and share links to our pages and quote short excerpts with attribution for non-commercial purposes. Any other use requires our prior written permission.</p>

<h2>Third-party content and advertising</h2>
<p>The Site may contain advertisements and links to third-party websites. We do not control and are not responsible for third-party content, products or services, and inclusion of an ad or link is not an endorsement. Your dealings with advertisers are solely between you and them. See our <a href="/advertising-policy.html">Advertising Policy</a>.</p>

<h2>No warranties</h2>
<p>The Site is provided "as is" and "as available" without warranties of any kind, express or implied, including warranties of accuracy, completeness, merchantability, fitness for a particular purpose and non-infringement. We do not warrant that the Site will be uninterrupted or error-free.</p>

<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by law, [[COMPANY]] and its affiliates, officers, employees and suppliers will not be liable for any indirect, incidental, special, consequential or punitive damages, or for any loss of profits, data or goodwill, or for any investment or trading losses, arising from your use of or inability to use the Site or from reliance on its content. Nothing in these Terms limits liability that cannot be limited under applicable law.</p>

<h2>Indemnity</h2>
<p>You agree to indemnify and hold us harmless from claims, damages and expenses, including reasonable legal fees, arising from your breach of these Terms or misuse of the Site.</p>

<h2>Changes to the Site and Terms</h2>
<p>We may change, suspend or discontinue any part of the Site at any time. We may update these Terms by posting a new version here with a revised date. Your continued use after changes take effect means you accept them.</p>

<h2>Governing law</h2>
<p>These Terms are governed by the laws of the jurisdiction in which [[COMPANY]] is established, without regard to conflict-of-law principles. Courts in that jurisdiction have exclusive authority over disputes, except where mandatory consumer law in your country provides otherwise.</p>

<h2>Contact</h2>
<p>Questions about these Terms: <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>.</p>
"""
},

"disclaimer": {
 "title": "Disclaimer",
 "desc": "Important information about the financial content, simulated data and risks on kryptooo.",
 "lede": "Please read this before relying on anything you see on kryptooo.",
 "toc": True,
 "updated": True,
 "body": """
<h2>No financial advice</h2>
<p>All content on kryptooo, including quotes, charts, rankings, sentiment gauges and educational articles, is for general information and education only. It does not take into account your objectives, financial situation or needs, and it is not personalized investment advice. We are not a registered investment adviser, broker-dealer, or financial planner. Consult a qualified professional before making financial decisions.</p>

<h2>Simulated market data</h2>
<div class="note"><strong>The prices on this site are not real</strong><p>Prices, price changes, volumes, market capitalizations, index levels, historical charts and the fear and greed gauge on kryptooo are generated by a simulation engine for demonstration. Company and asset names are used only to make the demonstration realistic, and they do not imply any relationship with, or endorsement by, those companies or projects. Do not use this data to trade.</p></div>

<h2>Risk warning</h2>
<ul>
  <li>Investing in stocks and other securities involves risk, including the possible loss of principal.</li>
  <li>Cryptoassets are highly volatile and largely unregulated in many places. Prices can fall sharply and without warning, and you can lose your entire investment.</li>
  <li>Past performance, real or simulated, is not a reliable indicator of future results.</li>
  <li>Diversification does not guarantee a profit or protect against loss.</li>
</ul>

<h2>Accuracy of content</h2>
<p>We work to keep our educational content accurate, but we make no representation that it is complete or free of errors. Laws, regulations and market practices change. Report errors to <a href="mailto:[[CORR_EMAIL]]">[[CORR_EMAIL]]</a>.</p>

<h2>Forward-looking statements</h2>
<p>Any statements about future conditions are opinions and not guarantees. Actual outcomes may differ materially.</p>

<h2>Third parties</h2>
<p>Advertisements and links to third-party sites are provided for convenience. We do not endorse, and are not responsible for, third-party products, services or content.</p>

<h2>Limitation</h2>
<p>To the maximum extent permitted by law, we accept no liability for any loss or damage arising from the use of or reliance on information on this site. See our <a href="/terms-of-service.html">Terms of Service</a>.</p>
"""
},

"cookie-policy": {
 "title": "Cookie Policy",
 "desc": "The cookies and browser storage kryptooo and its advertising partners use, and how to control them.",
 "lede": "This page lists what we store on your device, what our advertising partners may store if you agree, and how to change your choice.",
 "toc": True,
 "updated": True,
 "body": """
<h2>What are cookies?</h2>
<p>Cookies are small text files placed on your device by websites. We also use similar browser technologies, such as local storage. They help sites remember your settings, measure usage and show relevant advertising.</p>

<h2>What we use</h2>
<table>
<thead><tr><th>Name</th><th>Purpose</th><th>Category</th><th>Duration</th></tr></thead>
<tbody>
<tr><td>kryptooo_consent</td><td>Remembers your cookie choice</td><td>Essential</td><td>Until cleared</td></tr>
<tr><td>kryptooo_theme</td><td>Remembers light or dark theme</td><td>Essential (preference)</td><td>Until cleared</td></tr>
<tr><td>Google advertising cookies (for example IDE, NID and related identifiers)</td><td>Serve, limit and measure ads; prevent fraud; personalize ads where permitted</td><td>Advertising</td><td>Set by Google; typically up to 13 months</td></tr>
</tbody></table>
<p>Advertising cookies are set <strong>only if you choose "Accept all"</strong>. Cookie names, purposes and lifetimes for third parties are controlled by them and may change. See <a href="https://policies.google.com/technologies/cookies" rel="noopener" target="_blank">Google's cookie information</a> for current details.</p>

<h2>Managing your choice</h2>
<ul>
  <li>Use "Cookie preferences" in the footer of any page to reopen the banner and change your choice.</li>
  <li>Most browsers let you block or delete cookies in their settings. Blocking essential storage may reset your theme preference.</li>
  <li>Opt out of personalized ads from Google at <a href="https://adssettings.google.com" rel="noopener" target="_blank">adssettings.google.com</a>, or from participating companies at <a href="https://www.aboutads.info/choices" rel="noopener" target="_blank">aboutads.info/choices</a>.</li>
</ul>

<h2>Analytics</h2>
<p>We do not currently use third-party analytics cookies. If that changes, we will update this page and ask for consent where required.</p>

<h2>More information</h2>
<p>See our <a href="/privacy-policy.html">Privacy Policy</a> or write to <a href="mailto:[[PRIVACY_EMAIL]]">[[PRIVACY_EMAIL]]</a>.</p>
"""
},

"editorial-policy": {
 "title": "Editorial Policy",
 "desc": "How kryptooo researches, writes, reviews and corrects its educational content, and how it keeps advertising separate.",
 "lede": "Readers should be able to trust what we publish. This is the standard we hold ourselves to.",
 "toc": True,
 "updated": True,
 "body": """
<h2>Purpose of our content</h2>
<p>Our articles and glossary exist to help readers understand how financial markets work. They explain concepts and mechanisms. They do not tell readers what to buy or sell.</p>

<h2>Accuracy and sourcing</h2>
<ul>
  <li>We rely on primary and authoritative sources where possible, such as exchange rulebooks, index methodology documents, regulator guidance and company filings.</li>
  <li>We avoid stating figures that go stale quickly unless we can date and source them.</li>
  <li>We explain our own calculations, such as how the kryptooo fear and greed gauge is built.</li>
</ul>

<h2>Review process</h2>
<p>Each article is drafted, fact-checked against its sources, and reviewed for clarity and for language that could be mistaken for advice before publication. Pages show a "Last updated" date when they change.</p>

<h2>Corrections</h2>
<p>If we get something wrong, we fix it promptly and note material changes on the page. To report an error, write to <a href="mailto:[[CORR_EMAIL]]">[[CORR_EMAIL]]</a> with the page address and what you believe is incorrect.</p>

<h2>Independence and conflicts of interest</h2>
<ul>
  <li>Advertising and sponsorship never determine what we cover or what we say about an asset or company.</li>
  <li>Ads are always labeled and kept visually separate from editorial content.</li>
  <li>If any person responsible for a page holds a material position in an asset discussed, it will be disclosed.</li>
</ul>

<h2>Market data and simulation</h2>
<p>Market data currently displayed on kryptooo is simulated for demonstration and is labeled as such throughout the site. We will state clearly when and if we switch to licensed real-time or delayed data, and name the provider.</p>

<h2>Use of automation</h2>
<p>We may use software tools for tasks such as data simulation, formatting and spell checking. Editorial responsibility for published articles rests with people, not tools.</p>

<h2>Feedback</h2>
<p>We welcome questions about our standards. Contact us at <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>.</p>
"""
},

"advertising-policy": {
 "title": "Advertising Policy",
 "desc": "How advertising works on kryptooo, how ads are labeled, and how to control or report them.",
 "lede": "Ads help fund free access to our content. Here is how they work and what we do to keep them in their place.",
 "toc": True,
 "updated": True,
 "body": """
<h2>How we are funded</h2>
<p>kryptooo is free to read. We fund it through advertising, which may include ads served by Google AdSense and, in the future, direct sponsorships.</p>

<h2>Our standards</h2>
<ul>
  <li><strong>Clearly labeled.</strong> Every ad is marked "Advertisement" and kept visually separate from editorial content.</li>
  <li><strong>No influence on editorial.</strong> Advertisers cannot pay for coverage, rankings or favorable language. See our <a href="/editorial-policy.html">Editorial Policy</a>.</li>
  <li><strong>Limited placement.</strong> We do not place ads on legal pages, contact forms or error pages, and we avoid layouts that cause accidental clicks.</li>
  <li><strong>No incentives to click.</strong> We never ask or encourage visitors to click ads. Clicking on your own ads is prohibited.</li>
</ul>

<h2>Financial advertising</h2>
<p>Ads for financial products, brokers or cryptoassets are provided by third parties. They are not recommendations by kryptooo. Investing involves risk, and you should do your own research before acting on any ad.</p>

<h2>Your controls</h2>
<ul>
  <li>Use "Cookie preferences" in the footer to accept or decline advertising cookies. If you decline, ad scripts are not loaded.</li>
  <li>Control personalization at <a href="https://adssettings.google.com" rel="noopener" target="_blank">Google Ads Settings</a>.</li>
  <li>Read our <a href="/privacy-policy.html">Privacy Policy</a> and <a href="/cookie-policy.html">Cookie Policy</a>.</li>
</ul>

<h2>Report a problem ad</h2>
<p>If you see an ad that is misleading, offensive or inappropriate, use the "Report ad" control Google provides on the ad if available, and email us at <a href="mailto:[[EMAIL]]">[[EMAIL]]</a> with the page address and a description or screenshot.</p>

<h2>Advertise with us</h2>
<p>For sponsorship enquiries, contact <a href="mailto:[[AD_EMAIL]]">[[AD_EMAIL]]</a>.</p>
"""
},
}
