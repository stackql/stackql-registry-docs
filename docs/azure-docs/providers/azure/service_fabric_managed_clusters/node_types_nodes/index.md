---
title: node_types_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - node_types_nodes
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

Creates, updates, deletes, gets or lists a <code>node_types_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_types_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.node_types_nodes" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, nodeTypeName, resourceGroupName, subscriptionId" /> | Deletes one or more nodes on the node type. It will disable the fabric nodes, trigger a delete on the VMs and removes the state from the cluster. |

## `DELETE` example

Deletes the specified <code>node_types_nodes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_fabric_managed_clusters.node_types_nodes
WHERE clusterName = '{{ clusterName }}'
AND nodeTypeName = '{{ nodeTypeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
