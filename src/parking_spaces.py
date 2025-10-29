"""
HW02 — Parking Spaces: Minimum Spots Needed

Implement min_parking_spots(intervals) -> int

Behavior:
- Given a list of (start, end) times, return the minimum number of parking spots
  so that no car waits. If a car leaves at time t and another arrives at time t,
  the same spot can be reused.
"""

def min_parking_spots(intervals):
    # TODO Steps:
    # 1) Understand: we need peak overlap count.
    # 2) Re-phrase: track earliest end; reuse when end <= start.
    # 3) Identify: inputs list of pairs; output int; vars heap, rooms.
    # 4) Break down: sort by start; pop ends <= start; push end; track max size.
    # 5) Pseudocode above; implement with heapq.
    # 6) Write code.
    # 7) Debug with small examples.
    # 8) Confirm O(n log n).
    raise NotImplementedError
