---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - transcoder
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
<tr><td><b>Id</b></td><td><code>google.transcoder.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | List of regions that could not be reached. |
| `jobs` | `array` | List of jobs in the specified region. |
| `nextPageToken` | `string` | The pagination token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobsId, locationsId, projectsId` | Returns the job data. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists jobs in the specified region. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a job in the specified region. |
| `delete` | `DELETE` | `jobsId, locationsId, projectsId` | Deletes a job. |
