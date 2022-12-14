---
title: nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes
  - sasportal
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.sasportal.nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A pagination token returned from a previous call to ListNodes that indicates from where listing should continue. If the field is missing or empty, it means there is no more nodes. |
| `nodes` | `array` | The nodes that match the request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_nodes_list` | `SELECT` | `customersId` | Lists nodes. |
| `customers_nodes_nodes_list` | `SELECT` | `customersId, nodesId` | Lists nodes. |
| `get` | `SELECT` | `nodesId` | Returns a requested node. |
| `nodes_list` | `SELECT` | `nodesId` | Lists nodes. |
| `nodes_nodes_list` | `SELECT` | `nodesId, nodesId1` | Lists nodes. |
| `customers_nodes_create` | `INSERT` | `customersId` | Creates a new node. |
| `customers_nodes_nodes_create` | `INSERT` | `customersId, nodesId` | Creates a new node. |
| `nodes_create` | `INSERT` | `nodesId` | Creates a new node. |
| `nodes_nodes_create` | `INSERT` | `nodesId, nodesId1` | Creates a new node. |
| `customers_nodes_delete` | `DELETE` | `customersId, nodesId` | Deletes a node. |
| `nodes_delete` | `DELETE` | `nodesId, nodesId1` | Deletes a node. |
| `customers_nodes_get` | `EXEC` | `customersId, nodesId` | Returns a requested node. |
| `customers_nodes_move` | `EXEC` | `customersId, nodesId` | Moves a node under another node or customer. |
| `customers_nodes_patch` | `EXEC` | `customersId, nodesId` | Updates an existing node. |
| `nodes_get` | `EXEC` | `nodesId, nodesId1` | Returns a requested node. |
| `nodes_move` | `EXEC` | `nodesId, nodesId1` | Moves a node under another node or customer. |
| `nodes_patch` | `EXEC` | `nodesId, nodesId1` | Updates an existing node. |
