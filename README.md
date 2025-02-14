
<div align="center">

# Videoconference-using-zegocloud

</div>

This project is a web application that facilitates video conferencing using ZegoCloud. It allows users to register, log in, create new meetings, and join existing meetings.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)


## Features

- **User Authentication:** Secure user registration, login, and logout functionality.
- **Dashboard:** A personalized dashboard to manage meeting activities.
- **Meeting Creation:** Users can create new video conference meetings.
- **Join Meeting:** Users can join existing meetings by entering a room ID.
- **ZegoCloud Integration:** Utilizes ZegoCloud for video conferencing features.
- **Customizable UI:** Basic CSS styling for a user-friendly interface.

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/mayurexh/Videoconference-using-zegocloud.git
    cd Videoconference-using-zegocloud
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```
    *Note:* A `requirements.txt` file was not present in the repository.  Please create one listing all dependencies needed to run the project and include it in the repository.*

4.  Apply migrations:

    ```bash
    python manage.py migrate
    ```

## Usage

1.  Start the Django development server:

    ```bash
    python manage.py runserver
    ```

2.  Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

3.  Register a new user account or log in with existing credentials.

4.  From the dashboard, you can create a new meeting or join an existing one by entering the room ID.

## Dependencies

-   **Django:** A high-level Python web framework for building web applications quickly.
-   **ZegoUIKitPrebuilt:**  A library from ZegoCloud, used for implementing video conferencing features.


## Contributing

Contributions are welcome! Here's how you can contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, concise messages.
4.  Submit a pull request to the main branch.

