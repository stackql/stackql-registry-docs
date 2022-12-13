---
title: private_link_scope_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_scope_operation_status
  - monitor
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
<tr><td><b>Name</b></td><td><code>private_link_scope_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.private_link_scope_operation_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The operation Id. |
| `name` | `string` | The operation name. |
| `status` | `string` | The status of the operation. |
| `endTime` | `string` | End time of the job in standard ISO8601 format. |
| `error` | `object` | The error detail. |
| `startTime` | `string` | Start time of the job in standard ISO8601 format. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PrivateLinkScopeOperationStatus_Get` | `SELECT` | `asyncOperationId, resourceGroupName, subscriptionId` |
