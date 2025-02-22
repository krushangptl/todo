# TODO App

## Installation 

Here is Command:
```
git clone --depth 1 https://github.com/krushangptl/todo 
```

Set as Executable:
```
cd todo
chmod +x todo
```

Move `todo` in `/usr/local/bin`

```
sudo mv todo /usr/local/bin/

which todo
```

## How to use? 

- Initialize `todo` CLI Application 
```
todo
```

- Add Tasks 

```
todo add "Task 1"
todo add "Task 2"
todo add "Task 3"
```

- List Tasks
```
todo list
```
```
=== Todo ===
Index | Task | Status
---------------------
1 | Task 1 | Pending
2 | Task 2 | Pending
3 | Task 3 | Pending
```

- Mark Task as Done
```
todo done 2 
```
```
=== Task Completed: Task 2 ===
```
```
todo list
```
```
=== Todo ===
Index | Task | Status
---------------------
1 | Task 1 | Pending
2 | Task 2 | Done
3 | Task 3 | Pending
```

- Delete Task 
```
todo delete 2
```
```
=== Task Deleted: Task 2 ===
```
```
todo list
```
```
=== Todo ===
Index | Task | Status
---------------------
1 | Task 1 | Pending
2 | Task 3 | Pending
```

