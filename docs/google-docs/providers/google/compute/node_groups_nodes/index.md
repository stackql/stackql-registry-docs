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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `add_nodes` | `EXEC` | `nodeGroup, project, zone` | Adds specified number of nodes to the node group. |
| `delete_nodes` | `EXEC` | `nodeGroup, project, zone` | Deletes specified nodes from the node group. |
| `list_nodes` | `EXEC` | `nodeGroup, project, zone` | Lists nodes in the node group. |
