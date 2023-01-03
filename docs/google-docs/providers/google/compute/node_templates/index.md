---
title: node_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - node_templates
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
<tr><td><b>Name</b></td><td><code>node_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.node_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `nodeType` | `string` | The node type to use for nodes group that are created from this template. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `accelerators` | `array` |  |
| `statusMessage` | `string` | [Output Only] An optional, human-readable explanation of the status. |
| `nodeAffinityLabels` | `object` | Labels to use for node affinity, which will be used in instance scheduling. |
| `region` | `string` | [Output Only] The name of the region where the node template resides, such as us-central1. |
| `status` | `string` | [Output Only] The status of the node template. One of the following values: CREATING, READY, and DELETING. |
| `cpuOvercommitType` | `string` | CPU overcommit. |
| `disks` | `array` |  |
| `serverBinding` | `object` |  |
| `kind` | `string` | [Output Only] The type of the resource. Always compute#nodeTemplate for node templates. |
| `nodeTypeFlexibility` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `nodeTemplates_aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of node templates. |
| `nodeTemplates_get` | `SELECT` | `nodeTemplate, project, region` | Returns the specified node template. Gets a list of available node templates by making a list() request. |
| `nodeTemplates_list` | `SELECT` | `project, region` | Retrieves a list of node templates available to the specified project. |
| `nodeTemplates_insert` | `INSERT` | `project, region` | Creates a NodeTemplate resource in the specified project using the data included in the request. |
| `nodeTemplates_delete` | `DELETE` | `nodeTemplate, project, region` | Deletes the specified NodeTemplate resource. |
