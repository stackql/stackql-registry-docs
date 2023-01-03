---
title: manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - manifests
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
<tr><td><b>Name</b></td><td><code>manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.deploymentmanager.manifests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | Output only. The name of the manifest. |
| `expandedConfig` | `string` | Output only. The fully-expanded configuration file, including any templates and references. |
| `manifestSizeBytes` | `string` | Output only. The computed size of the fully expanded manifest. |
| `selfLink` | `string` | Output only. Self link for the manifest. |
| `insertTime` | `string` | Output only. Creation timestamp in RFC3339 text format. |
| `manifestSizeLimitBytes` | `string` | Output only. The size limit for expanded manifests in the project. |
| `layout` | `string` | Output only. The YAML layout for this manifest. |
| `config` | `object` |  |
| `imports` | `array` | Output only. The imported files for this manifest. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deployment, manifest, project` | Gets information about a specific manifest. |
| `list` | `SELECT` | `deployment, project` | Lists all manifests for a given deployment. |
