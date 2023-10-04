# Python3 program to find the shortest pairwise
# distance between any two different good nodes.
from heapq import *
 
N = 100005
MAXI = 99999999;
 
# Function to add edges
def add_edge(gr, x, y, weight):
    gr[x].append( (y, weight ));
    gr[y].append((x, weight));
 
# Function to find the shortest
# distance between any pair of
# two different good nodes
def minDistance(gr, n, dist, vis, a, k):
    # Keeps minimum element on top
    q = heapify([])
   
    # To keep required answer
    ans = MAXI;
 
    for i in range(1, n + 1):
        # If it is not good vertex
        if not (a[i]):
            continue;
 
        # Keep all vertices not visited
        # and distance as MAXI
        for j in range(1, n + 1):
            dist[j] = MAXI;
            vis[j] = 0;
 
        # Distance from ith vertex to ith is zero
        dist[i] = 0;
 
        # Make queue empty
        q = []
 
        # Push the ith vertex
        heappush(q,  (0, i ));
 
        # Count the good vertices
        good = 0;
 
        while q:
            # Take the top element
            v = q[0][1]
 
            # Remove it
            heappop(q);
 
            # If it is already visited
            if (vis[v]):
                continue;
            vis[v] = 1;
             
             
            # Count good vertices
            good += a[v];
 
            # If distance from vth vertex
            # is greater than ans
            if (dist[v] > ans):
                break;
 
            # If two good vertices are found
            if (good == 2 and a[v]):
                ans = min(ans, dist[v]);
                break;
 
            # Go to all adjacent vertices
            for j in range(0, len(gr[v])):
                to = gr[v][j][0];
                weight = gr[v][j][1];
 
                # if distance is less
                if (dist[v] + weight < dist[to]):
                    dist[to] = dist[v] + weight;
                    heappush(q, (dist[to], to ));
 
 
    # Return the required answer
    return ans;
 
# Driver code
 
# Number of vertices and edges
n = 5
m = 5;
 
gr = [[] for _ in range(N)];
 
# Function call to add edges
add_edge(gr, 1, 2, 3);
add_edge(gr, 1, 2, 3);
add_edge(gr, 2, 3, 4);
add_edge(gr, 3, 4, 1);
add_edge(gr, 4, 5, 8);
 
# Number of good nodes
k = 3;
 
a = [0 for _ in range(N)];
vis = [None for _ in range(N)];
dist = [None for _ in range(N)];
 
# To keep good vertices
a[1] = 1
a[3] = 1
a[5] = 1;
 
print(minDistance(gr, n, dist, vis, a, k))
