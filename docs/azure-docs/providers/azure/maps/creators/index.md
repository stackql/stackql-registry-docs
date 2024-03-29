---
title: creators
hide_title: false
hide_table_of_contents: false
keywords:
  - creators
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
<tr><td><b>Name</b></td><td><code>creators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maps.creators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Creator resource properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, creatorName, resourceGroupName, subscriptionId` | Get a Maps Creator resource. |
| `list_by_account` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Get all Creator instances for an Azure Maps Account |
| `create_or_update` | `INSERT` | `accountName, creatorName, resourceGroupName, subscriptionId, data__properties` | Create or update a Maps Creator resource. Creator resource will manage Azure resources required to populate a custom set of mapping data. It requires an account to exist before it can be created. |
| `delete` | `DELETE` | `accountName, creatorName, resourceGroupName, subscriptionId` | Delete a Maps Creator resource. |
| `_list_by_account` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Get all Creator instances for an Azure Maps Account |
| `update` | `EXEC` | `accountName, creatorName, resourceGroupName, subscriptionId` | Updates the Maps Creator resource. Only a subset of the parameters may be updated after creation, such as Tags. |
