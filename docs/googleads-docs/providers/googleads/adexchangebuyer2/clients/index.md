---
title: clients
hide_title: false
hide_table_of_contents: false
keywords:
  - clients
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
<tr><td><b>Name</b></td><td><code>clients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.clients</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `string` | The status of the client buyer. |
| `entityType` | `string` | An optional field for specifying the type of the client entity: `ADVERTISER`, `BRAND`, or `AGENCY`. |
| `role` | `string` | The role which is assigned to the client buyer. Each role implies a set of permissions granted to the client. Must be one of `CLIENT_DEAL_VIEWER`, `CLIENT_DEAL_NEGOTIATOR` or `CLIENT_DEAL_APPROVER`. |
| `clientName` | `string` | Name used to represent this client to publishers. You may have multiple clients that map to the same entity, but for each client the combination of `clientName` and entity must be unique. You can specify this field as empty. Maximum length of 255 characters is allowed. |
| `entityName` | `string` | The name of the entity. This field is automatically fetched based on the type and ID. The value of this field is ignored in create and update operations. |
| `clientAccountId` | `string` | The globally-unique numerical ID of the client. The value of this field is ignored in create and update operations. |
| `entityId` | `string` | Numerical identifier of the client entity. The entity can be an advertiser, a brand, or an agency. This identifier is unique among all the entities with the same type. The value of this field is ignored if the entity type is not provided. A list of all known advertisers with their identifiers is available in the [advertisers.txt](https://storage.googleapis.com/adx-rtb-dictionaries/advertisers.txt) file. A list of all known brands with their identifiers is available in the [brands.txt](https://storage.googleapis.com/adx-rtb-dictionaries/brands.txt) file. A list of all known agencies with their identifiers is available in the [agencies.txt](https://storage.googleapis.com/adx-rtb-dictionaries/agencies.txt) file. |
| `visibleToSeller` | `boolean` | Whether the client buyer will be visible to sellers. |
| `partnerClientId` | `string` | Optional arbitrary unique identifier of this client buyer from the standpoint of its Ad Exchange sponsor buyer. This field can be used to associate a client buyer with the identifier in the namespace of its sponsor buyer, lookup client buyers by that identifier and verify whether an Ad Exchange counterpart of a given client buyer already exists. If present, must be unique among all the client buyers for its Ad Exchange sponsor buyer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_clients_get` | `SELECT` | `accountId, clientAccountId` | Gets a client buyer with a given client account ID. |
| `accounts_clients_list` | `SELECT` | `accountId` | Lists all the clients for the current sponsor buyer. |
| `accounts_clients_create` | `INSERT` | `accountId` | Creates a new client buyer. |
| `accounts_clients_update` | `EXEC` | `accountId, clientAccountId` | Updates an existing client buyer. |
