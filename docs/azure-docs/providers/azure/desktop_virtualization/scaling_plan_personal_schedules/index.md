---
title: scaling_plan_personal_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_plan_personal_schedules
  - desktop_virtualization
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
<tr><td><b>Name</b></td><td><code>scaling_plan_personal_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.desktop_virtualization.scaling_plan_personal_schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | A ScalingPlanPersonalSchedule. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId` | Get a ScalingPlanPersonalSchedule. |
| `list` | `SELECT` | `resourceGroupName, scalingPlanName, subscriptionId` | List ScalingPlanPersonalSchedules. |
| `create` | `INSERT` | `resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId, data__properties` | Create or update a ScalingPlanPersonalSchedule. |
| `delete` | `DELETE` | `resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId` | Remove a ScalingPlanPersonalSchedule. |
| `_list` | `EXEC` | `resourceGroupName, scalingPlanName, subscriptionId` | List ScalingPlanPersonalSchedules. |
| `update` | `EXEC` | `resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId` | Update a ScalingPlanPersonalSchedule. |
