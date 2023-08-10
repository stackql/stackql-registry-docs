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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `properties` | `string` | Output only. The current properties of the resource before any references have been filled in. Returned as serialized YAML. |
| `accessControl` | `object` | The access controls set on the resource. |
| `url` | `string` | Output only. The URL of the actual resource. |
| `update` | `object` |  |
| `insertTime` | `string` | Output only. Creation timestamp in RFC3339 text format. |
| `finalProperties` | `string` | Output only. The evaluated properties of the resource with references expanded. Returned as serialized YAML. |
| `manifest` | `string` | Output only. URL of the manifest representing the current configuration of this resource. |
| `warnings` | `array` | Output only. If warning messages are generated during processing of this resource, this field will be populated. |
| `updateTime` | `string` | Output only. Update timestamp in RFC3339 text format. |
| `type` | `string` | Output only. The type of the resource, for example `compute.v1.instance`, or `cloudfunctions.v1beta1.function`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deployment, project, resource` | Gets information about a single resource. |
| `list` | `SELECT` | `deployment, project` | Lists all resources in a given deployment. |
| `_list` | `EXEC` | `deployment, project` | Lists all resources in a given deployment. |
