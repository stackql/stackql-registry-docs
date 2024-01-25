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
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `identity` | `object` | Managed identity for the resource. |
| `properties` | `object` | The properties of a container registry. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Gets the properties of the specified container registry. |
| `list` | `SELECT` | `subscriptionId` | Lists all the container registries under the specified subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the container registries under the specified resource group. |
| `create` | `INSERT` | `registryName, resourceGroupName, subscriptionId, data__sku` | Creates a container registry with the specified parameters. |
| `delete` | `DELETE` | `registryName, resourceGroupName, subscriptionId` | Deletes a container registry. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the container registries under the specified subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the container registries under the specified resource group. |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks whether the container registry name is available for use. The name must contain only alphanumeric characters, be globally unique, and between 5 and 50 characters in length. |
| `generate_credentials` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Generate keys for a token of a specified container registry. |
| `import_image` | `EXEC` | `registryName, resourceGroupName, subscriptionId, data__source` | Copies an image to this container registry from the specified container registry. |
| `regenerate_credential` | `EXEC` | `registryName, resourceGroupName, subscriptionId, data__name` | Regenerates one of the login credentials for the specified container registry. |
| `schedule_run` | `EXEC` | `registryName, resourceGroupName, subscriptionId, data__type` | Schedules a new run based on the request parameters and add it to the run queue. |
| `update` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Updates a container registry with the specified parameters. |
