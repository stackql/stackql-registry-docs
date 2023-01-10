---
title: operations_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_results
  - orbital
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
<tr><td><b>Name</b></td><td><code>operations_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.orbital.operations_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `status` | `string` | The status of operation. |
| `endTime` | `string` | The operation end time (ISO 8601 UTC standard). |
| `error` | `object` | Operation result error properties. |
| `percentComplete` | `number` | Percentage completed. |
| `properties` | `object` | Operation result properties. |
| `startTime` | `string` | The operation start time (ISO 8601 UTC standard). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationsResults_Get` | `SELECT` | `location, operationId, subscriptionId` |
