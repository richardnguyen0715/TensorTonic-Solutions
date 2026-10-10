def schedule_pipeline(tasks: list, resource_budget: int) -> list:
    import heapq

    task_map = {task["name"]: task for task in tasks}
    completed = set()
    scheduled = []
    running = []  # (end_time, task_name, resource_requirement)
    current_time = 0
    used_resources = 0

    while len(completed) < len(tasks):
        # Complete all running tasks whose end time has been reached.
        while running and running[0][0] <= current_time:
            end_time, name, resources = heapq.heappop(running)
            completed.add(name)
            used_resources -= resources

        # Find tasks whose dependencies are complete.
        eligible = sorted(
            name
            for name, task in task_map.items()
            if name not in completed
            and all(
                dep in completed
                for dep in task["depends_on"]
            )
            and name not in {entry[1] for entry in running}
            and name not in {
                item["task_name"] for item in scheduled
            }
        )

        # Greedily start eligible tasks in alphabetical order.
        started_any = False

        for name in eligible:
            task = task_map[name]
            resources = task["resources"]

            if used_resources + resources <= resource_budget:
                duration = task["duration"]
                heapq.heappush(
                    running,
                    (current_time + duration, name, resources)
                )
                used_resources += resources
                scheduled.append({
                    "task_name": name,
                    "start_time": current_time
                })
                started_any = True

        # If no tasks are running, remaining tasks cannot proceed.
        if not running:
            break

        # Advance to the next task completion event.
        current_time = running[0][0]

    return sorted(
        scheduled,
        key=lambda item: (item["start_time"], item["task_name"])
    )