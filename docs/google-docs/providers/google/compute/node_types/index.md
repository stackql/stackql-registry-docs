---
title: node_types
hide_title: false
hide_table_of_contents: false
keywords:
  - node_types
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
<tr><td><b>Name</b></td><td><code>node_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.node_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | [Output Only] Name of the resource. |
| `description` | `string` | [Output Only] An optional textual description of the resource. |
| `guestCpus` | `integer` | [Output Only] The number of virtual CPUs that are available to the node type. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `deprecated` | `object` | Deprecation status for a public resource. |
| `localSsdGb` | `integer` | [Output Only] Local SSD available to the node type, defined in GB. |
| `memoryMb` | `integer` | [Output Only] The amount of physical memory available to the node type, defined in MB. |
| `zone` | `string` | [Output Only] The name of the zone where the node type resides, such as us-central1-a. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `kind` | `string` | [Output Only] The type of the resource. Always compute#nodeType for node types. |
| `cpuPlatform` | `string` | [Output Only] The CPU platform used by this node type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `aggregated_list` | `SELECT` | `project` | Retrieves an aggregated list of node types. |
| `get` | `SELECT` | `nodeType, project, zone` | Returns the specified node type. |
| `list` | `SELECT` | `project, zone` | Retrieves a list of node types available to the specified project. |
| `_aggregated_list` | `EXEC` | `project` | Retrieves an aggregated list of node types. |
