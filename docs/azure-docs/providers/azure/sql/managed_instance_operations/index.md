---
title: managed_instance_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_operations
  - sql
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
<tr><td><b>Name</b></td><td><code>managed_instance_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instance_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managedInstanceName, operationId, resourceGroupName, subscriptionId` | Gets a management operation on a managed instance. |
| `list_by_managed_instance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of operations performed on the managed instance. |
| `_list_by_managed_instance` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of operations performed on the managed instance. |
| `cancel` | `EXEC` | `managedInstanceName, operationId, resourceGroupName, subscriptionId` | Cancels the asynchronous operation on the managed instance. |
