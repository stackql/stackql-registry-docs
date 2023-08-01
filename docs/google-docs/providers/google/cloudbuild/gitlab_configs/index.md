---
title: gitlab_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - gitlab_configs
  - cloudbuild
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
<tr><td><b>Name</b></td><td><code>gitlab_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbuild.gitlab_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `gitlabConfigs` | `array` | A list of GitLabConfigs |
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_gitlab_configs_get` | `SELECT` | `gitLabConfigsId, locationsId, projectsId` | Retrieves a `GitLabConfig`. This API is experimental |
| `projects_locations_gitlab_configs_list` | `SELECT` | `locationsId, projectsId` | List all `GitLabConfigs` for a given project. This API is experimental |
| `projects_locations_gitlab_configs_create` | `INSERT` | `locationsId, projectsId` | Creates a new `GitLabConfig`. This API is experimental |
| `projects_locations_gitlab_configs_delete` | `DELETE` | `gitLabConfigsId, locationsId, projectsId` | Delete a `GitLabConfig`. This API is experimental |
| `projects_locations_gitlab_configs_patch` | `EXEC` | `gitLabConfigsId, locationsId, projectsId` | Updates an existing `GitLabConfig`. This API is experimental |
