---
title: registries
hide_title: false
hide_table_of_contents: false
keywords:
  - registries
  - container_registry
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
<tr><td><b>Name</b></td><td><code>registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.registries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `identity` | `object` | Managed identity for the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
| `type` | `string` | The type of the resource. |
| `tags` | `object` | The tags of the resource. |
| `properties` | `object` | The properties of a container registry. |
| `sku` | `object` | The SKU of a container registry. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Registries_Get` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Gets the properties of the specified container registry. |
| `Registries_List` | `SELECT` | `subscriptionId` | Lists all the container registries under the specified subscription. |
| `Registries_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the container registries under the specified resource group. |
| `Registries_Create` | `INSERT` | `registryName, resourceGroupName, subscriptionId, data__sku` | Creates a container registry with the specified parameters. |
| `Registries_Delete` | `DELETE` | `registryName, resourceGroupName, subscriptionId` | Deletes a container registry. |
| `Registries_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks whether the container registry name is available for use. The name must contain only alphanumeric characters, be globally unique, and between 5 and 50 characters in length. |
| `Registries_GenerateCredentials` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Generate keys for a token of a specified container registry. |
| `Registries_GetBuildSourceUploadUrl` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Get the upload location for the user to be able to upload the source. |
| `Registries_GetPrivateLinkResource` | `EXEC` | `groupName, registryName, resourceGroupName, subscriptionId` | Gets a private link resource by a specified group name for a container registry. |
| `Registries_ImportImage` | `EXEC` | `registryName, resourceGroupName, subscriptionId, data__source` | Copies an image to this container registry from the specified container registry. |
| `Registries_ListCredentials` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Lists the login credentials for the specified container registry. |
| `Registries_ListPrivateLinkResources` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Lists the private link resources for a container registry. |
| `Registries_ListUsages` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Gets the quota usages for the specified container registry. |
| `Registries_RegenerateCredential` | `EXEC` | `registryName, resourceGroupName, subscriptionId, data__name` | Regenerates one of the login credentials for the specified container registry. |
| `Registries_ScheduleRun` | `EXEC` | `registryName, resourceGroupName, subscriptionId, data__type` | Schedules a new run based on the request parameters and add it to the run queue. |
| `Registries_Update` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Updates a container registry with the specified parameters. |
