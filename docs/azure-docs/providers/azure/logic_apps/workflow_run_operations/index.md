---
title: workflow_run_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_operations
  - logic_apps
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
<tr><td><b>Name</b></td><td><code>workflow_run_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.workflow_run_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the workflow run name. |
| `type` | `string` | Gets the workflow run type. |
| `properties` | `object` | The workflow run properties. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `WorkflowRunOperations_Get` | `SELECT` | `api-version, operationId, resourceGroupName, runName, subscriptionId, workflowName` |
