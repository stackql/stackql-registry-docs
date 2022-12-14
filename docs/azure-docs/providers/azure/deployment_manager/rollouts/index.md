---
title: rollouts
hide_title: false
hide_table_of_contents: false
keywords:
  - rollouts
  - deployment_manager
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
<tr><td><b>Name</b></td><td><code>rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_manager.rollouts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties that define a rollout. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Rollouts_Get` | `SELECT` | `resourceGroupName, rolloutName, subscriptionId` |  |
| `Rollouts_List` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `Rollouts_CreateOrUpdate` | `INSERT` | `resourceGroupName, rolloutName, subscriptionId, data__identity, data__properties` | This is an asynchronous operation and can be polled to completion using the location header returned by this operation. |
| `Rollouts_Delete` | `DELETE` | `resourceGroupName, rolloutName, subscriptionId` | Only rollouts in terminal state can be deleted. |
| `Rollouts_Cancel` | `EXEC` | `resourceGroupName, rolloutName, subscriptionId` | Only running rollouts can be canceled. |
| `Rollouts_Restart` | `EXEC` | `resourceGroupName, rolloutName, subscriptionId` | Only failed rollouts can be restarted. |
