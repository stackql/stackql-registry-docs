---
title: processes
hide_title: false
hide_table_of_contents: false
keywords:
  - processes
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
<tr><td><b>Name</b></td><td><code>processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalineage.processes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The token to specify as `page_token` in the next call to get the next page. If this field is omitted, there are no subsequent pages. |
| `processes` | `array` | The processes from the specified project and location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, processesId, projectsId` | Gets the details of the specified process. |
| `list` | `SELECT` | `locationsId, projectsId` | List processes in the given project and location. List order is descending by insertion time. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new process. |
| `delete` | `DELETE` | `locationsId, processesId, projectsId` | Deletes the process with the specified name. |
| `patch` | `EXEC` | `locationsId, processesId, projectsId` | Updates a process. |
