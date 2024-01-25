---
title: start_stop_managed_instance_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - start_stop_managed_instance_schedules
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
<tr><td><b>Name</b></td><td><code>start_stop_managed_instance_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.start_stop_managed_instance_schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of managed instance's Start/Stop schedule. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managedInstanceName, resourceGroupName, startStopScheduleName, subscriptionId` | Gets the managed instance's Start/Stop schedule. |
| `list_by_instance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Lists the managed instance's Start/Stop schedules. |
| `create_or_update` | `INSERT` | `managedInstanceName, resourceGroupName, startStopScheduleName, subscriptionId` | Creates or updates the managed instance's Start/Stop schedule. |
| `delete` | `DELETE` | `managedInstanceName, resourceGroupName, startStopScheduleName, subscriptionId` | Deletes the managed instance's Start/Stop schedule. |
| `_list_by_instance` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Lists the managed instance's Start/Stop schedules. |
