---
title: node
hide_title: false
hide_table_of_contents: false
keywords:
  - node
  - prod_tt_sasportal
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
<tr><td><b>Name</b></td><td><code>node</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.prod_tt_sasportal.node</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name. |
| `displayName` | `string` | The node's display name. |
| `sasUserIds` | `array` | User ids used by the devices belonging to this node. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `nodes_get` | `SELECT` | `nodesId` |
| `nodes_nodes_get` | `SELECT` | `nodesId, nodesId1` |
