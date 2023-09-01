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
| `labels` | `object` | Optional. Repository user labels. |
| `npmrcEnvironmentVariablesSecretVersion` | `string` | Optional. The name of the Secret Manager secret version to be used to interpolate variables into the .npmrc file for package installation operations. Must be in the format `projects/*/secrets/*/versions/*`. The file itself must be in a JSON format. |
| `serviceAccount` | `string` | Optional. The service account to run workflow invocations under. |
| `setAuthenticatedUserAdmin` | `boolean` | Optional. Input only. If set to true, the authenticated user will be granted the roles/dataform.admin role on the created repository. To modify access to the created repository later apply setIamPolicy from https://cloud.google.com/dataform/reference/rest#rest-resource:-v1beta1.projects.locations.repositories |
| `workspaceCompilationOverrides` | `object` | Configures workspace compilation overrides for a repository. Primarily used by the UI (`console.cloud.google.com`). `schema_suffix` and `table_prefix` can have a special expression - `$&#123;workspaceName&#125;`, which refers to the workspace name from which the compilation results will be created. API callers are expected to resolve the expression in these overrides and provide them explicitly in `code_compilation_config` (https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults#codecompilationconfig) when creating workspace-scoped compilation results. |
| `displayName` | `string` | Optional. The repository's user-friendly name. |
| `gitRemoteSettings` | `object` | Controls Git remote configuration for a repository. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, repositoriesId` | Fetches a single Repository. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists Repositories in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Repository in a given project and location. |
| `delete` | `DELETE` | `locationsId, projectsId, repositoriesId` | Deletes a single Repository. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists Repositories in a given project and location. |
| `commit` | `EXEC` | `locationsId, projectsId, repositoriesId` | Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`. |
| `compute_access_token_status` | `EXEC` | `locationsId, projectsId, repositoriesId` | Computes a Repository's Git access token status. |
| `patch` | `EXEC` | `locationsId, projectsId, repositoriesId` | Updates a single Repository. |
| `query_directory_contents` | `EXEC` | `locationsId, projectsId, repositoriesId` | Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`. |
| `read_file` | `EXEC` | `locationsId, projectsId, repositoriesId` | Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`. |
