---
title: runtime_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - runtime_versions
  - tpu
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
<tr><td><b>Name</b></td><td><code>runtime_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.tpu.runtime_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name. |
| `version` | `string` | The runtime version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_runtimeVersions_get` | `SELECT` | `locationsId, projectsId, runtimeVersionsId` | Gets a runtime version. |
| `projects_locations_runtimeVersions_list` | `SELECT` | `locationsId, projectsId` | Lists runtime versions supported by this API. |
