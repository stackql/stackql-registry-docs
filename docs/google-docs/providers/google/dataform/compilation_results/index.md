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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compilation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.compilation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The compilation result's name. |
| <CopyableCode code="codeCompilationConfig" /> | `object` | Configures various aspects of Dataform code compilation. |
| <CopyableCode code="compilationErrors" /> | `array` | Output only. Errors encountered during project compilation. |
| <CopyableCode code="dataEncryptionState" /> | `object` | Describes encryption state of a resource. |
| <CopyableCode code="dataformCoreVersion" /> | `string` | Output only. The version of `@dataform/core` that was used for compilation. |
| <CopyableCode code="gitCommitish" /> | `string` | Immutable. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: `12ade345` - a tag: `tag1` - a branch name: `branch1` |
| <CopyableCode code="releaseConfig" /> | `string` | Immutable. The name of the release config to compile. Must be in the format `projects/*/locations/*/repositories/*/releaseConfigs/*`. |
| <CopyableCode code="resolvedGitCommitSha" /> | `string` | Output only. The fully resolved Git commit SHA of the code that was compiled. Not set for compilation results whose source is a workspace. |
| <CopyableCode code="workspace" /> | `string` | Immutable. The name of the workspace to compile. Must be in the format `projects/*/locations/*/repositories/*/workspaces/*`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="compilationResultsId, locationsId, projectsId, repositoriesId" /> | Fetches a single CompilationResult. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Lists CompilationResults in a given Repository. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Creates a new CompilationResult in a given project and location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Lists CompilationResults in a given Repository. |
| <CopyableCode code="query" /> | `EXEC` | <CopyableCode code="compilationResultsId, locationsId, projectsId, repositoriesId" /> | Returns CompilationResultActions in a given CompilationResult. |
