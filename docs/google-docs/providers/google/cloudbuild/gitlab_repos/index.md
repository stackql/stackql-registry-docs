---
title: gitlab_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - gitlab_repos
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
<tr><td><b>Name</b></td><td><code>gitlab_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudbuild.gitlab_repos" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the repository |
| <CopyableCode code="description" /> | `string` | Description of the repository |
| <CopyableCode code="browseUri" /> | `string` | Link to the browse repo page on the GitLab instance |
| <CopyableCode code="displayName" /> | `string` | Display name of the repository |
| <CopyableCode code="repositoryId" /> | `object` | GitLabRepositoryId identifies a specific repository hosted on GitLab.com or GitLabEnterprise |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_gitlab_configs_repos_list" /> | `SELECT` | <CopyableCode code="gitLabConfigsId, locationsId, projectsId" /> |
| <CopyableCode code="_projects_locations_gitlab_configs_repos_list" /> | `EXEC` | <CopyableCode code="gitLabConfigsId, locationsId, projectsId" /> |
