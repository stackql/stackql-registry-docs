---
title: executions
hide_title: false
hide_table_of_contents: false
keywords:
  - executions
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
<tr><td><b>Name</b></td><td><code>executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.run.executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `executions` | `array` | The resulting list of Executions. |
| `nextPageToken` | `string` | A token indicating there are more items than page_size. Use it in the next ListExecutions request to continue. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `executionsId, jobsId, locationsId, projectsId` | Gets information about an Execution. |
| `list` | `SELECT` | `jobsId, locationsId, projectsId` | Lists Executions from a Job. |
| `delete` | `DELETE` | `executionsId, jobsId, locationsId, projectsId` | Deletes an Execution. |
