<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">FIND-YOUR-GUIDE</h1>
</p>
<p align="center">
    <em>HTTP error 401 for prompt `slogan`</em>
</p>
<p align="center">
    <img src="https://img.shields.io/github/license/erdincakgun/find-your-guide?style=flat&color=0080ff" alt="license">
    <img src="https://img.shields.io/github/last-commit/erdincakgun/find-your-guide?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/erdincakgun/find-your-guide?style=flat&color=0080ff" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/erdincakgun/find-your-guide?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
    <em>Developed with the software and tools below.</em>
</p>
<p align="center">
    <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
    <img src="https://img.shields.io/badge/Babel-F9DC3E.svg?style=flat&logo=Babel&logoColor=black" alt="Babel">
    <img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
    <img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
    <img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
    <br>
    <img src="https://img.shields.io/badge/Gunicorn-499848.svg?style=flat&logo=Gunicorn&logoColor=white" alt="Gunicorn">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=Flask&logoColor=white" alt="Flask">
</p>
<hr>

## Quick Links

> - [Overview](#-overview)
> - [Features](#-features)
> - [Installation](#-installation)
> - [Usage](#-usage)
> - [Project Roadmap](#-project-roadmap)
> - [Contributing](#-contributing)
> - [License](#-license)
> - [Acknowledgments](#-acknowledgments)

---

## Overview

Find Your Guide is a web application designed to connect runners with local guides for tailored running experiences. Whether you're traveling to a new city or looking for a unique running adventure in your hometown, our platform helps you find the perfect guide to enhance your running journey.

## Features

- **Browse Guides:** Discover profiles of local running guides with detailed descriptions and reviews.
- **Book Experiences:** Easily schedule and book running experiences directly through the app.
- **Customizable Runs:** Work with your guide to create a personalized running experience that matches your preferences and fitness level.
- **Secure Payments:** Enjoy secure and hassle-free transactions within the app.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/erdincakgun/find-your-guide.git
   cd find-your-guide
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy the contents of `.env.example` to a new file named `.env` and update the values as needed.

5. **Run database migrations:**
   ```sh
   flask db upgrade
   ```

6. **Start the development server:**
   ```sh
   flask run
   ```

## Usage

To use Find Your Guide, follow these steps:

1. **Sign Up/Log In:** Create an account or log in if you already have one.
2. **Search for Guides:** Browse through the available guides in your desired location.
3. **Book a Run:** Select a guide and book a running experience that fits your schedule.
4. **Enjoy Your Run:** Meet your guide and enjoy your tailored running experience.
5. **Leave a Review:** Provide feedback on your experience to help other users.

## Project Roadmap

- [X] Implement user authentication and profile management.
- [X] Develop guide search and filtering functionality.
- [ ] Integrate payment gateway for secure transactions.
- [ ] Add multi-language support.
- [ ] Enhance user interface and experience.

## Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/erdincakgun/find-your-guide/blob/main/CONTRIBUTING.md):** Review open PRs and submit your own.
- **[Join the Discussions](https://github.com/erdincakgun/find-your-guide/discussions):** Share insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/erdincakgun/find-your-guide/issues):** Submit bugs or log feature requests.

<details>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository:** Start by forking the project repository to your GitHub account.
2. **Clone Locally:** Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/erdincakgun/find-your-guide.git
   ```
3. **Create a New Branch:** Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes:** Develop and test your changes locally.
5. **Commit Your Changes:** Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub:** Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request:** Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

## License

This project is protected under the [MIT License](https://choosealicense.com/licenses/mit/). For more details, refer to the [LICENSE](LICENSE) file.

## Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)