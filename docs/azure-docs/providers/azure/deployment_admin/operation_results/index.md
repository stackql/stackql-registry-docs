---
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - deployment_admin
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
<tr><td><b>Name</b></td><td><code>operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_admin.operation_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `startTime` | `string` | The deployment start time |
| `status` | `string` | Specifies the state of the Operation result. |
| `endTime` | `string` | The deployment end time |
| `percentComplete` | `number` | Percentage completed. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationResults_Get` | `SELECT` | `location, operationResultId, subscriptionId` |
