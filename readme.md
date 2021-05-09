# Programming Task - Qtec Solution Limited

Create a parcel delivery software.

### Backend Stack

-   Django
-   MySQL

**URL: https://moshohel-delivary.herokuapp.com**

### Website is not working cause MySQL App needs ClearDB MySQL Add-ons Which is not for unverified(Free) Users.

#### User Types

-   Admin
-   Merchant
-   Super User

#### URL For Admin

### POST

-   Add a USER
    -   endpoint: /admin_user/createUser
    -   submit form data:
    ```
      {
        Username [Required] [Unique],
        Password [Required],
        Usser type [Required],
        Email ,
        First name,
        Last name
      }
    ```
-   Create New User
    -   endpoint: _/admin_user/create_parcel_
    -   form field :
    ```
      {
        Merchant [Required] {dropdown},
        Weight [Required],
        Product type [Required] {dropdown},
        Division [Required] {dropdown},
        Address [Required],
      }
    ```

#### GET

-   List of all Parcel
    -   endpoint: _/admin_user/parcel_list_

#### URL For Merchant

#### GET

-   List of Parcel of that Marchant
    -   endpoint: \_/merchant/parcel_list

#### Super User is responsible to mantain Application

-   Login URL for Super User
    -   endpoint: \_/admin

### Project Set Process

-   Download the project
-   Create Virtual Environment in project directory
-   Activate Environment
-   Run Command -

```json
pip install -r requirements.txt
```

-   If MySQL Client is not Installed Please Download MySQL Client and installed it
-   Run Command -

```
python manage.py runserver
```
