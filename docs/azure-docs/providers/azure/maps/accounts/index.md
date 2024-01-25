---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - maps
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maps.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `kind` | `string` | The Kind of the Maps Account. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Additional Maps account properties |
| `sku` | `object` | The SKU of the Maps Account. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Get a Maps Account. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get all Maps Accounts in a Resource Group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get all Maps Accounts in a Subscription |
| `create_or_update` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__sku` | Create or update a Maps Account. A Maps Account holds the keys which allow access to the Maps REST APIs. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete a Maps Account. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get all Maps Accounts in a Resource Group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get all Maps Accounts in a Subscription |
| `regenerate_keys` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__keyType` | Regenerate either the primary or secondary key for use with the Maps APIs. The old key will stop working immediately. |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates a Maps Account. Only a subset of the parameters may be updated after creation, such as Sku, Tags, Properties. |
