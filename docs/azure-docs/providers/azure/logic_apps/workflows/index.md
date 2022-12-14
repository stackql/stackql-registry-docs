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
| `Workflows_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, workflowName` | Gets a workflow. |
| `Workflows_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets a list of workflows by resource group. |
| `Workflows_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets a list of workflows by subscription. |
| `Workflows_CreateOrUpdate` | `INSERT` | `api-version, resourceGroupName, subscriptionId, workflowName` | Creates or updates a workflow. |
| `Workflows_Delete` | `DELETE` | `api-version, resourceGroupName, subscriptionId, workflowName` | Deletes a workflow. |
| `Workflows_Disable` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Disables a workflow. |
| `Workflows_Enable` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Enables a workflow. |
| `Workflows_GenerateUpgradedDefinition` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Generates the upgraded definition for a workflow. |
| `Workflows_ListCallbackUrl` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Get the workflow callback Url. |
| `Workflows_ListSwagger` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Gets an OpenAPI definition for the workflow. |
| `Workflows_Move` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Moves an existing workflow. |
| `Workflows_RegenerateAccessKey` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Regenerates the callback URL access key for request triggers. |
| `Workflows_Update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Updates a workflow. |
| `Workflows_ValidateByLocation` | `EXEC` | `api-version, location, resourceGroupName, subscriptionId, workflowName` | Validates the workflow definition. |
| `Workflows_ValidateByResourceGroup` | `EXEC` | `api-version, resourceGroupName, subscriptionId, workflowName` | Validates the workflow. |
