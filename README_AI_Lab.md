# CMC381-L Artificial Intelligence Lab

Lab material for **CMC381-L Artificial Intelligence Lab** (BS Computer Science, Fall 2026) at the Department of Computer Science, FEST, **Iqra University Islamabad**.

In this lab, students implement the core algorithms of Artificial Intelligence in **Python**:

- intelligent agents
- search: uninformed, informed, local and adversarial
- fuzzy logic
- machine learning
- neural networks

| | |
|---|---|
| **Instructor** | Faiza Ali, Junior Lecturer |
| **Email** | faiza.ali@iqraisb.edu.pk |
| **Office** | A8 |
| **Credit hours** | 3+1 (one 3-hour lab per week) |
| **Prerequisite** | CMC371 |
| **Language / tools** | Python 3.10+, Anaconda (Jupyter Notebook) or Google Colab |

---

## Repository structure

```
AI-Lab-CMC381L/
├── README.md
├── requirements.txt
├── docs/
│   ├── Course_Card_CMC381L_Artificial_Intelligence_Lab.pdf
│   └── AI_Lab_Manual_CMC381L.pdf
└── code/
    ├── lab01.py
    ├── lab02.py
    └── ...
```

Each file in `code/` is the worked example of one lab in the manual. Labs with two parts have two files, for example `lab06a.py` (Hill Climbing) and `lab06b.py` (Genetic Algorithm).

---

## Lab sessions

| Week | Lab | Topic | Programs |
|:---:|:---:|---|---|
| 1 | 1 | Introduction to AI, Intelligent Agents and Environments | `lab01.py` – reflex vacuum-cleaner agent |
| 2 | 2 | Problem Formulation and the 8-Puzzle Problem | `lab02.py` – 8-puzzle with node-expansion counters |
| 3 | 3 | Uninformed Search: BFS, DFS and Uniform Cost Search | `lab03.py` – maze (BFS vs DFS) and UCS road map |
| 4 | 4 | Depth-Limited and Iterative Deepening Search | `lab04.py` – DLS, IDDFS and tree visualisation |
| 5 | 5 | Informed Search: Greedy Best-First and A* | `lab05.py` – 8-puzzle with Manhattan distance |
| 6 | 6 | Local Search: Hill Climbing and Genetic Algorithm | `lab06a.py` – 8-queens, `lab06b.py` – GA optimisation |
| 7 | – | **Open-Ended Lab / Project assigned** | – |
| 8 | – | **Midterm Exam** | – |
| 9 | 7 | Adversarial Search: Minimax and Alpha-Beta Pruning | `lab07.py` – unbeatable Tic-Tac-Toe |
| 10 | 8 | Fuzzy Sets and Fuzzy Set Operations | `lab08.py` – union, intersection, complement |
| 11 | 9 | Fuzzy Logic Based Expert System (AC control) | `lab09.py` – Mamdani inference from scratch |
| 12 | 10 | Naive Bayes and K-Means | `lab10a.py` – spam filter, `lab10b.py` – Iris clustering |
| 13 | 11 | Artificial Neural Networks: The Perceptron | `lab11.py` – AND gate, XOR limitation |
| 14 | 12 | Multi-Layer Perceptron and Backpropagation | `lab12a.py` – XOR from scratch, `lab12b.py` – MNIST (PyTorch) |
| 15–16 | – | **Open-Ended Lab / Project assessment** | – |
| 17 | – | **Final Exam** | – |

---

## Getting started

### Option A – Anaconda (lab computers)

```bash
conda create -n ailab python=3.11 -y
conda activate ailab
pip install -r requirements.txt
```

Run any lab from the repository folder:

```bash
python code/lab05.py
```

### Option B – Google Colab

Open <https://colab.research.google.com>, create a notebook, and paste the code of a lab into a cell. Colab already has all the required libraries. Use **Runtime → Change runtime type → GPU** for Lab 12 if training is slow.

### requirements.txt

```
numpy
matplotlib
networkx
scikit-learn
torch         # Lab 12 only
torchvision   # Lab 12 only
```

### Example output

```
$ python code/lab05.py
Start h(n) = 10
Algorithm   Solution length   Nodes expanded
greedy                   36              181
astar                    14               76
```

On the same 8-puzzle, breadth-first search needs about 5,960 expansions to find the 14-move solution. A* finds it with only 76.

---

## Course Learning Outcomes

| CLO | Statement | BT Level | GA | Weight |
|:---:|---|:---:|:---:|:---:|
| CLO1 | **Apply** fundamental concepts of Artificial Intelligence, including rational agents, search algorithms, and fuzzy logic, to solve real-world problems. | C3 | GA2 | 60% |
| CLO2 | Leverage modern AI tools and frameworks to **design** and implement basic algorithms, including search strategies and machine learning models. | P2 | GA5 | 40% |

## Assessment

| Component | Weight |
|---|:---:|
| Lab tasks (graded on rubrics R1–R5) | 25% |
| Midterm Exam | 15% |
| Open-Ended Lab / Project | 20% |
| Final Exam | 40% |

**Open-Ended Lab:** *Smart Campus Delivery Robot.* Groups of 2–3 students:

- model a campus as a grid map
- plan delivery routes with BFS, UCS and A*, using their own admissible heuristics
- order several deliveries with local search or a genetic algorithm
- add one extension: a fuzzy speed controller, an ML-based congestion predictor, or dynamic re-planning

---

## For students

- Read the theory and example code of a lab **before** the session.
- Save your work as `LabXX_RegNo.ipynb` (or `.py`) and upload it to the LMS before the deadline.
- Write clean, commented code with meaningful names.
- **Academic integrity:** You may study these examples, but lab tasks must be your own work. Copied code, whether from classmates, the internet or AI tools, receives zero marks.

## Notes

- All example programs (Labs 1–12) were run before publication, and their outputs appear in the manual.
- One part was not run: the MNIST part of Lab 12 (`lab12b.py`). It downloads the dataset on first run, and its results vary from run to run. It typically reaches about 97–98% test accuracy after 5 epochs.
- Execution times printed by `lab02.py` depend on your computer.

## References

1. S. Russell and P. Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed., Pearson, 2021.
2. T. J. Ross, *Fuzzy Logic with Engineering Applications*, 4th ed., Wiley, 2016.
3. T. M. Mitchell, *Machine Learning*, McGraw-Hill.
4. I. Goodfellow, Y. Bengio and A. Courville, *Deep Learning*, MIT Press, 2016.
5. scikit-learn User Guide – <https://scikit-learn.org/stable/user_guide.html>
6. PyTorch Tutorials – <https://pytorch.org/tutorials/>

---

© 2026 Faiza Ali, Department of Computer Science, Iqra University Islamabad. For educational use.
