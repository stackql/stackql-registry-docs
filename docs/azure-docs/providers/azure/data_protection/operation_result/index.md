---
title: operation_result
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_result
  - data_protection
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
<tr><td><b>Name</b></td><td><code>operation_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.operation_result</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `jobId` | `string` | Arm Id of the job created for this operation. |
| `objectType` | `string` | This property will be used as the discriminator for deciding the specific types in the polymorphic chain of types. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OperationResult_Get` | `SELECT` | `api-version, location, operationId, subscriptionId` |
