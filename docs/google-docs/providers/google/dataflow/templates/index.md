---
title: templates
hide_title: false
hide_table_of_contents: false
keywords:
  - templates
  - dataflow
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
<tr><td><b>Name</b></td><td><code>templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataflow.templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `templateType` | `string` | Template Type. |
| `metadata` | `object` | Metadata describing a template. |
| `runtimeMetadata` | `object` | RuntimeMetadata describing a runtime environment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_templates_get` | `SELECT` | `location, projectId` | Get the template associated with a template. |
| `projects_templates_get` | `SELECT` | `projectId` | Get the template associated with a template. |
| `projects_locations_templates_create` | `INSERT` | `location, projectId` | Creates a Cloud Dataflow job from a template. Do not enter confidential information when you supply string values using the API. |
| `projects_templates_create` | `INSERT` | `projectId` | Creates a Cloud Dataflow job from a template. Do not enter confidential information when you supply string values using the API. |
| `projects_locations_templates_launch` | `EXEC` | `location, projectId` | Launch a template. |
| `projects_templates_launch` | `EXEC` | `projectId` | Launch a template. |
