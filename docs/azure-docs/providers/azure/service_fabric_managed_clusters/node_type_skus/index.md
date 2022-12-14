---
title: node_type_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - node_type_skus
  - service_fabric_managed_clusters
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
<tr><td><b>Name</b></td><td><code>node_type_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.node_type_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `capacity` | `object` | Provides information about how node type can be scaled. |
| `resourceType` | `string` | The type of resource the sku applies to.  &lt;br /&gt;&lt;br /&gt;Value: Microsoft.ServiceFabric/managedClusters/nodeTypes. |
| `sku` | `object` | Describes a node type supported sku. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `NodeTypeSkus_List` | `SELECT` | `api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId` |
