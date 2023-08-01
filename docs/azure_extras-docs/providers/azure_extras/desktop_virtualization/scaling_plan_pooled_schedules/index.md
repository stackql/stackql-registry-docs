---
title: scaling_plan_pooled_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_plan_pooled_schedules
  - desktop_virtualization
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
<tr><td><b>Name</b></td><td><code>scaling_plan_pooled_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.desktop_virtualization.scaling_plan_pooled_schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | A ScalingPlanPooledSchedule. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScalingPlanPooledSchedules_Get` | `SELECT` | `resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId` | Get a ScalingPlanPooledSchedule. |
| `ScalingPlanPooledSchedules_List` | `SELECT` | `resourceGroupName, scalingPlanName, subscriptionId` | List ScalingPlanPooledSchedules. |
| `ScalingPlanPooledSchedules_Create` | `INSERT` | `resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId, data__properties` | Create or update a ScalingPlanPooledSchedule. |
| `ScalingPlanPooledSchedules_Delete` | `DELETE` | `resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId` | Remove a ScalingPlanPooledSchedule. |
| `ScalingPlanPooledSchedules_Update` | `EXEC` | `resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId` | Update a ScalingPlanPooledSchedule. |
