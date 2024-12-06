User guide
==========


Use Case 1: View Lettings
-------------------------

**Objective**: A user wants to explore available rental properties.

    **Scenario**:

        1. User lands on the Home Page and clicks on the Lettings button.
        2. The user is redirected to the Lettings Page where a list of lettings is displayed.
        3. User clicks on a letting to view its details.
        4. On the Letting Detail Page, the user reviews the letting's address and navigates back to the Lettings list or to the Home Page.

    **Steps**:

        1. Visit /.
        2. Navigate to /lettings/.
        3. Click on a letting (e.g., "Oceanview Retreat").
        4. Review details at /lettings/<letting_id>/.

    **Expected Outcome**:

        - User finds information about rental properties.

Use Case 2: View a Profile
--------------------------

**Objective**: A user wants to view details of a specific profile.

    **Scenario**:

        1. User lands on the Home Page and clicks on the Profiles button.
        2. The user is redirected to the Profiles Page, which lists usernames.
        3. User selects a username to view the corresponding profile details.
        4. On the Profile Detail Page, the user reviews the details and navigates back to the Profiles list or to the Lettings Page.

    **Steps**:

        1. Visit /.
        2. Navigate to /profiles/.
        3. Click on a username (e.g., "HeadlinesGazer").
        4. Review details at /profiles/<username>/.

    **Expected Outcome**:

        User accesses and reviews profile details, including favorite city.

Use Case 3: access to a page that doesn't exist anymore
-------------------------------------------------------

**Objective**: A user wants to view a page that doesn't exist anymore.

    **Scenario**:

        1. User tries to access a page that has been removed or never existed.
        2. The user is redirected to a 404 page.
        3. User can navigate back to the Home Page or other available pages.

    **Steps**:

        1. Visit a non-existent page (e.g., /profiles/<deleted_user>/).
        2. redirected to a 404 page.
        3. Navigate back to the Home Page or other available pages.

    **Expected Outcome**:

        User is redirected to personalized 404 page.

Use Case 4: server issue
------------------------

**Objective**: A user encounters a server issue.

    **Scenario**:

        1. User tries to access a page but encounters a server error.
        2. The user sees an error message indicating that the server has an issue.
        3. User can try to refresh the page, navigate back or return later.

    **Steps**:

        1. Visit a page that triggers a server error.
        2. See page 500 error message.
        3. Try to refresh the page, navigate back, or return later.
    
    **Expected Outcome**:
    
            User is informed about the server issue and can take appropriate actions.