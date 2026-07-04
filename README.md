# WORKEFFI (Task Manager and Optimizer)

# Problematic

The application seeks to resolve the lack of organization on a daily basis. Often, even if previous tasks are scheduled, new unforeseen pending tasks arise. With little time available, it is common for users to get blocked and not know where to start.

# Objective

The main objective of WORKEFFI is to optimize the user's available time for all the tasks they must complete in their day. The system helps determine if the time available is enough to complete all the tasks. In case time is not enough, the application intelligently suggests which tasks to postpone (smart sacrifice), ensuring that those of high importance are always maintained and prioritized.

# How does the code work?

The program uses structured logic based on the following fundamental programming elements:

Variables: Used to store temporary data entered by the user, such as their available time, task name, time unit, and calculated priority scores.

Dictionaries: They are essential to structure information. Each individual task is saved as a dictionary containing its specific attributes: "name", "time", "level", and its "state" (active or postponed). An additional dictionary maps text priority levels ("high", "medium", "low") to numerical values for easy sorting.

Loops: A main "while" loop is used that allows the user to continue adding multiple tasks one after another until they decide to stop. "For" cycles are used to iterate over the list of tasks when sorting them (bubble algorithm) and to calculate the total time needed by adding the time of each item in the list.

# AI usage statement

Artificial Intelligence (Gemini) tools were used for the development and documentation of this project:

    Writing and Structure
    Diagram Generation