---
title: compilation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - compilation_results
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
<tr><td><b>Name</b></td><td><code>compilation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataform.compilation_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The compilation result's name. |
| `releaseConfig` | `string` | Immutable. The name of the release config to compile. The release config's 'current_compilation_result' field will be updated to this compilation result. Must be in the format `projects/*/locations/*/repositories/*/releaseConfigs/*`. |
| `resolvedGitCommitSha` | `string` | Output only. The fully resolved Git commit SHA of the code that was compiled. Not set for compilation results whose source is a workspace. |
| `workspace` | `string` | Immutable. The name of the workspace to compile. Must be in the format `projects/*/locations/*/repositories/*/workspaces/*`. |
| `codeCompilationConfig` | `object` | Configures various aspects of Dataform code compilation. |
| `compilationErrors` | `array` | Output only. Errors encountered during project compilation. |
| `dataformCoreVersion` | `string` | Output only. The version of `@dataform/core` that was used for compilation. |
| `gitCommitish` | `string` | Immutable. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: `12ade345` - a tag: `tag1` - a branch name: `branch1` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `compilationResultsId, locationsId, projectsId, repositoriesId` | Fetches a single CompilationResult. |
| `list` | `SELECT` | `locationsId, projectsId, repositoriesId` | Lists CompilationResults in a given Repository. |
| `create` | `INSERT` | `locationsId, projectsId, repositoriesId` | Creates a new CompilationResult in a given project and location. |
| `_list` | `EXEC` | `locationsId, projectsId, repositoriesId` | Lists CompilationResults in a given Repository. |
| `query` | `EXEC` | `compilationResultsId, locationsId, projectsId, repositoriesId` | Returns CompilationResultActions in a given CompilationResult. |
