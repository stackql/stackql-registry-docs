---
title: workflow_run_action_repetitions_request_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_action_repetitions_request_histories
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
<tr><td><b>Name</b></td><td><code>workflow_run_action_repetitions_request_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.workflow_run_action_repetitions_request_histories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The request history. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `actionName, name, repetitionName, requestHistoryName, resourceGroupName, runName, subscriptionId, workflowName` | Gets a workflow run repetition request history. |
| `list` | `SELECT` | `actionName, name, repetitionName, resourceGroupName, runName, subscriptionId, workflowName` | List a workflow run repetition request history. |
| `_list` | `EXEC` | `actionName, name, repetitionName, resourceGroupName, runName, subscriptionId, workflowName` | List a workflow run repetition request history. |
