---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `location` | `string` | Specifies the location of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_Get` | `SELECT` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Gets the specified private endpoint connection associated with the workspace. |
| `PrivateEndpointConnections_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List all the private endpoint connections associated with the workspace. |
| `PrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Update the state of specified private endpoint connection associated with the workspace. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName` | Deletes the specified private endpoint connection associated with the workspace. |
