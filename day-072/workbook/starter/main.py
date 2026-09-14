#!/usr/bin/env python3
"""Day 072: Wall vs monotonic vs Lamport ordering."""
import argparse

class Lamport:
def __init__(self):
self.t = 0

def tick(self) -> int:
self.t += 1
return self.t

def on_message(self, remote: int) -> int:
self.t = max(self.t, remote) + 1
return self.t

def main():
p = argparse.ArgumentParser()
p.add_argument("--ntp-step-back-ms", type=float, default=0)
args = p.parse_args()
wall = 1000.0
mono = 0.0
events = []
for i in range(3):
mono += 100
wall += 100
events.append(("local", i, wall, mono))
wall -= args.ntp_step_back_ms
events.append(("after ntp step", 3, wall, mono + 100))
lc = Lamport()
stamps = []
for name, _, w, m in events:
stamps.append((name, w, m, lc.tick()))
mis = sum(1 for i in range(len(stamps) - 1) if stamps[i][1] > stamps[i + 1][1])
print("event wall mono lamport")
for row in stamps:
print(f" {row[0]}: wall={row[1]:.0f} mono={row[2]:.0f} L={row[3]}")
print(f"wall-clock mis-order pairs after step-back: {mis}")

if __name__ == "__main__":
main()
