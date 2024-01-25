---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - container_storage
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
<tr><td><b>Id</b></td><td><code>azure.container_storage.pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Pool Properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `poolName, resourceGroupName, subscriptionId` | Get a Pool |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List Pool resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List Pool resources by subscription ID |
| `create_or_update` | `INSERT` | `poolName, resourceGroupName, subscriptionId` | Create a Pool |
| `delete` | `DELETE` | `poolName, resourceGroupName, subscriptionId` | Compliant create or update template/** |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List Pool resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List Pool resources by subscription ID |
| `update` | `EXEC` | `poolName, resourceGroupName, subscriptionId` | Update a Pool |
