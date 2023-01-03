---
title: accelerator_types
hide_title: false
hide_table_of_contents: false
keywords:
  - accelerator_types
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
<tr><td><b>Name</b></td><td><code>accelerator_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.accelerator_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | [Output Only] Name of the resource. |
| `description` | `string` | [Output Only] An optional textual description of the resource. |
| `maximumCardsPerInstance` | `integer` | [Output Only] Maximum number of accelerator cards allowed per instance. |
| `selfLink` | `string` | [Output Only] Server-defined, fully qualified URL for this resource. |
| `deprecated` | `object` | Deprecation status for a public resource. |
| `zone` | `string` | [Output Only] The name of the zone where the accelerator type resides, such as us-central1-a. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `kind` | `string` | [Output Only] The type of the resource. Always compute#acceleratorType for accelerator types. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `acceleratorTypes_aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of accelerator types. |
| `acceleratorTypes_get` | `SELECT` | `acceleratorType, project, zone` | Returns the specified accelerator type. |
| `acceleratorTypes_list` | `SELECT` | `project, zone` | Retrieves a list of accelerator types that are available to the specified project. |
