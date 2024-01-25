---
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboards
  - portal
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
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.portal.dashboards</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | The shared dashboard properties. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dashboardName, resourceGroupName, subscriptionId` | Gets the Dashboard. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the Dashboards within a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets all the dashboards within a subscription. |
| `create_or_update` | `INSERT` | `dashboardName, resourceGroupName, subscriptionId, data__location` | Creates or updates a Dashboard. |
| `delete` | `DELETE` | `dashboardName, resourceGroupName, subscriptionId` | Deletes the Dashboard. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all the Dashboards within a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets all the dashboards within a subscription. |
| `update` | `EXEC` | `dashboardName, resourceGroupName, subscriptionId` | Updates an existing Dashboard. |
