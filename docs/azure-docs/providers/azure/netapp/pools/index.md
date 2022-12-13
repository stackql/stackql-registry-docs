---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - netapp
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
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Pool properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Pools_Get` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId` | Get details of the specified capacity pool |
| `Pools_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List all capacity pools in the NetApp Account |
| `Pools_CreateOrUpdate` | `INSERT` | `accountName, poolName, resourceGroupName, subscriptionId, data__location, data__properties` | Create or Update a capacity pool |
| `Pools_Delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId` | Delete the specified capacity pool |
| `Pools_Update` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId` | Patch the specified capacity pool |
