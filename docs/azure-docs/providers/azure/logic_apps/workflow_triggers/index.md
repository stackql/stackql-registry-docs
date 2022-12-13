---
title: workflow_triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_triggers
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
<tr><td><b>Name</b></td><td><code>workflow_triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.workflow_triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the workflow trigger name. |
| `properties` | `object` | The workflow trigger properties. |
| `type` | `string` | Gets the workflow trigger type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkflowTriggers_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, triggerName, workflowName` | Gets a workflow trigger. |
| `WorkflowTriggers_List` | `SELECT` | `api-version, resourceGroupName, subscriptionId, workflowName` | Gets a list of workflow triggers. |
| `WorkflowTriggers_GetSchemaJson` | `EXEC` | `api-version, resourceGroupName, subscriptionId, triggerName, workflowName` | Get the trigger schema as JSON. |
| `WorkflowTriggers_ListCallbackUrl` | `EXEC` | `api-version, resourceGroupName, subscriptionId, triggerName, workflowName` | Get the callback URL for a workflow trigger. |
| `WorkflowTriggers_Reset` | `EXEC` | `api-version, resourceGroupName, subscriptionId, triggerName, workflowName` | Resets a workflow trigger. |
| `WorkflowTriggers_Run` | `EXEC` | `api-version, resourceGroupName, subscriptionId, triggerName, workflowName` | Runs a workflow trigger. |
| `WorkflowTriggers_SetState` | `EXEC` | `api-version, resourceGroupName, subscriptionId, triggerName, workflowName, data__source` | Sets the state of a workflow trigger. |
