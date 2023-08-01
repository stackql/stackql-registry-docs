---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - batch
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.batch.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `jobs` | `array` | Jobs. |
| `nextPageToken` | `string` | Next page token. |
| `unreachable` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobsId, locationsId, projectsId` | Get a Job specified by its resource name. |
| `list` | `SELECT` | `locationsId, projectsId` | List all Jobs for a project within a region. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a Job. |
| `delete` | `DELETE` | `jobsId, locationsId, projectsId` | Delete a Job. |
