# Python Basics Algorithms Data-Structures Object Oriented Programming Job Interview Questions

Hello, this repo is a repository I've compiled with basic python exercises, algorithms, data structures, object-oriented programming, questions in job interviews (on data science, machine learning and deep learning), clean code and git usage.  

You can find all the resources I used to create the repo in the reference section. Enjoy it

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Python Basics Algorithms Data-Structures Object Oriented Programming Job Interview Questions](#python-basics-algorithms-data-structures-object-oriented-programming-job-interview-questions)
  - [Folders and Files Tree in this Repo](#folders-and-files-tree-in-this-repo)
    - [Python](#python)
    - [Algorithms](#algorithms)
  - [📝 License](#-license)
  - [👨‍🚀 Show your support](#-show-your-support)
  - [References:](#references)
    - [Clean Code](#clean-code)
    - [Data Structures](#data-structures)
    - [Interview_Questions](#interview_questions)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Folders and Files Tree in this Repo

### Python
📦Python
 ┗ 📜python-exercise.ipynb
 
### Algorithms
📦Algorithms
 ┣ 📂Graphs and Graph Algorithms
 ┃ ┣ 📂breadth-first-search
 ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┗ 📜queue.py
 ┃ ┣ 📂cycle-detection
 ┃ ┃ ┣ 📂cycle-detection-directed-graph
 ┃ ┃ ┃ ┣ 📜Graph directed cycle.png
 ┃ ┃ ┃ ┣ 📜Graph directed no cycle.png
 ┃ ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┃ ┗ 📜main.py
 ┃ ┃ ┣ 📂cycle-detection-undirected-graph
 ┃ ┃ ┃ ┣ 📜Graph undirected.png
 ┃ ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┃ ┗ 📜main.py
 ┃ ┃ ┗ 📜Cycle.md
 ┃ ┣ 📂depth-first-search
 ┃ ┃ ┣ 📂depth-first-search
 ┃ ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┗ 📜stack.py
 ┃ ┃ ┗ 📂depth-first-search-recursive
 ┃ ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┃ ┗ 📜main.py
 ┃ ┣ 📂graphs
 ┃ ┃ ┣ 📂dijkstra
 ┃ ┃ ┃ ┣ 📂matrix-impl
 ┃ ┃ ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┃ ┗ 📜vertex.py
 ┃ ┃ ┃ ┗ 📂priority-queue-impl-adjacency-map
 ┃ ┃ ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┃ ┣ 📜priorityqueue.py
 ┃ ┃ ┃ ┃ ┗ 📜vertex.py
 ┃ ┃ ┣ 📂is-graph-bipartite
 ┃ ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┗ 📜queue.py
 ┃ ┃ ┗ 📂prims-algorithm
 ┃ ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┃ ┣ 📜priorityqueue.py
 ┃ ┃ ┃ ┗ 📜vertex.py
 ┃ ┗ 📂topological-sorting
 ┃ ┃ ┣ 📜graph.py
 ┃ ┃ ┗ 📜main.py
 ┣ 📂Sorting and Searching
 ┃ ┣ 📂hashing
 ┃ ┃ ┣ 📜HashMap.py
 ┃ ┃ ┗ 📜HashMapChaining.py
 ┃ ┣ 📂searching
 ┃ ┃ ┣ 📂binary search
 ┃ ┃ ┃ ┣ 📜iterative.py
 ┃ ┃ ┃ ┣ 📜recursive-no-slicing.py
 ┃ ┃ ┃ ┗ 📜recursive.py
 ┃ ┃ ┣ 📂sequential search
 ┃ ┃ ┃ ┣ 📜ordered-list.py
 ┃ ┃ ┃ ┗ 📜unordered-list.py
 ┃ ┃ ┣ 📜binary-search-iterative.py
 ┃ ┃ ┣ 📜binary-search-recursive-pointers.py
 ┃ ┃ ┣ 📜binary-search-recursive.py
 ┃ ┃ ┣ 📜sequential-search-ordered-list.py
 ┃ ┃ ┗ 📜sequential-search-unordered-list.py
 ┃ ┗ 📂sorting
 ┃ ┃ ┣ 📂bubble sort
 ┃ ┃ ┃ ┣ 📜bubble-sort-recursive.py
 ┃ ┃ ┃ ┣ 📜bubble-sort.py
 ┃ ┃ ┃ ┗ 📜short-bubble.py
 ┃ ┃ ┣ 📂heapsort
 ┃ ┃ ┃ ┣ 📜binaryheap.py
 ┃ ┃ ┃ ┗ 📜main.py
 ┃ ┃ ┣ 📂insertion sort
 ┃ ┃ ┃ ┗ 📜insertion-sort.py
 ┃ ┃ ┣ 📂merge sort
 ┃ ┃ ┃ ┣ 📜merge-sort-return-list.py
 ┃ ┃ ┃ ┗ 📜merge-sort.py
 ┃ ┃ ┣ 📂quicksort
 ┃ ┃ ┃ ┣ 📜quick-sort-return-list.py
 ┃ ┃ ┃ ┗ 📜quicksort.py
 ┃ ┃ ┗ 📂selection sort
 ┃ ┃ ┃ ┗ 📜selection-sort.py
 ┗ 📂Trees and Tree Algorithms
 ┃ ┣ 📂avl tree
 ┃ ┃ ┣ 📜avl.py
 ┃ ┃ ┗ 📜treenode.py
 ┃ ┣ 📂binary heap
 ┃ ┃ ┗ 📜binary-heap.py
 ┃ ┣ 📂bst
 ┃ ┃ ┣ 📜bst.py
 ┃ ┃ ┗ 📜treenode.py
 ┃ ┣ 📂list representation
 ┃ ┃ ┗ 📜tree.py
 ┃ ┣ 📂nodes representation
 ┃ ┃ ┣ 📜exercise.py
 ┃ ┃ ┗ 📜tree.py
 ┃ ┣ 📂parse tree
 ┃ ┃ ┣ 📜main.py
 ┃ ┃ ┣ 📜stack.py
 ┃ ┃ ┗ 📜tree.py
 ┃ ┣ 📂tree
 ┃ ┃ ┗ 📜tree.py
 ┃ ┗ 📂tree traversal
 ┃ ┃ ┣ 📜exercise01-methods.py
 ┃ ┃ ┣ 📜exercise02-functions.py
 ┃ ┃ ┣ 📜exercise03-postorder.py
 ┃ ┃ ┣ 📜exercise04-inorder.py
 ┃ ┃ ┣ 📜preorder-indentation.py
 ┃ ┃ ┣ 📜stack.py
 ┃ ┃ ┗ 📜tree.py

![](.images/python_basic.png)

## 📝 License

This project is licensed under [MIT](https://opensource.org/licenses/MIT) license.

## 👨‍🚀 Show your support

Give a ⭐️ if this project helped you!

## References:
https://www.udemy.com/course/object-oriented-programming-masterclass-with-python-a-z/

### Clean Code
https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29
https://gist.github.com/leeweiminsg/b31495b05136a29ceff86f5c4967a697
https://gist.github.com/scottashipp/88b3a4d97eaa542842bcf5b08f5bac6d
https://gist.github.com/vaibhavpaliwal/508f4e67f7fd36209f2d92455b39de85
https://gist.github.com/jonnyjava/4f615567f0b55d361654
https://gist.github.com/zhehaowang/b6c9517dc690054670c8638f18a68a42
https://www.youtube.com/playlist?list=PLxw2ybf4zPJ5TncW4_IWqFSGGybTaXs5I

### Data Structures
https://www.udemy.com/course/algorithms-data-structures-and-real-life-python-problems/
https://github.com/Hemant-Jain-Author/Problem-Solving-in-Data-Structures-Algorithms-using-Python
https://github.com/ivanmmarkovic/Problem-Solving-with-Algorithms-and-Data-Structures-using-Python
https://github.com/OmkarPathak/Data-Structures-using-Python/tree/master/Arrays

### Interview_Questions
https://github.com/JifuZhao/120-DS-Interview-Questions/blob/master/DataScience_Interview_Questions.pdf
https://gist.github.com/felipemoraes/c423d1447ee13585e2270b27f174fb13
https://github.com/rbhatia46/Data-Science-Interview-Resources
https://github.com/conordewey3/DS-Career-Resources/blob/master/Interview-Resources.md
https://github.com/khanhnamle1994/cracking-the-data-science-interview/blob/master/DataScience%20Interview%20Questions.pdf
https://github.com/khanhnamle1994/cracking-the-data-science-interview
https://github.com/zhiqiangzhongddu/Data-Science-Interview-Questions-and-Answers-General-
https://www.interviewbit.com/python-interview-questions/
https://www.techbeamers.com/python-interview-questions-programmers/
https://www.youtube.com/watch?v=HGXlFG_Rz4E&ab_channel=edureka%21
