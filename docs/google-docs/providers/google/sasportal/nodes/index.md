---
title: nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes
  - sasportal
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
<tr><td><b>Name</b></td><td><code>nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sasportal.nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name. |
| `sasUserIds` | `array` | User ids used by the devices belonging to this node. |
| `displayName` | `string` | The node's display name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `nodes_nodes_list` | `SELECT` | `nodesId` | Lists nodes. |
| `nodes_nodes_nodes_list` | `SELECT` | `nodesId, nodesId1` | Lists nodes. |
| `nodes_nodes_create` | `INSERT` | `nodesId` | Creates a new node. |
| `nodes_nodes_nodes_create` | `INSERT` | `nodesId, nodesId1` | Creates a new node. |
| `nodes_nodes_delete` | `DELETE` | `nodesId, nodesId1` | Deletes a node. |
| `_nodes_nodes_list` | `EXEC` | `nodesId` | Lists nodes. |
| `_nodes_nodes_nodes_list` | `EXEC` | `nodesId, nodesId1` | Lists nodes. |
| `customers_nodes_move` | `EXEC` | `customersId, nodesId` | Moves a node under another node or customer. |
| `customers_nodes_patch` | `EXEC` | `customersId, nodesId` | Updates an existing node. |
| `nodes_nodes_move` | `EXEC` | `nodesId, nodesId1` | Moves a node under another node or customer. |
| `nodes_nodes_patch` | `EXEC` | `nodesId, nodesId1` | Updates an existing node. |
