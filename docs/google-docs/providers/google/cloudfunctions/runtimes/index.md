---
title: runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - runtimes
  - cloudfunctions
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
<tr><td><b>Name</b></td><td><code>runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudfunctions.runtimes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the runtime, e.g., 'go113', 'nodejs12', etc. |
| `warnings` | `array` | Warning messages, e.g., a deprecation warning. |
| `displayName` | `string` | The user facing name, eg 'Go 1.13', 'Node.js 12', etc. |
| `environment` | `string` | The environment for the runtime. |
| `stage` | `string` | The stage of life this runtime is in, e.g., BETA, GA, etc. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_runtimes_list` | `SELECT` | `locationsId, projectsId` |
