---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - netapp
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Pool properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId` | Get details of the specified capacity pool |
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List all capacity pools in the NetApp Account |
| `create_or_update` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId, data__location, data__properties` | Create or Update a capacity pool |
| `delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId` | Delete the specified capacity pool |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | List all capacity pools in the NetApp Account |
| `update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | Patch the specified capacity pool |
