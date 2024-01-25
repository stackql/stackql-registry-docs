---
title: alert_operation
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_operation
  - authorization
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
<tr><td><b>Name</b></td><td><code>alert_operation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.alert_operation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of the alert operation. |
| `createdDateTime` | `string` | The created date of the alert operation. |
| `lastActionDateTime` | `string` | The last action date of the alert operation. |
| `resourceLocation` | `string` | The location of the alert associated with the operation. |
| `status` | `string` | The status of the alert operation. |
| `statusDetail` | `string` | The status detail of the alert operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `operationId, scope` |
