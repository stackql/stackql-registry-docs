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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>compilation_results</code> resource.

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
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp of when the compilation result was created. |
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
| <CopyableCode code="query" /> | `SELECT` | <CopyableCode code="compilationResultsId, locationsId, projectsId, repositoriesId" /> | Returns CompilationResultActions in a given CompilationResult. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Creates a new CompilationResult in a given project and location. |

## `SELECT` examples

Lists CompilationResults in a given Repository.

```sql
SELECT
name,
codeCompilationConfig,
compilationErrors,
createTime,
dataEncryptionState,
dataformCoreVersion,
gitCommitish,
releaseConfig,
resolvedGitCommitSha,
workspace
FROM google.dataform.compilation_results
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>compilation_results</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.dataform.compilation_results (
locationsId,
projectsId,
repositoriesId,
gitCommitish,
workspace,
releaseConfig,
codeCompilationConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ repositoriesId }}',
'{{ gitCommitish }}',
'{{ workspace }}',
'{{ releaseConfig }}',
'{{ codeCompilationConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: gitCommitish
      value: '{{ gitCommitish }}'
    - name: workspace
      value: '{{ workspace }}'
    - name: releaseConfig
      value: '{{ releaseConfig }}'
    - name: codeCompilationConfig
      value:
        - name: defaultDatabase
          value: '{{ defaultDatabase }}'
        - name: defaultSchema
          value: '{{ defaultSchema }}'
        - name: defaultLocation
          value: '{{ defaultLocation }}'
        - name: assertionSchema
          value: '{{ assertionSchema }}'
        - name: vars
          value: '{{ vars }}'
        - name: databaseSuffix
          value: '{{ databaseSuffix }}'
        - name: schemaSuffix
          value: '{{ schemaSuffix }}'
        - name: tablePrefix
          value: '{{ tablePrefix }}'
        - name: defaultNotebookRuntimeOptions
          value:
            - name: gcsOutputBucket
              value: '{{ gcsOutputBucket }}'

```
</TabItem>
</Tabs>
