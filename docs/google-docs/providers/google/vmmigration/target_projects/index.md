---
title: target_projects
hide_title: false
hide_table_of_contents: false
keywords:
  - target_projects
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
<tr><td><b>Name</b></td><td><code>target_projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.target_projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Output only. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `targetProjects` | `array` | Output only. The list of target response. |
| `unreachable` | `array` | Output only. Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, targetProjectsId` | Gets details of a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists TargetProjects in a given project. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new TargetProject in a given project. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| `delete` | `DELETE` | `locationsId, projectsId, targetProjectsId` | Deletes a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| `patch` | `EXEC` | `locationsId, projectsId, targetProjectsId` | Updates the parameters of a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
