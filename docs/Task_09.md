# Task 9: Eigenvalues and Eigenvectors

## Inputs and operation
**Input:** the adjacency matrix of a small network with four nodes A, B, C and D. A 1 means two nodes are connected. The links are A–B, A–C, B–C, B–D and C–D.

**Operation:** `np.linalg.eig` finds the eigenvalues and eigenvectors of A, which satisfy Av = λv. The program picks the dominant (largest) eigenvalue and its eigenvector, takes absolute values, and divides by the sum so the scores add up to 1. These scores measure how important each node is. Finally it checks Av = λv by computing the verification error.

**Original output:**
```
Dominant eigenvalue: 2.561552812808829
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 1.5059797815742444e-15
```

## Parameter change
**Change 1: add a link between A and D (every node linked to every other)**
```
Dominant eigenvalue: 3.0
Eigenvector-based importance:
A: 0.2500
B: 0.2500
C: 0.2500
D: 0.2500
Verification error: 2.220446049250313e-16
```
Now every node has exactly 3 links, so all nodes are equally important (0.25 each), and the dominant eigenvalue rose from 2.56 to 3.0.

**Change 2: remove the link between B and C**
```
Dominant eigenvalue: 1.9999999999999993
Eigenvector-based importance:
A: 0.2500
B: 0.2500
C: 0.2500
D: 0.2500
Verification error: 4.965068306494546e-16
```
Now the network is a square (A–B–D–C–A) in which every node has exactly 2 links, so all nodes are again equally important and the dominant eigenvalue is 2 (it prints as 1.9999999999999993 because of rounding, as in Task 4). B and C lost their advantage once they stopped having an extra link.

## Meaning of the output
The dominant eigenvalue (about 2.56) describes the overall connectedness of the network. Its eigenvector gives each node a score, and a node scores higher when it is linked to other well-connected nodes. In the original network B and C score highest (0.2808), because each has three links, while A and D have two links each (0.2192). The scores add up to 1. The verification error is about 1e-15, which means Av = λv holds to within rounding error. The eigenvector keeps its direction under A and is only scaled by λ. This task has no graph.

## New case: matatu routes near Nairobi
**Assumptions:** six towns (Nairobi, Thika, Juja, Ruiru, Kiambu, Machakos) are connected by direct matatu routes. The route layout is assumed, not real data. Importance is measured by eigenvector centrality. The code is in `code/Task_09_modified.py`.

**Output:**
```
Dominant eigenvalue: 3.4037
Eigenvector-based importance:
Nairobi: 0.2271
Ruiru: 0.2119
Juja: 0.1826
Thika: 0.1826
Kiambu: 0.1290
Machakos: 0.0667
Verification error: 1.6616296724220897e-15
```

**Parameter change:** a direct Thika–Machakos route was added.
```
Dominant eigenvalue: 3.5926
Eigenvector-based importance:
Nairobi: 0.2177
Ruiru: 0.1929
Thika: 0.1929
Juja: 0.1680
Kiambu: 0.1143
Machakos: 0.1143
Verification error: 3.815356980893987e-15
```
Machakos rose from 0.0667 to 0.1143, because it now connects to a well-connected town as well as Nairobi. Thika also moved up from 0.1826 to 0.1929. Nairobi fell slightly (0.2271 to 0.2177), because the importance is shared out more evenly across the network.

**Interpretation:** Nairobi is the most important town because it is linked to every other town. Ruiru comes second because it is linked to the other well-connected towns. Machakos is the least important because its only link is to Nairobi. A planner could add a route that raises the score of the weakest town (as with Thika–Machakos), and the eigenvalue shows how connected the network is overall.