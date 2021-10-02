# Programming Task

Create a parcel delivery software.

### Backend Stack

-   Django
-   MySQL

**URL: http://raahinn.pythonanywhere.com/ **

## Steps to run the project-

-   Clone or Download the project.
    -   Create a Virtual Environment on the project repository & activate it.

#### Run Command -

```json
pip install -r requirements.txt
python manage.py runserver
```

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

### Super user

#### Users who have all the authorizations & permissions to maintain the applications

-   Login route
    -   endpoint: \_/admin

## For login use -

-   Admin user
    -   username: admin
    -   password: 123
-   Merchant user
    -   username: stylezone
    -   password: 123
-   Super User
    -   username: superuser
    -   password: 123
