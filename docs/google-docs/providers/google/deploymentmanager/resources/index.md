---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - deploymentmanager
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
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.deploymentmanager.resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | Output only. The name of the resource as it appears in the YAML config. |
| `accessControl` | `object` | The access controls set on the resource. |
| `update` | `object` |  |
| `properties` | `string` | Output only. The current properties of the resource before any references have been filled in. Returned as serialized YAML. |
| `url` | `string` | Output only. The URL of the actual resource. |
| `manifest` | `string` | Output only. URL of the manifest representing the current configuration of this resource. |
| `finalProperties` | `string` | Output only. The evaluated properties of the resource with references expanded. Returned as serialized YAML. |
| `insertTime` | `string` | Output only. Creation timestamp in RFC3339 text format. |
| `type` | `string` | Output only. The type of the resource, for example `compute.v1.instance`, or `cloudfunctions.v1beta1.function`. |
| `updateTime` | `string` | Output only. Update timestamp in RFC3339 text format. |
| `warnings` | `array` | Output only. If warning messages are generated during processing of this resource, this field will be populated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deployment, project, resource` | Gets information about a single resource. |
| `list` | `SELECT` | `deployment, project` | Lists all resources in a given deployment. |
