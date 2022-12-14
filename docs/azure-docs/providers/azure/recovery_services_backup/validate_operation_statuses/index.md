---
title: validate_operation_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - validate_operation_statuses
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>validate_operation_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.validate_operation_statuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the operation. |
| `name` | `string` | Name of the operation. |
| `endTime` | `string` | Operation end time. Format: ISO-8601. |
| `error` | `object` | Error information associated with operation status call. |
| `properties` | `object` | Base class for additional information of operation status. |
| `startTime` | `string` | Operation start time. Format: ISO-8601. |
| `status` | `string` | Operation status. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ValidateOperationStatuses_Get` | `SELECT` | `api-version, operationId, resourceGroupName, subscriptionId, vaultName` |
