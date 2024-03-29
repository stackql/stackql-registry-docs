---
title: connected_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_repositories
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
<tr><td><b>Name</b></td><td><code>connected_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbuild.connected_repositories</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_bitbucket_server_configs_connected_repositories_batch_create` | `EXEC` | `bitbucketServerConfigsId, locationsId, projectsId` | Batch connecting Bitbucket Server repositories to Cloud Build. |
| `projects_locations_gitlab_configs_connected_repositories_batch_create` | `EXEC` | `gitLabConfigsId, locationsId, projectsId` | Batch connecting GitLab repositories to Cloud Build. This API is experimental. |
