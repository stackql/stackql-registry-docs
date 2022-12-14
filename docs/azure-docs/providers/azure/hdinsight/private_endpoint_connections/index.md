---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - hdinsight
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
<tr><td><b>Id</b></td><td><code>azure.hdinsight.private_endpoint_connections</code></td></tr>
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
| `PrivateEndpointConnections_Get` | `SELECT` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets the specific private endpoint connection. |
| `PrivateEndpointConnections_ListByCluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Lists the private endpoint connections for a HDInsight cluster. |
| `PrivateEndpointConnections_CreateOrUpdate` | `INSERT` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Approve or reject a private endpoint connection manually. |
| `PrivateEndpointConnections_Delete` | `DELETE` | `clusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes the specific private endpoint connection. |
