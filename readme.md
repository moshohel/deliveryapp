# Programming Task - Qtec Solution Limited

Create a parcel delivery software.

### Backend Stack

-   Django
-   MySQL

**URL: https://moshohel-delivary.herokuapp.com/ **

#### User Types

-   Admin
-   Merchant

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
