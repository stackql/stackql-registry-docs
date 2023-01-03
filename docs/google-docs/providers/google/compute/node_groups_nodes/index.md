---
title: node_groups_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - node_groups_nodes
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_groups_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.node_groups_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the node. |
| `nodeType` | `string` | The type of this node. |
| `disks` | `array` | Local disk configurations. |
| `serverBinding` | `object` |  |
| `status` | `string` |  |
| `satisfiesPzs` | `boolean` | [Output Only] Reserved for future use. |
| `cpuOvercommitType` | `string` | CPU overcommit. |
| `instances` | `array` | Instances scheduled on this node. |
| `serverId` | `string` | Server ID associated with this node. |
| `accelerators` | `array` | Accelerators for this node. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `nodeGroups_listNodes` | `SELECT` | `nodeGroup, project, zone` | Lists nodes in the node group. |
| `nodeGroups_addNodes` | `INSERT` | `nodeGroup, project, zone` | Adds specified number of nodes to the node group. |
| `nodeGroups_deleteNodes` | `DELETE` | `nodeGroup, project, zone` | Deletes specified nodes from the node group. |
