---
title: operation_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_statuses
  - recommendations_service
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
<tr><td><b>Id</b></td><td><code>azure_extras.recommendations_service.operation_statuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified ID for the async operation. |
| `name` | `string` | Name of the async operation. |
| `operations` | `array` | The operations list. |
| `percentComplete` | `number` | Percent of the operation that is complete. |
| `startTime` | `string` | The start time of the operation. |
| `status` | `string` | Operation status. |
| `endTime` | `string` | The end time of the operation. |
| `error` | `object` | The error detail. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationStatuses_Get` | `SELECT` | `location, operationId` |
