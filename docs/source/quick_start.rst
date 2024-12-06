Quick Start Guide
=================

This guide provides a quick setup to run the **Orange County Lettings** website locally.

Prerequisites
-------------

Make sure you have the following installed:

- A GitHub account with access to the repository.
- Git CLI.
- SQLite3 CLI.
- Python 3.12 or higher.

Clone the Repository
--------------------

Run the following commands in your terminal:

.. code-block:: bash

   cd /path/to/put/project/in
   git clone https://github.com/CuteSlime/P13_Mettez_a_l_echelle_une_application_Django_en_utilisant_une-_architecture_modulaire.git

Create and Activate a Virtual Environment
-----------------------------------------

1. Navigate to the project directory:

   .. code-block:: bash

      cd /path/to/Python-OC-Lettings-FR

2. Create the virtual environment:

   .. code-block:: bash

      python -m venv venv

   **Note:** If you encounter errors on Ubuntu, install the `python3-venv` package:

   .. code-block:: bash

      sudo apt-get install python3-venv

3. Activate the virtual environment:

   - macOS/Linux:

     .. code-block:: bash

        source venv/bin/activate

   - Windows:

     .. code-block:: bash

        .\venv\Scripts\Activate.ps1

4. Confirm that the correct Python interpreter and `pip` are used:

   .. code-block:: bash

      which python
      python --version
      which pip

Run the Website
---------------

1. Install the project dependencies:

   .. code-block:: bash

      pip install --requirement requirements.txt

2. make sure that the DB is up to date:

   .. code-block:: bash

      python manage.py migrate

3. Run the Django development server:

   .. code-block:: bash

      python manage.py runserver

4. Open a web browser and navigate to `http://localhost:8000` to verify the website is running.


for more information (with docker and Render service), see the full installation guide in the :doc:`full_install`.