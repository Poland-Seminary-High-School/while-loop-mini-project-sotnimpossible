prompt='add some Tasks to your to-do list\n'
prompt += 'type done when youre done\n'
tasks=[]
while True:
    task=input(prompt)
    if task.lower()=='done':
        break
    else:
        tasks.append(task)
        print('added',task,'to your to-do list')
print('your to-do list has',tasks,'on it.')
prompt='do you wanna Change the list (add/remove/done)\n'
while True:
    task=input(prompt)
    if task.lower()=='done':
        break
    elif task.lower()=='add':
        tasks.append(input('what do you wanna add\n'))
        print('added to list')
    elif task.lower()=='remove':
        tasks.remove(input('what do you want to remove\n'))
        print('removed from list')
print('your to-do list has',tasks,'on it.')
#silly list so you can Keep Track of your Tasks because i keep my homework on a google doc to-do list 
#but its kinda stupid so i made a list where you can add/remove stuff after you Create it