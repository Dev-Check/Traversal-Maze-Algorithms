from pyamaze import maze,agent,COLOR
import timeit
import random

begin = timeit.default_timer()

#used refrence from pymaze dijskstra demo to help finish converting the algorithm into a maze 
def dijkstra(m,*h,start=None):
    if start is None:
        start=(m.rows,m.cols)

    hurdles=[(i.position,i.cost) for i in h]

    unvisited={n:float('inf') for n in m.grid}
    unvisited[start]=0
    visited={}
    revPath={}
    mypath = []
    while unvisited:
        curr=min(unvisited,key=unvisited.get)
        visited[curr]=unvisited[curr]
       
        if curr==m._goal:
            break
        for i in "NSEW":
            #checking open directions
            if m.maze_map[curr][i] == True:
                if i == "N":
                    child = (curr[0]-1,curr[1])
                    
                elif i == "S":
                    child = (curr[0]+1,curr[1])
                    
                elif i == "E":
                    child = (curr[0],curr[1]+1)
                    
                elif i == "W":
                    child = (curr[0],curr[1]-1)
                    
                if child in visited:
                    continue
                tempDist= unvisited[curr]+1
                for hurdle in hurdles:
                    if hurdle[0]==curr:
                        tempDist+=hurdle[1]

                if tempDist < unvisited[child]:
                    unvisited[child]=tempDist
                    revPath[child]=curr
                    mypath.append(curr)
        unvisited.pop(curr)
    

    return mypath,visited[m._goal]


            
m = maze(20,20)
m.CreateMaze(20,20)
#The only reason there is a times 5 is to get a more of a guarentee that more than 95% of nodes will get a hurdle
# I know this is sloppy coding and i can add this into the while loop but im a little lazy to change that code(I know it works now and dont want the hassle of it not)
i = (m.cols * m.rows) * 5
j = 0
h = agent(m,random.randint(1,20),random.randint(1,20),color=COLOR.yellow)
hurdles = []
#creates around 400 hurdles (there is overlap so there will not be always 400)
while j != i:
    h = agent(m,random.randint(1,20),random.randint(1,20),color=COLOR.yellow)
    hurdles.append(h)
    j += 1
#creates the cost for each hurdle
for cost in hurdles:
    h.cost = random.randint(1,100)
    
path,c=dijkstra(m,h,start=(1,1))
   

   
a=agent(m,1,1,color=COLOR.red,filled=True,footprints=True)
m.tracePath({a:path},delay = 150)

m.run()
end = timeit.default_timer()

