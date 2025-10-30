import heapq

def min_parking_spots(intervals):
    # Edge case: no cars
    if not intervals:
        return 0

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Min-heap to track end times of current parked cars
    heap = []
    max_spots = 0

    for start, end in intervals:
        # Free spots for cars that have already left
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        # Add current car's end time to heap
        heapq.heappush(heap, end)
        # Update max spots needed
        max_spots = max(max_spots, len(heap))

    return max_spots


# Optional manual tests
if __name__ == "__main__":
    print(min_parking_spots([(0,30),(5,10),(15,20)]))  # 2
    print(min_parking_spots([(7,10),(2,4)]))           # 1
    print(min_parking_spots([(0,10),(10,20),(20,30)])) # 1
    print(min_parking_spots([(1,5),(2,3),(4,6)]))      # 2
