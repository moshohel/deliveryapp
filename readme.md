# Programming Task - Qtec Solution Limited

Create a parcel delivery software.

### Backend Stack

-   Django
-   MySQL

**URL: https://moshohel-delivary.herokuapp.com/ **

### ### Website is not working cause MySQL App needs ClearDB MySQL Add-ons on Heroku Which is not for unverified(Free) Users.

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
