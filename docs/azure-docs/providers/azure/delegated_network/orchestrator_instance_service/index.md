---
title: orchestrator_instance_service
hide_title: false
hide_table_of_contents: false
keywords:
  - orchestrator_instance_service
  - delegated_network
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
<tr><td><b>Name</b></td><td><code>orchestrator_instance_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.delegated_network.orchestrator_instance_service</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the resource. |
| `name` | `string` | The name of the resource. |
| `identity` | `object` |  |
| `kind` | `string` | The kind of workbook. Choices are user and shared. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of orchestrator |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the OrchestratorInstances resources in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get all the orchestratorInstance resources in a subscription. |
| `create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create a orchestrator instance |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes the Orchestrator Instance |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get all the OrchestratorInstances resources in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get all the orchestratorInstance resources in a subscription. |
| `patch` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update Orchestrator Instance |
