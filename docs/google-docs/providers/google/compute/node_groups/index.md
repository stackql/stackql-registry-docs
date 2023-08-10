---
title: node_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - node_groups
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
<tr><td><b>Name</b></td><td><code>node_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.node_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `size` | `integer` | [Output Only] The total number of nodes in the node group. |
| `nodeTemplate` | `string` | URL of the node template to create the node group from. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `locationHint` | `string` | An opaque location hint used to place the Node close to other resources. This field is for use by internal tools that use the public API. The location hint here on the NodeGroup overrides any location_hint present in the NodeTemplate. |
| `fingerprint` | `string` |  |
| `autoscalingPolicy` | `object` |  |
| `maintenanceWindow` | `object` | Time window specified for daily maintenance operations. GCE's internal maintenance will be performed within this window. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `status` | `string` |  |
| `maintenancePolicy` | `string` | Specifies how to handle instances when a node in the group undergoes maintenance. Set to one of: DEFAULT, RESTART_IN_PLACE, or MIGRATE_WITHIN_NODE_GROUP. The default value is DEFAULT. For more information, see Maintenance policies. |
| `zone` | `string` | [Output Only] The name of the zone where the node group resides, such as us-central1-a. |
| `shareSettings` | `object` | The share setting for reservations and sole tenancy node groups. |
| `kind` | `string` | [Output Only] The type of the resource. Always compute#nodeGroup for node group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `nodeGroup, project, zone` | Returns the specified NodeGroup. Get a list of available NodeGroups by making a list() request. Note: the "nodes" field should not be used. Use nodeGroups.listNodes instead. |
| `list` | `SELECT` | `project, zone` | Retrieves a list of node groups available to the specified project. Note: use nodeGroups.listNodes for more details about each group. |
| `insert` | `INSERT` | `initialNodeCount, project, zone` | Creates a NodeGroup resource in the specified project using the data included in the request. |
| `delete` | `DELETE` | `nodeGroup, project, zone` | Deletes the specified NodeGroup resource. |
| `_list` | `EXEC` | `project, zone` | Retrieves a list of node groups available to the specified project. Note: use nodeGroups.listNodes for more details about each group. |
| `aggregated_list` | `EXEC` | `project` | Retrieves an aggregated list of node groups. Note: use nodeGroups.listNodes for more details about each group. |
| `patch` | `EXEC` | `nodeGroup, project, zone` | Updates the specified node group. |
| `set_node_template` | `EXEC` | `nodeGroup, project, zone` | Updates the node template of the node group. |
| `simulate_maintenance_event` | `EXEC` | `nodeGroup, project, zone` | Simulates maintenance event on specified nodes from the node group. |
