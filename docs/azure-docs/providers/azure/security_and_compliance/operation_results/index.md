---
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - security_and_compliance
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
<tr><td><b>Id</b></td><td><code>azure.security_and_compliance.operation_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the operation returned. |
| `name` | `string` | The name of the operation result. |
| `status` | `string` | The status of the operation being performed. |
| `properties` | `` | Additional properties of the operation result. |
| `startTime` | `string` | The time that the operation was started. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationResults_Get` | `SELECT` | `locationName, operationResultId, subscriptionId` |
