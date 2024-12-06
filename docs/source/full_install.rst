Full Installation Guide
=======================

This guide provides detailed steps to set up, deploy, and manage the **Orange County Lettings** website.

Prerequisites
-------------

Ensure you have the following installed:

- GitHub account with repository access.
- Git CLI.
- SQLite3 CLI.
- Python 3.12 or higher.

Local Development
-----------------

for base install refer to :doc:`quick_start`.

Database Management
-------------------

1. In the project folder, open a SQLite3 session:

   .. code-block:: bash

      sqlite3 oc-lettings-site.sqlite3

2. Display the tables:

   .. code-block:: sql

      .tables

3. Query the profiles table info:

   .. code-block:: sql

      pragma table_info(profiles_profile);

3. Query the profiles table:

   .. code-block:: sql

      select user_id, favorite_city from profiles_profile where favorite_city like 'B%';

4. Exit the session:

   .. code-block:: sql

      .quit

CI/CD Deployment
----------------

The project is deployed using GitHub Actions and Render.

### Pipeline Overview

1. **Tests and Linting:**
   - Every push runs `pytest` for unit tests and `flake8` for linting.

2. **Docker Image Build and Deployment:**
   - On successful tests, Docker images are built and pushed to Docker Hub.
   - Render deploys the application based on the Docker image for the `master` branch.

Secrets Configuration
---------------------

Configure the following secrets in GitHub:

- `DEBUG`: Set to `False` in production.
- `SENTRY_DSN`: For error tracking.
- `ALLOWED_HOSTS`: List of allowed hostnames.
- `DOCKER_USERNAME` and `DOCKER_PASSWORD`: Docker Hub credentials.
- `RENDER_API_KEY`: Render API key for deployment.
- `RENDER_SERVICE_ID`: Render service ID for deployment.

Deployment on Render
--------------------

1. Create a new Web Service on Render.
2. Configure it to use an existing Docker image.
3. Add required environment variables:
   - `ALLOWED_HOSTS`
   - `SECRET_KEY`
   - `DEBUG` (set to `False`)
   - `PORT` (set to `8000`)
   - `DB_PATH` (path to the SQLite database)

Push changes to the `master` branch, and the pipeline will automatically deploy the application.
