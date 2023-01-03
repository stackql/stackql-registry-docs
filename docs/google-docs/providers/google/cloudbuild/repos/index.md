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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | The resource name of the repository. |
| `description` | `string` | Description of the repository. |
| `repoId` | `object` | BitbucketServerRepositoryId identifies a specific repository hosted on a Bitbucket Server. |
| `browseUri` | `string` | Link to the browse repo page on the Bitbucket Server instance. |
| `displayName` | `string` | Display name of the repository. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_bitbucketServerConfigs_repos_list` | `SELECT` | `bitbucketServerConfigsId, locationsId, projectsId` |
