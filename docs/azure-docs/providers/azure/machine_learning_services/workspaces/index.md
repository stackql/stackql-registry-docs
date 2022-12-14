---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - machine_learning_services
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
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `properties` | `object` | The properties of a machine learning workspace. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `location` | `string` | Specifies the location of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Workspaces_Get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets the properties of the specified machine learning workspace. |
| `Workspaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the available machine learning workspaces under the specified resource group. |
| `Workspaces_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the available machine learning workspaces under the specified subscription. |
| `Workspaces_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Creates or updates a workspace with the specified parameters. |
| `Workspaces_Delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes a machine learning workspace. |
| `Workspaces_Diagnose` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |  |
| `Workspaces_ListKeys` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Lists all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry |
| `Workspaces_ListNotebookAccessToken` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | return notebook access token and refresh token |
| `Workspaces_ListNotebookKeys` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | List keys of a notebook. |
| `Workspaces_ListOutboundNetworkDependenciesEndpoints` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |  |
| `Workspaces_ListStorageAccountKeys` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | List storage account keys of a workspace. |
| `Workspaces_PrepareNotebook` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Prepare a notebook. |
| `Workspaces_ResyncKeys` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Resync all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry |
| `Workspaces_Update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Updates a machine learning workspace with the specified parameters. |
