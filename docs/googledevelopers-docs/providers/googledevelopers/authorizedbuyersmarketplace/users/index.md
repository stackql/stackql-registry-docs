---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - authorizedbuyersmarketplace
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.authorizedbuyersmarketplace.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the client user. Format: `buyers/&#123;accountId&#125;/clients/&#123;clientAccountId&#125;/users/&#123;userId&#125;` |
| `state` | `string` | Output only. The state of the client user. |
| `email` | `string` | Required. The client user's email address that has to be unique across all users for the same client. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `buyers_clients_users_get` | `SELECT` | `buyersId, clientsId, usersId` | Retrieves an existing client user. |
| `buyers_clients_users_list` | `SELECT` | `buyersId, clientsId` | Lists all client users for a specified client. |
| `buyers_clients_users_create` | `INSERT` | `buyersId, clientsId` | Creates a new client user in "INVITED" state. An email invitation will be sent to the new user, once accepted the user will become active. |
| `buyers_clients_users_delete` | `DELETE` | `buyersId, clientsId, usersId` | Deletes an existing client user. The client user will lose access to the Authorized Buyers UI. Note that if a client user is deleted, the user's access to the UI can't be restored unless a new client user is created and activated. |
| `buyers_clients_users_activate` | `EXEC` | `buyersId, clientsId, usersId` | Activates an existing client user. The state of the client user will be updated from "INACTIVE" to "ACTIVE". This method has no effect if the client user is already in "ACTIVE" state. An error will be returned if the client user to activate is still in "INVITED" state. |
| `buyers_clients_users_deactivate` | `EXEC` | `buyersId, clientsId, usersId` | Deactivates an existing client user. The state of the client user will be updated from "ACTIVE" to "INACTIVE". This method has no effect if the client user is already in "INACTIVE" state. An error will be returned if the client user to deactivate is still in "INVITED" state. |
