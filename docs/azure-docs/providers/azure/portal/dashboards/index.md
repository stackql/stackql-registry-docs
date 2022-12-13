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
| `properties` | `object` | The shared dashboard properties. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Dashboards_Get` | `SELECT` | `dashboardName, resourceGroupName, subscriptionId` | Gets the Dashboard. |
| `Dashboards_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the Dashboards within a resource group. |
| `Dashboards_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all the dashboards within a subscription. |
| `Dashboards_CreateOrUpdate` | `INSERT` | `dashboardName, resourceGroupName, subscriptionId, data__location` | Creates or updates a Dashboard. |
| `Dashboards_Delete` | `DELETE` | `dashboardName, resourceGroupName, subscriptionId` | Deletes the Dashboard. |
| `Dashboards_Update` | `EXEC` | `dashboardName, resourceGroupName, subscriptionId` | Updates an existing Dashboard. |
