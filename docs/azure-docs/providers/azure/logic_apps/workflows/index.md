---
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
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
<tr><td><b>Name</b></td><td><code>workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.workflows</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `identity` | `object` | Managed service identity properties. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The workflow properties. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, workflowName` | Gets a workflow. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets a list of workflows by resource group. |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | Gets a list of workflows by subscription. |
| `create_or_update` | `INSERT` | `api-version, resourceGroupName, subscriptionId, workflowName` | Creates or updates a workflow. |
| `delete` | `DELETE` | `api-version, resourceGroupName, subscriptionId, workflowName` | Deletes a workflow. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Gets a list of workflows by resource group. |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | Gets a list of workflows by subscription. |
| `disable` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Disables a workflow. |
| `enable` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Enables a workflow. |
| `generate_upgraded_definition` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Generates the upgraded definition for a workflow. |
| `move` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Moves an existing workflow. |
| `regenerate_access_key` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Regenerates the callback URL access key for request triggers. |
| `update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Updates a workflow. |
| `validate_by_location` | `EXEC` | `api-version, location, resourceGroupName, subscriptionId, workflowName` | Validates the workflow definition. |
| `validate_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Validates the workflow. |
