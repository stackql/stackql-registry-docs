---
title: workflow_run_action_scope_repetitions
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_action_scope_repetitions
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
<tr><td><b>Name</b></td><td><code>workflow_run_action_scope_repetitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.workflow_run_action_scope_repetitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The workflow run action repetition properties definition. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `actionName, api-version, repetitionName, resourceGroupName, runName, subscriptionId, workflowName` | Get a workflow run action scoped repetition. |
| `list` | `SELECT` | `actionName, api-version, resourceGroupName, runName, subscriptionId, workflowName` | List the workflow run action scoped repetitions. |
| `_list` | `EXEC` | `actionName, api-version, resourceGroupName, runName, subscriptionId, workflowName` | List the workflow run action scoped repetitions. |
