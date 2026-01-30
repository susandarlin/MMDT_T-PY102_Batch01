### 📁 Assignment Submission on GitHub

All homework assignments for this course must be submitted via a **GitHub Pull Request**. This process ensures that your submissions are tracked, organized, and provides a clear way for the instructor to review your work.

You have two options for submitting your work, depending on your comfort level with Git.

---

### **Option 1: Web-Based Submission (Recommended for Beginners)** 🌐

This method allows you to submit your homework directly through the GitHub website without needing to install Git on your computer.

**Step 1: Fork the Homework Repository**
* Navigate to the class's **homework repository** on GitHub.
* Click the **'Fork'** button in the top-right corner. This will create a personal copy of the repository in your GitHub account.

**Step 2:Locate Your Assigned Folder**
* Inside the repository, a folder named with your student ID (e.g., submissions/PY102001001/) has already been created for you by the instructor.
* Do not create a new folder or rename the existing one. You must place all your lab submissions inside your assigned folder only.

**Step 3: Upload Your Homework Files**
* Open your ID-named folder (submissions/PY102001001/).
* Click **'Add file'** and then **'Upload files'**.
* Drag and drop all your completed homework files directly into the browser window.
* Each lab must be a single Python file named exactly as shown below:
- Lab 1 → lab01.py
- Lab 2 → lab02.py
- Lab 3 → lab03.py
* Do not create any subfolders inside your ID folder.

**Step 4: Commit and Submit**
* At the bottom of the page, add a clear and descriptive commit message, such as: `Submit Lab 1 - [Your ID]`.
* Click the **'Commit changes'** button.
* Go back to the main page of your forked repository. You should see a banner indicating that your changes are ready to be submitted. Click **'Contribute'** and then **'Open pull request'**.
* On the next screen, give your pull request a clear title and description, and then click **'Create pull request'** to submit.

---

### **Option 2: Local Machine Submission (Advanced Users)** 💻

This is the standard, professional method for using Git. It requires you to have Git installed on your computer.

**Step 1: Fork and Clone the Repository**
* **Fork:** First, fork the main homework repository on GitHub.
* **Clone:** Open your terminal or command prompt. Clone your forked repository to your local machine:
    ```
    git clone [https://github.com/](https://github.com/)<your-name>/MMDT_T-PY102_Batch[01]
    ```
* **Navigate:** Change into the repository folder:
    ```
    cd [name of the repo]
    ```
**Step 2:Locate Your Assigned Folder**
* Inside the repository, a folder named with your student ID (e.g., submissions/PY102001001/) has already been created for you by the instructor.
* Do not create a new folder or rename the existing one. You must place all your lab submissions inside your assigned folder only.
* Do not create any subfolders inside your ID folder.

**Step 3: Add, Commit, and Push Your Homework**
* Save or copy your lab file into your ID folder using this exact naming convention:
```
submissions/PY102001001/lab01.py
submissions/PY102001001/lab02.py
```
* Stage the new files to be tracked by Git:
    ```
    git add submissions/PY102001001/lab01.py
    ```
* Commit your changes with a clear message:
    ```
    git commit -m "Submit Homework [Number] - [Your ID]"
    ```
* Push your changes to your forked repository on GitHub:
    ```
    git push origin main
    ```

**Step 4: Create a Pull Request**
* Go to your forked repository on GitHub.
* Make sure your changes are only inside your assigned folder under submissions/
(for example: submissions/PY102001001/lab01.py).
* A banner will appear at the topat the top of the repository prompting you to create a pull request. 
Click **'Compare & pull request'**.
* Write a clear title and description (include your student ID and lab number) for your submission and click **'Create pull request'**.
