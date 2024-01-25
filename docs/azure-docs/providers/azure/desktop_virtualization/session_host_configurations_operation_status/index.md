---
title: session_host_configurations_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - session_host_configurations_operation_status
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>session_host_configurations_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.desktop_virtualization.session_host_configurations_operation_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified ID for the async operation. |
| `name` | `string` | Name of the async operation. |
| `endTime` | `string` | The end time of the operation. |
| `error` | `object` | The error detail. |
| `operations` | `array` | The operations list. |
| `percentComplete` | `number` | Percent of the operation that is complete. |
| `startTime` | `string` | The start time of the operation. |
| `status` | `string` | Operation status. Current defined values are &lt;UpdateFailed \| Paused \| Pausing \| Cancelling \| InProgress \| Succeeded \| Failed \| Canceled&gt; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hostPoolName, operationId, resourceGroupName, subscriptionId` | Get Operation status for SessionHostManagement |
| `list` | `SELECT` | `hostPoolName, resourceGroupName, subscriptionId` | Get Operation status for SessionHostConfiguration |
| `_list` | `EXEC` | `hostPoolName, resourceGroupName, subscriptionId` | Get Operation status for SessionHostConfiguration |
