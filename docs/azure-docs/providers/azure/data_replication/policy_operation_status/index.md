---
title: policy_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_operation_status
  - data_replication
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
<tr><td><b>Name</b></td><td><code>policy_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_replication.policy_operation_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id. |
| `name` | `string` | Gets or sets the operation name. |
| `endTime` | `string` | Gets or sets the end time. |
| `startTime` | `string` | Gets or sets the start time. |
| `status` | `string` | Gets or sets the status of the operation. ARM expects the terminal status to be one of<br />Succeeded/ Failed/ Canceled. All other values imply that the operation is still running. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `operationId, policyName, resourceGroupName, subscriptionId, vaultName` |
