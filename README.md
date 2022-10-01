## Hactoberfest 2022

![hactoberfest 2022](https://res.cloudinary.com/practicaldev/image/fetch/s--ds97LCK---/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ymlmr15l83rrjq8natft.jpg)

### Introduction

Hacktoberfest is a month-long celebration of open source software. Anyone can participate by making four pull requests to public repositories on GitHub. The goal is to get more people involved in contributing to open source projects, and to learn more about the GitHub platform.


>> Note: This repository will be respecting the [Hacktoberfest Code of Conduct](https://hacktoberfest.digitalocean.com/details#conduct), the [GDSC Code of Conduct](https://gdsc.community.dev/participation-terms/) and [conventional commits](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/).

## Participating universities
- University Of Buea
- University of Yaounde
- University of Bamenda

## Contributions

There are 4 Tasks available and each task will be considered as valid by the Hacktoberfest team if properly carried out. Below are the tasks:

- **Prerequisite**
    Fork and Make the project available locally. Run the command below for that:

    ```bash
        git clone https://github.com/<username>/hactoberfest2022
    ```
    Create a branch for the task1
    ```bash
        git branch -M task1

        git checkout task1
    ```

- [**Task 1 (Introduction)**](./Task1/README.md)

    For task 1, follow these instructions below:
    - Add your details following the previous example.
    - Respect the JSON formatting
        ```json
        [
            {
                "name": "Steve Yonkeu",
                "github_handle": "yokwejuste",
                "hacktoberfest_round": "third",
                "role": [
                    "maintainer",
                    "contributor"
                ]
            },
            {
                "name": "Fisher Monk",
                "github_handle": "fisherman20183698",
                "hacktoberfest_round": "first",
                "role": [
                    "contributor"
                ]
            }
        ]
        ```
    - Commit the change made and push

        ```bash
        git commit -am "feat: added <username> as contributor"

        git push -u

        ```
      >> Note: For any PR submitted before 1<sup>st</sup> of October, submit it as a draft pull request. Only PR opened as from early october are accepted by Hacktoberfest team. Thanks for undestanding.
    - Go to our your github and a pull request
        ![open a pull request](https://i0.wp.com/user-images.githubusercontent.com/3477155/52671177-5d0e0100-2ee8-11e9-8645-bdd923b7d93b.gif?resize=1024%2C512&ssl=1)

- [**Task 2 (Socials)**](./Task2/README.md)

    Here, all you need is put your social media handles as follows:
    - Create a new branch for this task from the `master branch`, call it `task2`.

        ```bash
        git checkout master

        git branch -M task2
        ```
    - Declare a variable for your socials as `<username>_socials`
    - Follow the defined structure
    ```javascript
    [
        yokwejuste_socials = {
            "twitter_handle": "yokwejuste",
            "likedin_handle": "yokwejuste",
            "facebook": "yokwejuste5013",
            "telegram_handle": "googledevz"
        },
        topolo_socials = {
            "twitter_handle": "topolo",
            "likedin_handle": "topolo2211772",
            "facebook": "topolo0",
            "telegram_handle": ""
        }
    ]
    ```
    - Commit these changes and make a pull request for this task.
        ```bash
        git commit -am "feat: added <username> socials"

        git push
        ```
    - Open a pull request from github.

- [**Task 3 (Educational Experience)**](./Task3/README.md)

    Before anything else change the branch and make a new one from the `master branch`.
    ```bash
        git checkout master

        git branch -M task3
    ```
    - This task is in relation to your educational experience. It's done as follows:
    ```python
    [
        ["university of bamenda", "Nahpi", "2019", "present"],
        ["university of houston", "Faculty of Science", "2016", "2019"],
    ]
    ```
    - Commit, push and make a pull request
    ```bash
    git commit -am "feat: added educational background of <username>"

    git push
    ```
    - Open a pull request.
    
- [**Task 4 (Tech Stack)**](./Task4/README.md)

    - Create new branch from the `master branch`
        ```bash
        git checkout master

        git branch -M task4
        ```
    - Contribute using the format below
    ```html
    <html>
        <head>
            <title>
                Hacktoberfest 2022
            </title>
        </head>
        <body>
            <div id="<username>_techstack">
                <p class="tech_stack_item">
                    Figma
                </p>
                <p class="tech_stack_item">
                    UI/UX
                </p>
                <p class="tech_stack_item">
                    Canva
                </p>
            </div>
            <div id="yokwejuste_techstack">
                <p class="tech_stack_item">
                    ReactJs
                </p>
                <p class="tech_stack_item">
                    Django
                </p>
                <p class="tech_stack_item">
                    Flask
                </p>
            </div>
        </body>
    </html>
    ```
    - Save your changes, commit, push and mnake a pull request.
    ```bash
    git commit -am "feat: added my techstack - yokwejuste"

    git push
    ```

## Thanks to all our contributors

<img src = "https://contrib.rocks/image?repo=Developer-Student-Clubs-UBa/hactoberfest2022"/>

This is an opensource project under the [GNU GENERAL PUBLIC LICENSE](./LICENSE).

Happy hacking!!!
