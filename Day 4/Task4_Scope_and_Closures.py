def task_status():
    status="pending"

    def updated_status():
        nonlocal status
        print("Updating Task Status...")
        status="Completed"

    print("Intitial status :",status)
    updated_status()
    print("Final Status :",status)

task_status()
