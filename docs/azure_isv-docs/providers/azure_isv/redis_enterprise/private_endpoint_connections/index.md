---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - redis_enterprise
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.redis_enterprise.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets the specified private endpoint connection associated with the RedisEnterprise cluster. |
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Lists all the private endpoint connections associated with the RedisEnterprise cluster. |
| `delete` | `DELETE` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes the specified private endpoint connection associated with the RedisEnterprise cluster. |
| `_list` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Lists all the private endpoint connections associated with the RedisEnterprise cluster. |
| `put` | `EXEC` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Updates the state of the specified private endpoint connection associated with the RedisEnterprise cluster. |
