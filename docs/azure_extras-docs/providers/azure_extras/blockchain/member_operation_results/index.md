---
title: member_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - member_operation_results
  - blockchain
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
<tr><td><b>Name</b></td><td><code>member_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.blockchain.member_operation_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Gets or sets the operation name. |
| `startTime` | `string` | Gets or sets the operation start time. |
| `endTime` | `string` | Gets or sets the operation end time. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `BlockchainMemberOperationResults_Get` | `SELECT` | `locationName, operationId, subscriptionId` |
