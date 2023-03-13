# Task 1
1. Create branch from `main` called `feat/<yourname>`.
   ```shell
   # make sure your current branch is `main`
   git branch
   # * main
   # now create a your branch
   git checkout -b feat/<yourname>
   # verify you are in your branch now
   git branch
   # * feat/<yourname>
   ```
   
   This will be your working branch. Before start working on a new task, always do:
   
   ```shell
   # pull into your branch latest changes (commits) from `main`
   git pull origin main
   ```
2. Create python program which prints variable with a value "Hello World!" to console inside `hello_world.py`
3. Commit your changes.
   ```shell
   git add week_1/hello_world/hello_world.py
   git commit -m "my first program in Python"
   git push
   ```
