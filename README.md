## Individual assignment practice

This assignment provides some practice on how to complete individual assignments using Git and GitHub. First, view the assignment from the GitHub organization linked below:

`https://github.com/orgs/rsm-msba-25-26/repositories`

Clone the repo to your laptop using the commands below, after you replace `aaa111` with the first part of your @ucsd.edu email address. Run this code in a terminal in VS Code attached to the RSM-MSBA docker container:

```bash
username="aaa111";
git clone git@github.com:rsm-msba-25-26/rsm-gh-assignment-practice-rsm-$username ~/git/rsm-gh-assignment-practice;
```

This is your copy of the original assignment on GitHub. The content is in the `~/git/rsm-gh-assignment-practice` directory on your computer for you to work on using VS Code.

Use **File > Open Folder** to navigate to the new folder and set it as the project folder in VS Code.

> Note: NEVER click on **Show Local** when you are navigating to a folder to connect to VS Code. Clicking on **Show Local** will detach VS Code from the RSM-MSBA docker container.

After cloning the assignment, check the remote repo the folder you are in is connected to by running the code below from a terminal in VS Code:

```bash
cat ~/git/rsm-gh-assignment-practice/.git/config;
```

If the contents of the `config` file are shown and mention your repo on GitHub, you are ready to move on to the next step.

Provide the information requested below. Then (1) save this markdown (md) file, (2) commit your changes to Git, and (3) push your work back to GitHub. After pushing your changes double-check that they are indeed visible in your repo on <https://github.com/orgs/rsm-msba-25-26/repositories>

---

Provide the information requested below:

- Last name: Vuppu123
- First (or preferred) name: Chandana
- Favorite food: Pasta
- Favorite recent Netflix movie or show: Community

---

If you have any problems with this practice assignment, take screenshots and post them to <https://piazza.com/ucsd/summer2025/rady499>.

> Note: You can copy-and-paste images directly into Piazza rather than having to upload an image file. This will make your post quicker and easier to review
