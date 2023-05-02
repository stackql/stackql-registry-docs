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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `totalResources` | `object` |  |
| `instances` | `array` | Instances scheduled on this node. |
| `serverBinding` | `object` |  |
| `consumedResources` | `object` |  |
| `disks` | `array` | Local disk configurations. |
| `cpuOvercommitType` | `string` | CPU overcommit. |
| `serverId` | `string` | Server ID associated with this node. |
| `instanceConsumptionData` | `array` | Instance data that shows consumed resources on the node. |
| `accelerators` | `array` | Accelerators for this node. |
| `status` | `string` |  |
| `satisfiesPzs` | `boolean` | [Output Only] Reserved for future use. |
| `nodeType` | `string` | The type of this node. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `nodeGroups_listNodes` | `SELECT` | `nodeGroup, project, zone` | Lists nodes in the node group. |
| `nodeGroups_addNodes` | `INSERT` | `nodeGroup, project, zone` | Adds specified number of nodes to the node group. |
| `nodeGroups_deleteNodes` | `DELETE` | `nodeGroup, project, zone` | Deletes specified nodes from the node group. |
