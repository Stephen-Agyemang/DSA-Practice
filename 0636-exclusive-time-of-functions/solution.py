class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        stack = []
        exclusive_times = [0] * n
        previous_time = 0

        for log in logs:
            parts = log.split(":")
            func_id = int(parts[0])
            status = parts[1]
            timestamp = int(parts[2])

            if status == "start":
                if stack:
                    exclusive_times[stack[-1]] += timestamp - prev_time 
                stack.append(func_id)
                prev_time = timestamp

            else: 
                popped_id = stack.pop()
                exclusive_times[popped_id] += timestamp - prev_time + 1
                prev_time = timestamp + 1 

        return exclusive_times    


