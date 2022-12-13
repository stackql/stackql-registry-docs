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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstanceOperations_Get` | `SELECT` | `managedInstanceName, operationId, resourceGroupName, subscriptionId` | Gets a management operation on a managed instance. |
| `ManagedInstanceOperations_ListByManagedInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of operations performed on the managed instance. |
| `ManagedInstanceOperations_Cancel` | `EXEC` | `managedInstanceName, operationId, resourceGroupName, subscriptionId` | Cancels the asynchronous operation on the managed instance. |
