---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
  - datalineage
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
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalineage.runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token to specify as `page_token` in the next call to get the next page. If this field is omitted, there are no subsequent pages. |
| `runs` | `array` | The runs from the specified project and location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, processesId, projectsId, runsId` | Gets the details of the specified run. |
| `list` | `SELECT` | `locationsId, processesId, projectsId` | Lists runs in the given project and location. List order is descending by `start_time`. |
| `create` | `INSERT` | `locationsId, processesId, projectsId` | Creates a new run. |
| `delete` | `DELETE` | `locationsId, processesId, projectsId, runsId` | Deletes the run with the specified name. |
| `patch` | `EXEC` | `locationsId, processesId, projectsId, runsId` | Updates a run. |
