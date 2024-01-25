---
title: workflow_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_runs
  - app_service
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
<tr><td><b>Name</b></td><td><code>workflow_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.workflow_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the workflow run name. |
| `properties` | `object` | The workflow run properties. |
| `type` | `string` | Gets the workflow run type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, runName, subscriptionId, workflowName` | Gets a workflow run. |
| `list` | `SELECT` | `name, resourceGroupName, subscriptionId, workflowName` | Gets a list of workflow runs. |
| `_list` | `EXEC` | `name, resourceGroupName, subscriptionId, workflowName` | Gets a list of workflow runs. |
| `cancel` | `EXEC` | `name, resourceGroupName, runName, subscriptionId, workflowName` | Cancels a workflow run. |
