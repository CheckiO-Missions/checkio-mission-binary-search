"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 2, 3, 4, 5], 3],
            "answer": [2, 1],
        },
        {
            "input": [[], 2],
            "answer": [-1, 1],
        },
        {
            "input": [[1, 10, 100, 1000], 1000],
            "answer": [3, 3],
        },
    ],
    "Extra": [
        {
            "input": [[1, 2, 3, 4, 5], 6],
            "answer": [-1, 3],
        },
        {
            "input": [[2, 5, 6, 9], 4],
            "answer": [-1, 2],
        },
        {
            "input": [[20, 25, 30, 35, 40, 45, 50, 55, 60], 52],
            "answer": [-1, 3],
        },
        {
            "input": [[0, 1, 2, 3, 4, 5], 0],
            "answer": [0, 2],
        },
        {
            "input": [[11, 13, 17, 19, 23], 12],
            "answer": [-1, 3],
        },
        {
            "input": [[11, 13, 17, 19, 23], 10],
            "answer": [-1, 2],
        },
    ]
}
