---
title: action_plan_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - action_plan_operations
  - deployment_admin
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
<tr><td><b>Name</b></td><td><code>action_plan_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_admin.action_plan_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Action Plan Operation Properties |
| `type` | `string` | Type of Resource. |
| `eTag` | `string` | Entity tag of the resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ActionPlanOperations_Get` | `SELECT` | `operationId, planId, subscriptionId` | Gets the specified action plan operation |
| `ActionPlanOperations_List` | `SELECT` | `planId, subscriptionId` | Lists the action plan operations |
