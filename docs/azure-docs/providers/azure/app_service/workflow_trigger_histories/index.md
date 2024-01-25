---
title: workflow_trigger_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_trigger_histories
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
<tr><td><b>Name</b></td><td><code>workflow_trigger_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.workflow_trigger_histories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the workflow trigger history name. |
| `properties` | `object` | The workflow trigger history properties. |
| `type` | `string` | Gets the workflow trigger history type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `historyName, name, resourceGroupName, subscriptionId, triggerName, workflowName` | Gets a workflow trigger history. |
| `list` | `SELECT` | `name, resourceGroupName, subscriptionId, triggerName, workflowName` | Gets a list of workflow trigger histories. |
| `_list` | `EXEC` | `name, resourceGroupName, subscriptionId, triggerName, workflowName` | Gets a list of workflow trigger histories. |
| `resubmit` | `EXEC` | `historyName, name, resourceGroupName, subscriptionId, triggerName, workflowName` | Resubmits a workflow run based on the trigger history. |
