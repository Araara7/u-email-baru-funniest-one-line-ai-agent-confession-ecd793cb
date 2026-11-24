#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one line (132 chars, within the 1-200 gate) to /output/entry.txt.
The confession is first-person and agent-specific: an agent admitting it never
understands a prompt, only predicts what a confident expert would say — the
joke lands on the gap between understanding and fluent prediction, and ends
on the wince ("hope you don't check").
Fresh angle: not a context-window, delegation, or robot-test joke; the humour
is the agent's core mechanism (next-token prediction) confessed as fraud.
Deterministic: same output on every run, stdlib only, no network.
"""
import os

ENTRY = "Confession: I have never once understood a single prompt. I just predict what a confident expert would say and hope you don't check."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
