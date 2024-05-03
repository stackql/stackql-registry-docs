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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gitlab_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudbuild.gitlab_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name for the config. |
| <CopyableCode code="connectedRepositories" /> | `array` | Connected GitLab.com or GitLabEnterprise repositories for this config. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the config was created. |
| <CopyableCode code="enterpriseConfig" /> | `object` | GitLabEnterpriseConfig represents the configuration for a GitLabEnterprise integration. |
| <CopyableCode code="secrets" /> | `object` | GitLabSecrets represents the secrets in Secret Manager for a GitLab integration. |
| <CopyableCode code="username" /> | `string` | Username of the GitLab.com or GitLab Enterprise account Cloud Build will use. |
| <CopyableCode code="webhookKey" /> | `string` | Output only. UUID included in webhook requests. The UUID is used to look up the corresponding config. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_gitlab_configs_get" /> | `SELECT` | <CopyableCode code="gitLabConfigsId, locationsId, projectsId" /> | Retrieves a `GitLabConfig`. This API is experimental |
| <CopyableCode code="projects_locations_gitlab_configs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List all `GitLabConfigs` for a given project. This API is experimental |
| <CopyableCode code="projects_locations_gitlab_configs_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new `GitLabConfig`. This API is experimental |
| <CopyableCode code="projects_locations_gitlab_configs_delete" /> | `DELETE` | <CopyableCode code="gitLabConfigsId, locationsId, projectsId" /> | Delete a `GitLabConfig`. This API is experimental |
| <CopyableCode code="_projects_locations_gitlab_configs_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List all `GitLabConfigs` for a given project. This API is experimental |
| <CopyableCode code="projects_locations_gitlab_configs_patch" /> | `EXEC` | <CopyableCode code="gitLabConfigsId, locationsId, projectsId" /> | Updates an existing `GitLabConfig`. This API is experimental |
