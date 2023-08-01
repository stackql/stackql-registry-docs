---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - run
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
<tr><td><b>Id</b></td><td><code>google.run.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `jobs` | `array` | The resulting list of Jobs. |
| `nextPageToken` | `string` | A token indicating there are more items than page_size. Use it in the next ListJobs request to continue. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobsId, locationsId, projectsId` | Gets information about a Job. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Jobs. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a Job. |
| `delete` | `DELETE` | `jobsId, locationsId, projectsId` | Deletes a Job. |
| `patch` | `EXEC` | `jobsId, locationsId, projectsId` | Updates a Job. |
| `run` | `EXEC` | `jobsId, locationsId, projectsId` | Triggers creation of a new Execution of this Job. |
