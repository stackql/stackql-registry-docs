---
title: action_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - action_plans
  - deployment_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>action_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.deployment_admin.action_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `eTag` | `string` | Entity tag of the resource |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Action Plan Properties |
| `type` | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `planId, subscriptionId` | Gets the specified action plan |
| `list` | `SELECT` | `subscriptionId` | Gets the list of action plans |
| `_list` | `EXEC` | `subscriptionId` | Gets the list of action plans |
