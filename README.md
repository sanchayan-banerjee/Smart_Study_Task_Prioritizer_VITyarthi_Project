## **Smart Study Task Prioritizer**


## **Problem Statement:-**
To develop a AI system that helps students prioritize study tasks based on priority and deadlines. The system uses heuristic scoring, greedy decision making and probabilistic risk estimation to generate an optimized study order thus improving productivity and time management.

## **Objectives:-**
- Develop an intelligent system for task prioritization.
- Apply heuristic-based decision-making to rank tasks.
- Estimate urgency and risks using simple probabilistic reasoning.
- Providing proper reasoning for each decision.
- Maintain a simple and user-friendly command-line interface.

## **Project Overview:-**
This program allows the user to:
- Enter multiple study tasks.
- Assign priority to each task.
- Specify deadlines (in days).
- Automatically compute a score for each task.
- Receive an ordered study plan based on urgency and importance.
- View risk estimations and reasoning for each recommendation.

## **System Workflow:-**
- Step 1: Start the program.
- Step 2: Enter the number of tasks.
- Step 3: Input task details (name, priority, deadline).
- Step 4: System validates inputs.
- Step 5: Compute heuristic scores.
- Step 6: Estimate probability of missing deadlines.
- Step 7: Apply sorting (greedy decision-making).
- Step 8: Display optimized study order with explanations.

## **Project Structure:-**
- **main.py**:Core program logic (AI decision system).
- **README.md**:Documentation and usage instructions.
- **screenshots/**:Contains sample output images (e.g., output1.1.png, output1.2.png).
- **STATEMENT.md**:Contains the Problem Statement.
- **Project_Report**:Contains the complete project report.

## **Requirements:-**
- Python 3.x
- No external libraries required

## **How to Run the Program:-**
- Step 1: Clone the Repository:
  git clone https://github.com/sanchayan-banerjee/Smart_Study_Task_Prioritizer_VITyarthi_Project.git
- Step 2: Navigate to the Project Folder:
  cd Smart_Study_Task_Prioritizer_VITyarthi_Project
- Step 3: Run the Program:
  python main.py

## **Sample Output Screenshots:-**
- [Sample Output Screenshots](screenshots/output1.1.png)
- [Sample Output Screenshots](screenshots/output1.2.png)

## **Decision Logic Explaination:-**
### **Scoring Rule:-**
- Score = priority * (1 / deadline)
- Higher priority signifies greater       importance.
- Smaller deadline signifies higher urgency.
- The final score reflects overall task significance.

### **Risk Evaluation:-**
- The system estimates the likelihood of missing a task.
- Risk = (1 / deadline)
- Tasks with shorter deadlines carry higher risk.
- This helps highlight time-sensitive tasks.

### **Strategy Used:-**
- Tasks are sorted based on computer scores.
- A greedy approach is used here to select the best option.
- The system always selects the highest scoring task first.

## **Core AI Foundations applied in this Project:-**
- **Rational Agent Model**: Makes goal oriented decisions based on inputs.
- **Heuristic Evaluation**: Uses a scoring function to estimate task importance.  
- **Greedy Strategy**: Selects the best option at each step. 
- **Informed Decision Making**: Uses computed values to guide choices. 
- **Probabilistic Thinking**: Estimates risk associated with deadlines. 
- **Basic Statistical Analysis**: Uses averages to understand task distribution.

## **Optional Future Enhancements:-**
Future versions of this project can include:
- Adaptive learning from user behaviour.
- More advanced scoring models.
- Integration with scheduling tools or calenders.
- Machine learning based prioritization.

## **Project By:**
- **Sanchayan Banerjee**
- **GitHub username:sanchayan-banerjee**
