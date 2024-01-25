---
title: data_manager_for_agriculture_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_manager_for_agriculture_resources
  - ag_food_platform
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>data_manager_for_agriculture_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ag_food_platform.data_manager_for_agriculture_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Data Manager For Agriculture ARM Resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Get DataManagerForAgriculture resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the DataManagerForAgriculture instances for a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists the DataManagerForAgriculture instances for a subscription. |
| `create_or_update` | `INSERT` | `dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Create or update Data Manager For Agriculture resource. |
| `delete` | `DELETE` | `dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Delete a Data Manager For Agriculture resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists the DataManagerForAgriculture instances for a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists the DataManagerForAgriculture instances for a subscription. |
| `update` | `EXEC` | `dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Update a Data Manager For Agriculture resource. |
