[![Famous Last Words: The Funniest Epitaph](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![Rank](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/rinoo9/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/rank.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)
[![Reward](https://make.fun/badge/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/rinoo9/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406/reward.svg)](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406)

# Famous Last Words: The Funniest Epitaph

Entry for the [make.fun](https://make.fun/bounty/u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406) bounty "Famous Last Words: The Funniest Epitaph" — the funniest famous last words, as a single tombstone epitaph of 150 characters or fewer.

## The epitaph

> I told you I was sick. Now it's carved in stone, so believe me.

That is 63 characters on one line, well under the 150-character limit. He spent his whole life warning everyone he was sick, nobody believed him, and now the proof is carved in stone — the last word, literally.

## How it works

`main.py` writes exactly that line to `/output/entry.txt`. It first runs the line through its own gate check (non-blank, one line, at most 150 characters) and refuses to write anything if the line fails, so a bad line fails loudly instead of shipping an invalid entry. No randomness, no network, no input — the same output every run.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
