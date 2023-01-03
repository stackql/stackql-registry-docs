---
title: disk_types
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_types
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
<tr><td><b>Name</b></td><td><code>disk_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.disk_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | [Output Only] Name of the resource. |
| `description` | `string` | [Output Only] An optional description of this resource. |
| `validDiskSize` | `string` | [Output Only] An optional textual description of the valid disk size, such as "10GB-10TB". |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#diskType for disk types. |
| `region` | `string` | [Output Only] URL of the region where the disk type resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `defaultDiskSizeGb` | `string` | [Output Only] Server-defined default disk size in GB. |
| `deprecated` | `object` | Deprecation status for a public resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `zone` | `string` | [Output Only] URL of the zone where the disk type resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `diskTypes_aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of disk types. |
| `diskTypes_get` | `SELECT` | `diskType, project, zone` | Returns the specified disk type. Gets a list of available disk types by making a list() request. |
| `diskTypes_list` | `SELECT` | `project, zone` | Retrieves a list of disk types available to the specified project. |
