---
title: cutover_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - cutover_jobs
  - vmmigration
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
<tr><td><b>Name</b></td><td><code>cutover_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.cutover_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `cutoverJobs` | `array` | Output only. The list of cutover jobs response. |
| `nextPageToken` | `string` | Output only. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable` | `array` | Output only. Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cutoverJobsId, locationsId, migratingVmsId, projectsId, sourcesId` | Gets details of a single CutoverJob. |
| `list` | `SELECT` | `locationsId, migratingVmsId, projectsId, sourcesId` | Lists CutoverJobs of a given migrating VM. |
| `create` | `INSERT` | `locationsId, migratingVmsId, projectsId, sourcesId` | Initiates a Cutover of a specific migrating VM. The returned LRO is completed when the cutover job resource is created and the job is initiated. |
| `cancel` | `EXEC` | `cutoverJobsId, locationsId, migratingVmsId, projectsId, sourcesId` | Initiates the cancellation of a running cutover job. |
