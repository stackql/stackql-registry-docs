---
title: cloud_hsm_cluster_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_hsm_cluster_private_endpoint_connections
  - hardware_security_modules
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
<tr><td><b>Name</b></td><td><code>cloud_hsm_cluster_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hardware_security_modules.cloud_hsm_cluster_private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the private endpoint connection. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cloudHsmClusterName, peConnectionName, resourceGroupName, subscriptionId` | Gets the private endpoint connection for the Cloud Hsm Cluster. |
| `create` | `INSERT` | `cloudHsmClusterName, peConnectionName, resourceGroupName, subscriptionId` | Creates or updates the private endpoint connection for the Cloud Hsm Cluster. |
| `delete` | `DELETE` | `cloudHsmClusterName, peConnectionName, resourceGroupName, subscriptionId` | Deletes the private endpoint connection for the Cloud Hsm Cluster. |
