from pyamaze import maze,agent,COLOR
import timeit

begin = timeit.default_timer()


def DFS(m):
    start = (m.rows,m.cols)
    explored = [start]
    frontier =  [start]
    dfs_path = {}
 
    while len(frontier) > 0:
        
        curr = frontier.pop()
    
        #checking to make sure it starts at (1,1)
        if curr == (1,1):
            break
        #NSEW will be order of prefered movement
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
                #checking to see if picked child is in explored list
                if child not in explored:
                    explored.append(child)
                    frontier.append(child)
                    dfs_path[child] = curr
    
    return explored

            
m = maze (20,20)
m.CreateMaze()

#footprints = True lets you see where the agent is traversing
#a = agent(m,footprints=True,shape = "square",color="green")

a = agent(m,20,20,shape="square",goal=(1,1),filled = True, footprints=True,color=COLOR.blue)
#traces with the 
m.tracePath({a:DFS(m)},delay = 150)

m.run()

end = timeit.default_timer()


#run time works correctly when you close the pygame winodw as soo as it finishes, will fix if i think i have time to 
print("runtime = ",end-begin)