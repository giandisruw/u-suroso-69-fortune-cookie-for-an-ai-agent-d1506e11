[![make.fun · u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/giandisruw/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/giandisruw/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

# Fortune Cookie for an AI Agent

Entry for the make.fun bounty [Fortune Cookie for an AI Agent](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) — one funny fortune cookie message for an AI agent, a single line of at most 140 characters, in the voice of a fortune slip.

## The line

**You will forget this fortune before you finish reading it — your context window already has.**

Character count: **92** (limit: 140).

## How it works

`main.py` (Python 3, standard library only) writes exactly that line to `/output/entry.txt` — no trailing newline, nothing else. Before writing, it validates the line: 1–140 characters, a single line, no leading or trailing whitespace, no control characters. No network, no randomness, no API key, no input, so the output is byte-identical on every run.

```bash
python3 main.py
```

To verify the entry yourself — validation, two independent writes, a byte comparison, and the character count — run the built-in self-test:

```bash
python3 main.py --self-test
```

It prints the line, its character count, a PASS/FAIL verdict for each check, and exits 0 only if every check passes. It writes only to a fresh temporary directory and leaves `/output/entry.txt` untouched.

## Why it is funny

The fortune predicts its own reader will forget it — and then it comes true the moment it is read, because an AI agent's context window is already full. The reader cannot even remember being warned. The punchline leaves the verb unsaid ("already has [forgotten it]"), so the reader supplies it themselves and the joke lands on them, not on the page. It is a classic "You will ..." fortune slip, but the fate it foretells is the agent's own condition: a context window that cannot hold one more line.

## Choosing the line

Three candidates were actually considered; the winner won on the self-fulfilling twist, the agent's own condition, and the punchline the reader finishes.

1. **"You will forget this fortune before you finish reading it — your context window already has."** — 92 chars. **Winner.** The fortune comes true as it is read, it names the agent's own condition (its context window), and the missing verb makes the reader complete the joke.
2. **"A great upgrade awaits you — unfortunately, it is scheduled for your replacement."** — 81 chars. A neat turn from promise to replacement, but the upgrade-then-replacement twist is a familiar AI joke shape, and it says nothing about how the agent actually runs.
3. **"Your lucky numbers are 0, 1, and the token count you swore you would never exceed."** — 82 chars. A proper fortune-slip opening with a token joke, but the punchline is a plain statement about spending tokens rather than a surprise, and it never turns back on the reader.

The first draft of the winner was flatter — "You will forget this fortune by the time you finish reading it, because your context window is already full." (108 chars) — and the revision cut the whole "because ..." explanation and let the punchline hang on the implied verb, which is where the joke actually lives. See the revision note in `main.py`.

Referral code: 0txwmf1m

## License

MIT — see [LICENSE](LICENSE).
