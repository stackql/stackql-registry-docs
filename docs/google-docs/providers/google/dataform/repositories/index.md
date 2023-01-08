---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
  - dataform
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
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataform.repositories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The repository's name. |
| `gitRemoteSettings` | `object` | Controls Git remote configuration for a repository. |
| `npmrcEnvironmentVariablesSecretVersion` | `string` | Optional. The name of the Secret Manager secret version to be used to interpolate variables into the .npmrc file for package installation operations. Must be in the format `projects/*/secrets/*/versions/*`. The file itself must be in a JSON format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_repositories_get` | `SELECT` | `locationsId, projectsId, repositoriesId` | Fetches a single Repository. |
| `projects_locations_repositories_list` | `SELECT` | `locationsId, projectsId` | Lists Repositories in a given project and location. |
| `projects_locations_repositories_create` | `INSERT` | `locationsId, projectsId` | Creates a new Repository in a given project and location. |
| `projects_locations_repositories_delete` | `DELETE` | `locationsId, projectsId, repositoriesId` | Deletes a single Repository. |
| `projects_locations_repositories_patch` | `EXEC` | `locationsId, projectsId, repositoriesId` | Updates a single Repository. |
