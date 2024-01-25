---
title: dev_centers
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_centers
  - dev_center
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
<tr><td><b>Name</b></td><td><code>dev_centers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_center.dev_centers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the devcenter. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `devCenterName, resourceGroupName, subscriptionId` | Gets a devcenter. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all devcenters in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all devcenters in a subscription. |
| `create_or_update` | `INSERT` | `devCenterName, resourceGroupName, subscriptionId` | Creates or updates a devcenter resource |
| `delete` | `DELETE` | `devCenterName, resourceGroupName, subscriptionId` | Deletes a devcenter |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all devcenters in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all devcenters in a subscription. |
| `update` | `EXEC` | `devCenterName, resourceGroupName, subscriptionId` | Partially updates a devcenter. |
