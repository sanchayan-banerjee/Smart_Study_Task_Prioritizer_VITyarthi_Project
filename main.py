#Heuristic Scoring Function
def calculate_score(task):
    priority = task["priority"]
    deadline = task["deadline"]

    urgency = 1 / deadline
    score = priority * urgency

    return score

#Probablity of missing deadline
def probablity_of_missing(deadline):
    return min(1, 1 / deadline)

#Reasoning behind the descision
def generate_reason(task):
    if task["priority"] >= 4 and task["deadline"] <= 3:
        return "High priority and urgent"
    elif task["priority"] >= 3:
        return "Moderate priority and moderate urgency"
    else:
        return "Lower priority and less urgent"

#Use of statistics to support our descision
def average_priority(tasks):
    return sum(t["priority"] for t in tasks) / len(tasks)

def average_deadline(tasks):
    return sum(t["deadline"] for t in tasks) / len(tasks)

#Programming the Task Analyzer
def main():
    print("-----SMART STUDY TASK PRIORITIZER-----")
    print("AI-based prioritization using Heuristic Scoring\n")


    try:
        n = int(input("Enter the number of tasks: "))
    except:
        print("INVALID INPUT.")
        return
    
    tasks = []
    
    for i in range(n):
        print(f"\nTask {i+1}:")

        name = input("Name: ")


        try:
            priority = int(input("Priority (1-5): "))
            deadline = int(input("Deadline (days): "))
        except:
            print("INVALID INPUT.Skipping task.")
            continue

        #Validation of Tasks
        priority = max(1, min(priority,5))
        deadline = max(1, deadline)

        tasks.append({
            "name": name,
            "priority": priority,
            "deadline": deadline
        })
    
    if not tasks:
        print("NO VALID TASKS ENTERED.")
        return
    
    print("\nCalculating optimal study plan...\n")

    #Application of Statistics
    avg_p = average_priority(tasks)
    avg_d = average_deadline(tasks)

    print("------Study Statistics------")
    print(f"Average Priority: {avg_p:.2f}")
    print(f"Average Deadline: {avg_d:.2f}")

    #Sorting by Heuristic Function(INFORMED SEARCH and GREEDY)
    tasks.sort(key=calculate_score, reverse=True)

    #Output
    print("----RECOMMENDED STUDY ORDER-----\n")

    for i, task in enumerate(tasks, 1):
        score = calculate_score(task)
        risk = probablity_of_missing(task["deadline"])
        reason = generate_reason(task)


        print(f"{i}. {task['name']}")
        print(f"   Score: {score:.2f}")
        print(f"   Risk of Missing Deadline: {risk:.2f}")
        print(f"   Reason: {reason}\n")


main()



    


     