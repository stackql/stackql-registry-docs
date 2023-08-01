---
title: executions
hide_title: false
hide_table_of_contents: false
keywords:
  - executions
  - workloadmanager
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
<tr><td><b>Id</b></td><td><code>google.workloadmanager.executions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `unreachable` | `array` | Locations that could not be reached. |
| `executions` | `array` | The list of Execution |
| `nextPageToken` | `string` | A token identifying a page of results the server should return. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `evaluationsId, executionsId, locationsId, projectsId` | Gets details of a single Execution. |
| `list` | `SELECT` | `evaluationsId, locationsId, projectsId` | Lists Executions in a given project and location. |
| `run` | `EXEC` | `evaluationsId, locationsId, projectsId` | Creates a new Execution in a given project and location. |
