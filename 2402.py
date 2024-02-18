class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()  # sort by starting time of meetings

        roomsUsedCount = [0] * n  # Each room is used 0 times in the beginning
        lastAvailableAt = [0] * n  # Each room will be last available at

        for meet in meetings:
            start = meet[0]
            end = meet[1]
            found = False

            EarlyEndRoomTime = float('inf')
            EarlyEndRoom = 0

            # Find the first available meeting room
            for room in range(n):
                if lastAvailableAt[room] <= start:
                    found = True
                    lastAvailableAt[room] = end
                    roomsUsedCount[room] += 1
                    break

                if lastAvailableAt[room] < EarlyEndRoomTime:
                    EarlyEndRoom = room
                    EarlyEndRoomTime = lastAvailableAt[room]

            if not found:
                lastAvailableAt[EarlyEndRoom] += (end - start)
                roomsUsedCount[EarlyEndRoom] += 1

        resultRoom = -1
        maxUse = 0
        for room in range(n):
            if roomsUsedCount[room] > maxUse:
                maxUse = roomsUsedCount[room]
                resultRoom = room

        return resultRoom
