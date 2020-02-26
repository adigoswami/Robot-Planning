import numpy as np
import copy
import time
import os

initial_node = np.array( [[1, 3, 0],
                         [5, 2, 6],
                         [4, 7, 8]])
solvable = initial_node.flatten().copy()
print(initial_node)
print(solvable)

def is_Node_Solvable(solvable):
    inv=0
    
    for i in range(len(solvable)-2):
        for j in range(i+1,len(solvable)-1):
            if solvable[i]<solvable[j]:
                inv +=1
    if inv % 2 == 0:
        print("The matrix is solvable.")
    else:
        print("The matrix is not solvable.")
is_Node_Solvable(solvable)

#%%
def Get_User_Input():
    print("Enter the values of input node in the range [0-8] without repetition :\n")
    flag = False
    final_input = np.zeros(9)
    while flag is False:
        for i in range (9):
            input_val = (input("Enter number " + str(i+1) +" : "))
            if len(input_val) is 0:
                print("You need to enter a value in range [0-8]. Don't leave a number blank!!!")
                flag = False
                break
            if int(input_val)<0 or int(input_val)>8:
                flag = False
                print("Entered input is out of bounds. Please enter a valid input!!")
                break
            else:
                flag =True
                final_input[i] = int(np.array((input_val)))

    return final_input
#%%
inp = False
while inp is False:
    initial_node = Get_User_Input().astype(int)
    initial_node_mat = initial_node.copy()
    inp = is_Node_Solvable(initial_node)

Goal_Node = 123456780
Goal_Node_Mat= np.array([[1,2,3],[4,5,6],[7,8,0]])
Queue = []
Parent_Node = []
Child_Node = []
Parent_dict = {}
Child_dict = {}
temp_child_list=[]
FinalNodeList =[]
node_info = []
visited_node_list = []
goal_id = False
#%%
def Convert_int_to_num(a,b,c,d,e,f,g,h,i):
    number= a*100000000+b*10000000+c*1000000+d*100000+e*10000+f*1000+g*100+h*10+i
    return  number
#%%
num_initial = Convert_int_to_num(initial_node[0][0],initial_node[0][1],initial_node[0][2],initial_node[1][0],initial_node[1][1],initial_node[1][2],initial_node[2][0],initial_node[2][1],initial_node[2][2])
visited_node_list.append(num_initial)

#%%
def Blank_Tile_Loc(solvable):
    for i in solvable:
        if solvable[i]==0:
            break
    return i

#%%
def goal_reached(node):
    num = Convert_int_to_num(node[0],node[1],node[2],node[3],node[4],node[5],node[6],node[7],node[8])
    if num == Goal_Node:
        print("Goal reached.")
    else:
        return False
    return True
#%%
def Visited_or_not(node):    
    for i in visited_node_list[::-1]:
        if np.array_equal(node,i):
            #print("################################################################")
            return True

    return False
#%%

def move_left(solvable, Queue, iter):
    goal_id = False
    #visited_node.update(solvable)
    current_node = copy.deepcopy(solvable)
    i = Blank_Tile_Loc(solvable)

    if i==0 or i==3 or i==6:
        return  goal_id, temp_child_list
    else:
        print("Moving left")
        current_node[i],current_node[i-1]=current_node[i-1],current_node[i]
        print("current node ::::::",current_node)
    
        if Visited_or_not(current_node) == False:
            #check if goal reached
            if goal_reached(current_node) == True:
                goal_id = True
            
            visited_node_list.append(current_node)
            Queue.append(current_node)
            #Child_dict
            temp_child_list.append(current_node)
        
    return goal_id, temp_child_list

#%%
def move_right(solvable, Queue, iter):
    goal_id =False
    #visited_node.update(solvable)
    current_node = copy.deepcopy(solvable)
    i = Blank_Tile_Loc(solvable)

    if i==2 or i==5 or i==8:
        goal_id = False
        return  goal_id, temp_child_list
    else:
        #print("Moving right")
        current_node[i],current_node[i+1]=current_node[i+1],current_node[i]
        #print("current node ::::::",current_node)

    
        if Visited_or_not(current_node) == False:
            #check if goal reached
            if goal_reached(current_node) == True:
                goal_id = True
            
            visited_node_list.append(current_node)
            Queue.append(current_node)
            #Child_dict
            temp_child_list.append(current_node)
      
    return  goal_id, temp_child_list

#%%
def move_up(solvable, Queue, iter):
    #visited_node.update(solvable)
    goal_id = False
    current_node = copy.deepcopy(solvable)
    i = Blank_Tile_Loc(solvable)

    if i==0 or i==1 or i==2:
        return  goal_id, temp_child_list
    else:
        #print("Moving  up")
        #print("node bfr swap", current_node)
        current_node[i],current_node[i-3]=current_node[i-3],current_node[i]
        #print("current node ::::::",current_node)

        if Visited_or_not(current_node) == False:
            #check if goal reached
            if goal_reached(current_node) == True:
                goal_id = True
            
            visited_node_list.append(current_node)
            Queue.append(current_node)
            #Child_dict
            temp_child_list.append(current_node)

    return  goal_id, temp_child_list

#%%
def move_down(solvable, Queue, iter):
    #visited_node.update(solvable)
    goal_id = False
    current_node = copy.deepcopy(solvable)
    i = Blank_Tile_Loc(solvable)

    if i==6 or i==7 or i==8:
        return goal_id, temp_child_list
    else:
        #print("Moving Down")
        current_node[i],current_node[i+3]=current_node[i+3],current_node[i]
        #print("current node ::::::",current_node)
    
        if Visited_or_not(current_node) == False:
            #check if goal reached
            if goal_reached(current_node) == True:
                goal_id = True

            
            visited_node_list.append(current_node)
            Queue.append(current_node)
            #Child_dict
            temp_child_list.append(current_node)
    
    return  goal_id, temp_child_list

#%%
# Update Node
def update_current_node(Queue,iter):
    #print("Update Current node")
    #print("Q",Queue)
    val = Queue.pop(0)
    Parent_dict.update({iter:val})
    Parent_Node.append(val)
    current_node = val.copy()
    return current_node,Queue

#%%
#Main()
print("Start Node", initial_node)
updated_current_node = solvable.copy()

iter_parent = 1
iter_child = 1
goal_id = False
Queue.append(solvable)
while Queue:
    temp_child_list=[]
    
    updated_current_node,Queue = update_current_node(Queue,iter_parent)
    print("Updated Current Node: ", updated_current_node)


    goal_id, temp_child_list = move_down(updated_current_node,Queue,iter_parent)
    # print("Current Node: ", Updated_Current_Node)
    # print("Queue", Queue)
    if goal_id == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break

    goal_id, temp_child_list = move_up(updated_current_node, Queue,iter_parent)
    print("Current Node: ", updated_current_node)
    # print("Queue", Queue)
    if goal_id == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break

    goal_id, temp_child_list = move_left(updated_current_node, Queue,iter_parent)
    # print("Current Node: ", Updated_Current_Node)
    # print("Queue",Queue)
    if goal_id == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break

    goal_id, temp_child_list = move_right(updated_current_node,Queue,iter_parent)
    # print("Current Node: ", Updated_Current_Node)
    # print("Queue", Queue)
    if goal_id == True:
        test_child_dict.update({iter_parent: temp_child_list})
        break
    test_child_dict.update({iter_parent:temp_child_list})
    iter_parent = iter_parent +1
    print('Level:',level)
    print('Total Parent iteration: ', iter_parent)
    # if iter_parent >=10000:
    #     break
#print('Child Node :', Child_Node)
#print('Test Child List :', test_child_dict)
#print('Parent Node:', Parent_Node)
#print('parent dict:',Parent_dict)
#print('child dict:',Child_dict)
#print("Queue: ", Queue)
#%%def Generate_Text_Files(FinalNodeList, test_child_dict, ):

    if os.path.exists("nodePath.txt"):
        os.remove("nodePath.txt")
    f = open("nodePath.txt", "a")
    for i in FinalNodeList:
        i = np.array(i).reshape((3, 3))
        for j in range(len(i.flatten())):

            x = (np.transpose(i).flatten())
            f.write(str((x[j])) + " ")
        f.write("\n")
    f.close()

    if os.path.exists("Nodes.txt"):
        os.remove("Nodes.txt")
    f = open("Nodes.txt", "a")

    for i in range(len(temp_child_dict)):

        for val in temp_child_dict.get(i):

            val = np.array(val).reshape(3, 3)
            for j in range(len(val.flatten())):

                x = (np.transpose(val)).flatten().astype(int)
                f.write(str(int(x[j])) + " ")
            f.write("\n")
    f.close()

    if os.path.exists("NodesInfo.txt"):
        os.remove("NodesInfo.txt")
    f = open("NodesInfo.txt", "a")
    count = 0
    for val in temp_child_dict.keys():
        f.write(str(val ) + " " + str(node_info[count]) + " " + str(0))
        count = count + 1
        f.write("\n")
    f.close()
    return None

#%%
def Back_Tracking(Parent_dict,temp_child_dict,FinalValue,InitialValue):
    updated_val= FinalValue
    while updated_val is not InitialValue :
        val_found = False
        for key,val in test_child_dict.items():

            for v in val:
                if np.array_equal(updated_val,v):
                    parent_key= key

                    updated_val = Parent_dict[parent_key]

                    FinalNodeList.append(updated_val)
                    val_found= True
                    break
            if val_found is True:
                break


        if np.array_equal(updated_val,initial_node_matrix):

            break
#%%
print("BackTracking:")
Back_Tracking(Parent_dict,temp_child_dict,Goal_Node_Mat,initial_node_mat)

FinalNodeList.reverse()
FinalNodeList.append(Goal_Node_Mat)


print("No of Steps :",len(FinalNodeList))

Generate_Text_Files(FinalNodeList,temp_child_dict)
end_time = time.time()
total_time =  end_time -start_time

print('Total Time:',total_time)