---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - power_platform
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
<tr><td><b>Id</b></td><td><code>azure.power_platform.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the PrivateEndpointConnectProperties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnections_Get` | `SELECT` | `enterprisePolicyName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets a private endpoint connection. |
| `PrivateEndpointConnections_ListByEnterprisePolicy` | `SELECT` | `enterprisePolicyName, resourceGroupName, subscriptionId` | List all private endpoint connections on an EnterprisePolicy. |
| `PrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `enterprisePolicyName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Approve or reject a private endpoint connection with a given name. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `enterprisePolicyName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes a private endpoint connection with a given name. |
