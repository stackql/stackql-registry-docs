---
title: operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status
  - service_fabric_managed_clusters
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
<tr><td><b>Name</b></td><td><code>operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.operation_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the operation. |
| `percentComplete` | `number` | The completion percentage of the operation. |
| `startTime` | `string` | The start time of the operation. |
| `status` | `string` | The status of the operation. |
| `endTime` | `string` | The end time of the operation. |
| `error` | `object` | The error details. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationStatus_Get` | `SELECT` | `api-version, location, operationId, subscriptionId` |
