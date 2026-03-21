# **Project Report On Smart Study Task Prioritizer**

## **Introduction:-**
In modern academic environments, students frequently face difficulty in deciding which tasks to prioritize when multiple assignments, subjects and deadlines overlap. Poor prioritization can lead to inefficiency, missed deadlines and reduced productivity.This project aims to assist users in organizing their tasks by evaluating their importance and urgency. The system applies Artificial Intelligence concepts to generate an optimized task execution order.

## **Problem Statement:-** 
To develop an AI system that helps students prioritize study tasks based on priority and deadlines. The system uses heuristic scoring, greedy decision making and probabilistic risk estimation to generate an optimized study order thus improving productivity and time management.

## **Problem Statement Inspiration:-**
- Students often lack a structured approach while prioritizing their tasks. 
- Manual decision-making may lead to inefficient time usage. 
- Urgent tasks may be ignored in favor of less important ones.  
- A simple intelligent agent can significantly improve productivity. 
 
## **Project Objectives:-**
- Develop a system that accepts multiple tasks as input.  
- Evaluate tasks based on importance and urgency.  
- Generating an optimized study order based on proper reasoning behind each decision.    
- Incorporating concepts of heuristics and rational agents in order to recommend the best prioritized order to do the   tasks.
- Maintain a simple and user friendly command line interface. 

## **Tools and Technologies Used:-**
| Category | Selection |
|----------|----------|
| Programming Language | Python 3 |
| Libraries Used | None (standard Python only) |
| IDE | Visual Studio Code |
| Operating System | Windows |
| Version Control | Git + GitHub |

## **Approach and Methodology:-**
The system follows a structured approach:
- User inputs task details (name, priority, deadline).  
- Input validation ensures correctness.
- A heuristic scoring function evaluates each task.  
- Probability is used to estimate risk of missing deadlines.  
- Tasks are sorted using a greedy decision-making strategy.  
- The final output is presented with explanation.
  
## **System Flow:-**
- Step 1: Start the program. 
- Step 2: Input number of tasks.  
- Step 3: Enter task details.
- Step 4: Validate inputs.  
- Step 5: Compute heuristic scores.  
- Step 6: Estimate risk values.  
- Step 7: Sort tasks based on score.  
- Step 8: Display recommended study order.
  
## **Implementation Details are as follows**

### **Core Components:-**
- Input handling system.  
- Task validation logic.  
- Heuristic scoring function.  
- Risk estimation function.  
- Sorting mechanism (greedy approach).  
- Output formatting module.

### **Decision Logic:**

#### Heuristic Function:-
- score = priority × (1 / deadline)
- Higher priority increases importances.
- Lower deadline increases urgency.

#### Risk Estimation:-
- Risk = 1 / deadline
- Smaller deadlines imply higher risk.

### **Decision Strategy:-**
- Tasks are sorted based on score.
- Highest scoring task is selected first.
- This follows a greedy approach.

### **Project Structure:-**
- **main.py**: Core program logic (AI decision system).
- **README.md**: Documentation and usage instructions.
- **screenshots/**: Contains sample output images (e.g., output1.1.png, output1.2.png).
- **Problem_Statement.md**: Contains the Problem Statement.
- **Project_Report**: Contains the complete project report.

## **Results and Observations**

### **Expected Behaviour:-**
- Tasks with high priority and low deadlines are ranked first.
- Tasks with low urgency appear later.
- The system provides consistent and logical ordering.

### **Observations:-**
- The scoring function effictively balances urgency and importance.
- Risk estimation highlights critical tasks.
- Output reasoning improves interpretability.

## **Analysis:-**
| Parameter | Impact of Parameter |
|----------|----------|
| Priority | Determines importance of task |
| Deadline | Determines urgency |
| Score | Final ranking factor |
| Risk | Indicates likelihood of delay |

## **Inference:-**
- Combining both urgency and importance leads to better decision making.
- Simple heuristics can effectively solve real world problems.
- Even basic AI techniques can improve productivity.

## **Key Decisions Included are as follows:-**
- Chose a heuristic approach for simiplicity and efficiency.
- Used greedy sorting instead of complex search algorithm.
- Avoided external libraries to maintain portability.
- Included reasoning output for explainability.

## **Challenges faced while making this project:-**
- Designing an effective scoring function.
- Balancing simplicity with AI concepts.
- Handling invalid user inputs.
- Ensuring clean and readable output.
- Mapping theoritical AI concepts to practical implementation.

## **Core AI Foundations applied in this Project:-**
- **Rational Agent Model**: Makes goal oriented decisions based on inputs.
- **Heuristic Evaluation**: Uses a scoring function to estimate task importance.  
- **Greedy Strategy**: Selects the best option at each step. 
- **Informed Decision Making**: Uses computed values to guide choices. 
- **Probabilistic Thinking**: Estimates risk associated with deadlines. 
- **Basic Statistical Analysis**: Uses averages to understand task distribution.

## **Learning Outcomes:-**
- Understanding of rational agent models.
- Application of heuristic based decision making.
- Implentation of greedy algorithms.
- Use of probability for risk estimation.
- Importance of clean CLI design.
- Experience with structured problem solving.

## **The possible future enhancements in this project:-**
- Adaptive learning based on user behaviour.
- Dynamic adjustment of priorities.
- Integration with calenders and planners
- Advanced machine learning models can be incorporated.

## **CONCLUSION:-**
The Smart Study Task Priortizer successfully demonstrates how AI concepts can be applied to solve real-world problems.The system provides an efficient and practical approach to task management using heuristic evaluation, greedy decision making and probablistic reasoning.Despite its simplicity , the project effectively improves task prioritization and showcases the relevance of AI techniques in everyday scenarios.

## **References**
### For furthur references check out the following:-
- Python Official Documentation
- Concepts from Artificial Intelligence Coursework.
- Basic principles of heuristic search and decision making.