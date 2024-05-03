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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.workflows" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="identity" /> | `object` | Managed service identity properties. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The workflow properties. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Gets a workflow. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets a list of workflows by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Gets a list of workflows by subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Creates or updates a workflow. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Deletes a workflow. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets a list of workflows by resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Gets a list of workflows by subscription. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Disables a workflow. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Enables a workflow. |
| <CopyableCode code="generate_upgraded_definition" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Generates the upgraded definition for a workflow. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Moves an existing workflow. |
| <CopyableCode code="regenerate_access_key" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Regenerates the callback URL access key for request triggers. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Updates a workflow. |
| <CopyableCode code="validate_by_location" /> | `EXEC` | <CopyableCode code="api-version, location, resourceGroupName, subscriptionId, workflowName" /> | Validates the workflow definition. |
| <CopyableCode code="validate_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Validates the workflow. |
