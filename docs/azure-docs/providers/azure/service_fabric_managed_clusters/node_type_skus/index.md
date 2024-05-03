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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_type_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.node_type_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | Provides information about how node type can be scaled. |
| <CopyableCode code="resourceType" /> | `string` | The type of resource the sku applies to.  &lt;br /&gt;&lt;br /&gt;Value: Microsoft.ServiceFabric/managedClusters/nodeTypes. |
| <CopyableCode code="sku" /> | `object` | Describes a node type supported sku. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> |
