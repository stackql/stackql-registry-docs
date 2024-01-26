---
title: plans
hide_title: false
hide_table_of_contents: false
keywords:
  - plans
  - subscriptions_admin
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
<tr><td><b>Name</b></td><td><code>plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.subscriptions_admin.plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource |
| `properties` | `object` | Properties of a plan. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `plan, resourceGroupName, subscriptionId` | Get the specified plan. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Get the list of plans under a resource group. |
| `create_or_update` | `INSERT` | `plan, resourceGroupName, subscriptionId` | Create or update the plan. |
| `delete` | `DELETE` | `plan, resourceGroupName, subscriptionId` | Delete the specified plan. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Get the list of plans under a resource group. |
