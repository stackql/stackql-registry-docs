---
title: jit_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - jit_requests
  - solutions
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
<tr><td><b>Name</b></td><td><code>jit_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.solutions.jit_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID |
| `name` | `string` | Resource name |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
| `properties` | `object` | Information about JIT request properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JitRequests_Get` | `SELECT` | `jitRequestName, resourceGroupName, subscriptionId` | Gets the JIT request. |
| `jitRequests_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all JIT requests within the resource group. |
| `jitRequests_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all JIT requests within the subscription. |
| `jitRequests_CreateOrUpdate` | `INSERT` | `jitRequestName, resourceGroupName, subscriptionId` | Creates or updates the JIT request. |
| `jitRequests_Delete` | `DELETE` | `jitRequestName, resourceGroupName, subscriptionId` | Deletes the JIT request. |
| `JitRequests_Update` | `EXEC` | `jitRequestName, resourceGroupName, subscriptionId` | Updates the JIT request. |
