# RoboScript Commands for TrueGPT

<details>
  <summary><h3>Internet & Communication</h3></summary>

| Command                  | Args                                       | Description                                                                               | Example                                                                                              |
|--------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `google_search`          | `query`: `<search>`                        | Performs a Google search for the specified query.                                         | `{"google_search": {"query": "best pizza in New York"}}`                                            |
| `browse_website`         | `url`: `<url>`, `question`: `<question>`   | Browses a website and finds information related to the specified question.                | `{"browse_website": {"url": "https://example.com", "question": "What are the opening hours?"}}`    |
| `send_email`             | `to`: `<email>`, `subject`: `<subject>`, `body`: `<body>` | Sends an email with the specified subject and body to the given recipient. | `{"send_email": {"to": "example@example.com", "subject": "Hello!", "body": "How are you?"}}`      |
| `send_message`           | `platform`: `<platform>`, `recipient`: `<recipient>`, `text`: `<text>` | Sends a message on the specified platform to the given recipient. | `{"send_message": {"platform": "telegram", "recipient": "@username", "text": "Hello!"}}`          |
| `publish_post`           | `platform`: `<platform>`, `content`: `<content>` | Publishes a post with the specified content on the given platform. | `{"publish_post": {"platform": "instagram", "content": {"image": "image_url", "caption": "My latest photo"}}}` |
</details>

<details>
  <summary><h3>File & Repository Management</h3></summary>

| Command                  | Args                                       | Description                                                                               | Example                                                                                              |
|--------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `clone_repository`       | `repository_url`: `<url>`, `clone_path`: `<directory>` | Clones a repository from the specified URL to the given directory. | `{"clone_repository": {"repository_url": "https://github.com/example/repo.git", "clone_path": "/home/user/projects"}}` |
| `write_to_file`          | `file_path`: `<file>`, `text`: `<text>`    | Writes the specified text to a file.                                                      | `{"write_to_file": {"file_path": "example.txt", "text": "Hello, world!"}}`                         |
| `read_file`              | `file_path`: `<file>`                      | Reads the specified file and returns its content.                                         | `{"read_file": {"file_path": "example.txt"}}`                                                      |
| `append_to_file`         | `file_path`: `<file>`, `text`: `<text>`    | Appends the specified text to a file.                                                     | `{"append_to_file": {"file_path": "example.txt", "text": " Appending this text"}}`                |
| `delete_file`            | `file_path`: `<file>`                      | Deletes the specified file.                                                               | `{"delete_file": {"file_path": "example.txt"}}`                                                    |
| `search_files`           | `directory`: `<directory>`                 | Searches for files in the specified directory.                                            | `{"search_files": {"directory": "/home/user/documents"}}`                                          |
</details>

<details>
  <summary><h3>Code & Task Management</h3></summary>

| Command                  | Args                                       | Description                                                                               | Example                                                                                              |
|--------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `analyze_code`           | `code`: `<full_code_string>`               | Analyzes the provided code and suggests improvements.                                     | `{"analyze_code": {"code": "def hello():\n  print('Hello, world!')"}}`                            |
| `improve_code`           | `suggestions`: `<list_of_suggestions>`, `code`: `<full_code_string>` | Applies the provided suggestions to the given code. | `{"improve_code": {"suggestions": ["Replace print with logging"], "code": "def hello():\n  print('Hello, world!')"}}` |
| `write_tests`            | `code`: `<full_code_string>`, `focus`: `<list_of_focus_areas>` | Writes tests for the provided code, focusing on the specified areas. | `{"write_tests": {"code": "def add(a, b):\n  return a + b", "focus": ["input validation", "edge cases"]}}` |
| `execute_python_file`    | `file_path`: `<file>`                      | Executes the specified Python file.                                                       | `{"execute_python_file": {"file_path": "example_script.py"}}`                                     |
| `task_complete`          | `reason`: `<reason>`                       | Shuts down the task and provides a reason for completion.                                  | `{"task_complete": {"reason": "Task successfully completed"}}`                                     |
  </details>


<details>
  <summary><h3>Multimedia</h3></summary>

| Command                  | Args                                       | Description                                                                               | Example                                                                                              |
|--------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `generate_image`         | `prompt`: `<prompt>`                       | Generates an image based on the specified prompt.                                         | `{"generate_image": {"prompt": "A beautiful sunset over a mountain range"}}`                       |
| `convert_audio_to_text`  | `file_path`: `<file>`                      | Converts the audio from the specified file to text.                                       | `{"convert_audio_to_text": {"file_path": "example_audio.wav"}}`                                   |
  </details>

<details>
  <summary><h3>AI Assistance</h3></summary>

| Command                  | Args                                       | Description                                                                               | Example                                                                                              |
|--------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `execute_shell_command`  | `command_line`: `<command_line>`           | Executes a non-interactive shell command.                                                | `{"execute_shell_command": {"command_line": "ls -la"}}`                                           |
| `execute_shell_popen`    | `command_line`: `<command_line>`           | Executes a non-interactive shell command using the Popen method.                         | `{"execute_shell_popen": {"command_line": "ls -la"}}`                                             |
| `wait`                   | `duration`: `<duration_in_seconds>`        | Waits for the specified duration (in seconds) before continuing.                          | `{"wait": {"duration": 5}}`                                                                        |
| `goal_achieved`          | `description`: `<short_goal_description>`  | Indicates that the specified goal has been achieved.                                      | `{"goal_achieved": {"description": "Successfully ordered pizza"}}`                                |
| `request_assistance`     | `issue`: `<issue_description>`             | Requests assistance from an operator to resolve the specified issue.                      | `{"request_assistance": {"issue": "Unable to find information on the specified website"}}`        |
| `do_nothing`             |                                            | Performs no action. Useful for testing or as a placeholder.                               | `{"do_nothing": {}}`                                                                               |
| `task_complete`          | `reason`: `<reason>`                       | Shuts down the task and provides a reason for completion.                                  | `{"task_complete": {"reason": "Task successfully completed"}}`                                     |
  </details>

<details>
  <summary><h3>RoboScript Events</h3></summary>

| Event                    | Args                                       | Description                                                                               | Example                                                                                              |
|--------------------------|--------------------------------------------|-------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `on_message_received`    | `sender`: `<sender>`, `message`: `<message>` | Triggered when a new message is received from a sender.                                   | `{"on_message_received": {"sender": "John Doe", "message": "Hello, how are you?"}}`                |
| `on_email_received`      | `sender`: `<sender_email>`, `subject`: `<subject>`, `body`: `<email_body>` | Triggered when a new email is received from a sender.                                     | `{"on_email_received": {"sender": "johndoe@example.com", "subject": "Meeting Reminder", "body": "Don't forget our meeting today at 3 PM!"}}` |
| `on_social_notification` | `platform`: `<platform>`, `type`: `<notification_type>`, `content`: `<content>` | Triggered when a new notification is received on a specified social media platform.       | `{"on_social_notification": {"platform": "Facebook", "type": "post_like", "content": "John Doe liked your post"}}` |
| `on_time_elapsed`        | `duration`: `<duration_in_seconds>`       | Triggered when a specified duration (in seconds) has elapsed.                             | `{"on_time_elapsed": {"duration": 300}}`                                                           |
  </details>
