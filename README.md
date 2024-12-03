# NoteApp API

The **NoteApp API** is a simple backend application built with **Django Rest Framework (DRF)** to manage user-specific notes. It supports basic note operations like adding, viewing, updating, and deleting notes. The application includes authentication for secure access and is designed as an API-only project.

## Features

- **User Authentication**:
  - Register new users.
  - Login for existing users using JWT tokens.

- **Note Management**:
  - Add, view, update, and delete notes.
  - Each user can only access their own notes.

## Tech Stack

- **Backend Framework**: Django 4.x, Django Rest Framework (DRF)
- **Database**: SQLite3 (default Django database)

## Installation

### Prerequisites
- Python 3.8 or above
- Virtual environment manager (e.g., `venv` or `pipenv`)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/noteapp.git
   cd noteapp
