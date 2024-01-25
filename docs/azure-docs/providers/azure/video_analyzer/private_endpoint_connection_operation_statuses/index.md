---
title: private_endpoint_connection_operation_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection_operation_statuses
  - video_analyzer
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connection_operation_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.video_analyzer.private_endpoint_connection_operation_statuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Operation resource ID. |
| `name` | `string` | Operation identifier. |
| `endTime` | `string` | Operation end time. |
| `error` | `object` | The error detail. |
| `startTime` | `string` | Operation start time. |
| `status` | `string` | Operation status. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `accountName, name, operationId, resourceGroupName, subscriptionId` |
