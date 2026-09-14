# Daily workflow

Use this when you want the shared checklist. Each day README already has a summary, key points, diagram, and a runnable starter. This file is the habit layer on top.

## Before the workbook

1. Read the matching DDIA section in your own copy of the book.
2. Skim that day's **Summary / Key points / Diagram**.
3. Run `python3 workbook/starter/main.py`.

While reading DDIA, keep these in the back of your head:

- What state exists?
- What operation changes it?
- What does the mechanism assume?
- What fails, and what does the user see?
- What guarantee do you actually get, and what does it cost?

Jot a one-paragraph mental model **before** you start hacking. Wrong models are useful, correct them after the experiment.

## Production lens

1. When is this technique a good fit?
2. When is it a bad fit?
3. What is the dominant bottleneck?
4. What is the scariest failure mode?
5. What would you measure in production?

## After you finish

You are done for the day when you can:

1. Explain the mechanism without notes
2. Point at something you ran or built
3. Name one variable you changed (or one failure you injected)
4. State a trade-off you would defend in a review

Mark the day in [PROGRESS.md](./PROGRESS.md) only then.
