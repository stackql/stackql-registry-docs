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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#diskType for disk types. |
| `deprecated` | `object` | Deprecation status for a public resource. |
| `region` | `string` | [Output Only] URL of the region where the disk type resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `zone` | `string` | [Output Only] URL of the zone where the disk type resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `defaultDiskSizeGb` | `string` | [Output Only] Server-defined default disk size in GB. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `validDiskSize` | `string` | [Output Only] An optional textual description of the valid disk size, such as "10GB-10TB". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `aggregated_list` | `SELECT` | `project` | Retrieves an aggregated list of disk types. |
| `get` | `SELECT` | `diskType, project, zone` | Returns the specified disk type. |
| `list` | `SELECT` | `project, zone` | Retrieves a list of disk types available to the specified project. |
| `_aggregated_list` | `EXEC` | `project` | Retrieves an aggregated list of disk types. |
