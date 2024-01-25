---
title: session_host_managements_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - session_host_managements_operation_status
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
<tr><td><b>Name</b></td><td><code>session_host_managements_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.desktop_virtualization.session_host_managements_operation_status</code></td></tr>
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
| `properties` | `object` | Properties bag to hold custom RP properties for sessionHostManagement Operation Statuses. |
| `startTime` | `string` | The start time of the operation. |
| `status` | `string` | Operation status. Current defined values are &lt; Scheduled \| UpdatingSessionHosts \| ValidatingSessionHostUpdate \| Paused \| Pausing \| Cancelling \| Resuming \| Starting &gt; \| Succeeded \| Failed \| Canceled |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `hostPoolName, operationId, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `hostPoolName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `hostPoolName, resourceGroupName, subscriptionId` |
