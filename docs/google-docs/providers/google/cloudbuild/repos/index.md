---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbuild.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `bitbucketServerRepositories` | `array` | List of Bitbucket Server repositories. |
| `nextPageToken` | `string` | A token that can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_bitbucket_server_configs_repos_list` | `SELECT` | `bitbucketServerConfigsId, locationsId, projectsId` | List all repositories for a given `BitbucketServerConfig`. This API is experimental. |
| `projects_locations_gitlab_configs_repos_list` | `SELECT` | `gitLabConfigsId, locationsId, projectsId` | List all repositories for a given `GitLabConfig`. This API is experimental |
