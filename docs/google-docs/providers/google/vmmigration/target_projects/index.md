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
| `name` | `string` | Output only. The name of the target project. |
| `description` | `string` | The target project's description. |
| `project` | `string` | The target project ID (number) or project name. |
| `updateTime` | `string` | Output only. The last time the target project resource was updated. |
| `createTime` | `string` | Output only. The time this target project resource was created (not related to when the Compute Engine project it points to was created). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, targetProjectsId` | Gets details of a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists TargetProjects in a given project. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new TargetProject in a given project. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| `delete` | `DELETE` | `locationsId, projectsId, targetProjectsId` | Deletes a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists TargetProjects in a given project. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
| `patch` | `EXEC` | `locationsId, projectsId, targetProjectsId` | Updates the parameters of a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`. |
