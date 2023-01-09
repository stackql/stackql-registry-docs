---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - adexchangebuyer2
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `clientAccountId` | `string` | Numerical account ID of the client buyer with which the user is associated; the buyer must be a client of the current sponsor buyer. The value of this field is ignored in an update operation. |
| `email` | `string` | User's email address. The value of this field is ignored in an update operation. |
| `status` | `string` | The status of the client user. |
| `userId` | `string` | The unique numerical ID of the client user that has accepted an invitation. The value of this field is ignored in an update operation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_clients_users_get` | `SELECT` | `accountId, clientAccountId, userId` | Retrieves an existing client user. |
| `accounts_clients_users_list` | `SELECT` | `accountId, clientAccountId` | Lists all the known client users for a specified sponsor buyer account ID. |
| `accounts_clients_users_update` | `EXEC` | `accountId, clientAccountId, userId` | Updates an existing client user. Only the user status can be changed on update. |
