---
title: export_jobs_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - export_jobs_operation_results
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
<tr><td><b>Name</b></td><td><code>export_jobs_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.export_jobs_operation_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `operation` | `object` | Base class for operation result info. |
| `statusCode` | `string` | HTTP Status Code of the operation. |
| `headers` | `object` | HTTP headers associated with this operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ExportJobsOperationResults_Get` | `SELECT` | `api-version, operationId, resourceGroupName, subscriptionId, vaultName` |
