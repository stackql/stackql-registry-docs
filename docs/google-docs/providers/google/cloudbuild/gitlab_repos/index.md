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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gitlab_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbuild.gitlab_repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the repository |
| `description` | `string` | Description of the repository |
| `displayName` | `string` | Display name of the repository |
| `repositoryId` | `object` | GitLabRepositoryId identifies a specific repository hosted on GitLab.com or GitLabEnterprise |
| `browseUri` | `string` | Link to the browse repo page on the GitLab instance |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_gitlab_configs_repos_list` | `SELECT` | `gitLabConfigsId, locationsId, projectsId` |
| `_projects_locations_gitlab_configs_repos_list` | `EXEC` | `gitLabConfigsId, locationsId, projectsId` |
