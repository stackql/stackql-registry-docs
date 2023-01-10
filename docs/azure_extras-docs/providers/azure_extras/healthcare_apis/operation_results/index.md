---
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - healthcare_apis
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
<tr><td><b>Name</b></td><td><code>operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare_apis.operation_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the operation returned. |
| `name` | `string` | The name of the operation result. |
| `properties` | `object` | Additional properties of the operation result. |
| `startTime` | `string` | The time that the operation was started. |
| `status` | `string` | The status of the operation being performed. |
| `endTime` | `string` | The time that the operation finished. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationResults_Get` | `SELECT` | `api-version, locationName, operationResultId, subscriptionId` |
