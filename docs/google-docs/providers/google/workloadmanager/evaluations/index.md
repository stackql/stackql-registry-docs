---
title: evaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluations
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
<tr><td><b>Name</b></td><td><code>evaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workloadmanager.evaluations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token identifying a page of results the server should return. |
| `unreachable` | `array` | Locations that could not be reached. |
| `evaluations` | `array` | The list of Evaluation |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `evaluationsId, locationsId, projectsId` | Gets details of a single Evaluation. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Evaluations in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Evaluation in a given project and location. |
