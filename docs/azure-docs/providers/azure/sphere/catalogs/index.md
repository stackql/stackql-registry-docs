---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
  - sphere
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
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sphere.catalogs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Catalog properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `catalogName, resourceGroupName, subscriptionId` | Get a Catalog |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List Catalog resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List Catalog resources by subscription ID |
| `create_or_update` | `INSERT` | `catalogName, resourceGroupName, subscriptionId` | Create a Catalog |
| `delete` | `DELETE` | `catalogName, resourceGroupName, subscriptionId` | Delete a Catalog |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List Catalog resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List Catalog resources by subscription ID |
| `count_devices` | `EXEC` | `catalogName, resourceGroupName, subscriptionId` | Counts devices in catalog. |
| `update` | `EXEC` | `catalogName, resourceGroupName, subscriptionId` | Update a Catalog |
