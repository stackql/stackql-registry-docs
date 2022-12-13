---
title: hybrid_identity_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_identity_metadata
  - hybrid_aks
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
<tr><td><b>Name</b></td><td><code>hybrid_identity_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_aks.hybrid_identity_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Defines the resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `HybridIdentityMetadata_Get` | `SELECT` | `hybridIdentityMetadataResourceName, provisionedClustersName, resourceGroupName, subscriptionId` | Get the hybrid identity metadata proxy resource. |
| `HybridIdentityMetadata_ListByCluster` | `SELECT` | `provisionedClustersName, resourceGroupName, subscriptionId` | Lists the hybrid identity metadata proxy resource in a cluster. |
| `HybridIdentityMetadata_Delete` | `DELETE` | `hybridIdentityMetadataResourceName, provisionedClustersName, resourceGroupName, subscriptionId` | Deletes the hybrid identity metadata proxy resource. |
| `HybridIdentityMetadata_Put` | `EXEC` | `hybridIdentityMetadataResourceName, provisionedClustersName, resourceGroupName, subscriptionId, data__properties` | Creates the hybrid identity metadata proxy resource that facilitates the managed identity provisioning. |
