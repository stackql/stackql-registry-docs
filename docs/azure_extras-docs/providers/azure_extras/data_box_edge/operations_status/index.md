---
title: operations_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_status
  - data_box_edge
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
<tr><td><b>Name</b></td><td><code>operations_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.operations_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `properties` | `object` | The properties for the job. |
| `startTime` | `string` | The UTC date and time at which the job started. |
| `error` | `object` | The job error information containing the list of job errors. |
| `percentComplete` | `integer` | The percentage of the job that is complete. |
| `status` | `string` | The current status of the job. |
| `endTime` | `string` | The UTC date and time at which the job completed. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationsStatus_Get` | `SELECT` | `deviceName, name, resourceGroupName, subscriptionId` |
