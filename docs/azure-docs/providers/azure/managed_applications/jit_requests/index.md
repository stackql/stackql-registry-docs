---
title: jit_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - jit_requests
  - managed_applications
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
<tr><td><b>Name</b></td><td><code>jit_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_applications.jit_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | Information about JIT request properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jitRequestName, resourceGroupName, subscriptionId` | Gets the JIT request. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all JIT requests within the resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all JIT requests within the subscription. |
| `create_or_update` | `INSERT` | `jitRequestName, resourceGroupName, subscriptionId` | Creates or updates the JIT request. |
| `delete` | `DELETE` | `jitRequestName, resourceGroupName, subscriptionId` | Deletes the JIT request. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all JIT requests within the resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all JIT requests within the subscription. |
| `update` | `EXEC` | `jitRequestName, resourceGroupName, subscriptionId` | Updates the JIT request. |
