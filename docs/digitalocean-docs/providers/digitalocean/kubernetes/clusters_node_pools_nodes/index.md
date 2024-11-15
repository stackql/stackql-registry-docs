---
title: clusters_node_pools_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_node_pools_nodes
  - kubernetes
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>clusters_node_pools_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_node_pools_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.kubernetes.clusters_node_pools_nodes" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="kubernetes_delete_node" /> | `DELETE` | <CopyableCode code="cluster_id, node_id, node_pool_id" /> | To delete a single node in a pool, send a DELETE request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID/nodes/$NODE_ID`. Appending the `skip_drain=1` query parameter to the request causes node draining to be skipped. Omitting the query parameter or setting its value to `0` carries out draining prior to deletion. Appending the `replace=1` query parameter to the request causes the node to be replaced by a new one after deletion. Omitting the query parameter or setting its value to `0` deletes without replacement. |

## `DELETE` example

Deletes the specified <code>clusters_node_pools_nodes</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.kubernetes.clusters_node_pools_nodes
WHERE cluster_id = '{{ cluster_id }}'
AND node_id = '{{ node_id }}'
AND node_pool_id = '{{ node_pool_id }}';
```
