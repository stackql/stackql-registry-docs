---
title: blockchain_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - blockchain_nodes
  - blockchainnodeengine
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
<tr><td><b>Name</b></td><td><code>blockchain_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.blockchainnodeengine.blockchain_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `blockchainNodes` | `array` | The list of nodes |
| `nextPageToken` | `string` | A token identifying a page of results the server should return. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blockchainNodesId, locationsId, projectsId` | Gets details of a single blockchain node. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists blockchain nodes in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new blockchain node in a given project and location. |
| `delete` | `DELETE` | `blockchainNodesId, locationsId, projectsId` | Deletes a single blockchain node. |
| `patch` | `EXEC` | `blockchainNodesId, locationsId, projectsId` | Updates the parameters of a single blockchain node. |
