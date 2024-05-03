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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_plan_personal_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.scaling_plan_personal_schedules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A ScalingPlanPersonalSchedule. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId" /> | Get a ScalingPlanPersonalSchedule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, scalingPlanName, subscriptionId" /> | List ScalingPlanPersonalSchedules. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId, data__properties" /> | Create or update a ScalingPlanPersonalSchedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId" /> | Remove a ScalingPlanPersonalSchedule. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, scalingPlanName, subscriptionId" /> | List ScalingPlanPersonalSchedules. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId" /> | Update a ScalingPlanPersonalSchedule. |
