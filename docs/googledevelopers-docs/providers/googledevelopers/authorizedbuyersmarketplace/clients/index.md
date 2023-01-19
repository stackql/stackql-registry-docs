---
title: clients
hide_title: false
hide_table_of_contents: false
keywords:
  - clients
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
<tr><td><b>Name</b></td><td><code>clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.authorizedbuyersmarketplace.clients</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the client. Format: `buyers/&#123;accountId&#125;/clients/&#123;clientAccountId&#125;` |
| `role` | `string` | Required. The role assigned to the client. Each role implies a set of permissions granted to the client. |
| `sellerVisible` | `boolean` | Whether the client will be visible to sellers. |
| `state` | `string` | Output only. The state of the client. |
| `displayName` | `string` | Required. Display name shown to publishers. Must be unique for clients without partnerClientId specified. Maximum length of 255 characters is allowed. |
| `partnerClientId` | `string` | Arbitrary unique identifier provided by the buyer. This field can be used to associate a client with an identifier in the namespace of the buyer, lookup clients by that identifier and verify whether an Authorized Buyers account of the client already exists. If present, must be unique across all the clients. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `buyers_clients_get` | `SELECT` | `buyersId, clientsId` | Gets a client with a given resource name. |
| `buyers_clients_list` | `SELECT` | `buyersId` | Lists all the clients for the current buyer. |
| `buyers_clients_create` | `INSERT` | `buyersId` | Creates a new client. |
| `buyers_clients_activate` | `EXEC` | `buyersId, clientsId` | Activates an existing client. The state of the client will be updated to "ACTIVE". This method has no effect if the client is already in "ACTIVE" state. |
| `buyers_clients_deactivate` | `EXEC` | `buyersId, clientsId` | Deactivates an existing client. The state of the client will be updated to "INACTIVE". This method has no effect if the client is already in "INACTIVE" state. |
| `buyers_clients_patch` | `EXEC` | `buyersId, clientsId` | Updates an existing client. |
