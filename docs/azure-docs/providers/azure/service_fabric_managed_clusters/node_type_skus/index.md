---
title: node_type_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - node_type_skus
  - service_fabric_managed_clusters
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>node_type_skus</code> resource.

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
| <CopyableCode code="resourceType" /> | `string` | The type of resource the sku applies to.    Value: Microsoft.ServiceFabric/managedClusters/nodeTypes. |
| <CopyableCode code="sku" /> | `object` | Describes a node type supported sku. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Get a Service Fabric node type supported SKUs. |

## `SELECT` examples

Get a Service Fabric node type supported SKUs.


```sql
SELECT
capacity,
resourceType,
sku
FROM azure.service_fabric_managed_clusters.node_type_skus
WHERE clusterName = '{{ clusterName }}'
AND nodeTypeName = '{{ nodeTypeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```