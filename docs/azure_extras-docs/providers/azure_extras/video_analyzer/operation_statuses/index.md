---
title: operation_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_statuses
  - video_analyzer
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
<tr><td><b>Name</b></td><td><code>operation_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.video_analyzer.operation_statuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Operation resource ID. |
| `name` | `string` | Operation identifier. |
| `error` | `object` | The error detail. |
| `startTime` | `string` | Operation start time. |
| `status` | `string` | Operation status. |
| `endTime` | `string` | Operation end time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `OperationStatuses_Get` | `SELECT` | `accountName, name, operationId, resourceGroupName, subscriptionId` | Get private endpoint connection operation status. |
| `VideoAnalyzerOperationStatuses_Get` | `SELECT` | `locationName, operationId, subscriptionId` | Get video analyzer operation status. |
