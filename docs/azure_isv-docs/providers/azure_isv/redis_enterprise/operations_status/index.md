---
title: operations_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_status
  - redis_enterprise
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.redis_enterprise.operations_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The operation's unique id. |
| `name` | `string` | The operation's name. |
| `endTime` | `string` | The end time of the operation. |
| `error` | `object` | Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.). |
| `startTime` | `string` | The start time of the operation. |
| `status` | `string` | The current status of the operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `location, operationId, subscriptionId` |
