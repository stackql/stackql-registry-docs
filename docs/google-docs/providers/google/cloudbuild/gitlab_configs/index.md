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
| `name` | `string` | The resource name for the config. |
| `webhookKey` | `string` | Output only. UUID included in webhook requests. The UUID is used to look up the corresponding config. |
| `connectedRepositories` | `array` | Connected GitLab.com or GitLabEnterprise repositories for this config. |
| `createTime` | `string` | Output only. Time when the config was created. |
| `enterpriseConfig` | `object` | GitLabEnterpriseConfig represents the configuration for a GitLabEnterprise integration. |
| `secrets` | `object` | GitLabSecrets represents the secrets in Secret Manager for a GitLab integration. |
| `username` | `string` | Username of the GitLab.com or GitLab Enterprise account Cloud Build will use. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_gitlab_configs_get` | `SELECT` | `gitLabConfigsId, locationsId, projectsId` | Retrieves a `GitLabConfig`. This API is experimental |
| `projects_locations_gitlab_configs_list` | `SELECT` | `locationsId, projectsId` | List all `GitLabConfigs` for a given project. This API is experimental |
| `projects_locations_gitlab_configs_create` | `INSERT` | `locationsId, projectsId` | Creates a new `GitLabConfig`. This API is experimental |
| `projects_locations_gitlab_configs_delete` | `DELETE` | `gitLabConfigsId, locationsId, projectsId` | Delete a `GitLabConfig`. This API is experimental |
| `_projects_locations_gitlab_configs_list` | `EXEC` | `locationsId, projectsId` | List all `GitLabConfigs` for a given project. This API is experimental |
| `projects_locations_gitlab_configs_patch` | `EXEC` | `gitLabConfigsId, locationsId, projectsId` | Updates an existing `GitLabConfig`. This API is experimental |
