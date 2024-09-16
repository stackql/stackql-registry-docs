---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
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

Creates, updates, deletes, gets or lists a <code>workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.workspaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The workspace's name. |
| <CopyableCode code="dataEncryptionState" /> | `object` | Describes encryption state of a resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Fetches a single Workspace. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Lists Workspaces in a given Repository. |
| <CopyableCode code="query_directory_contents" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Returns the contents of a given Workspace directory. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Creates a new Workspace in a given Repository. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Deletes a single Workspace. |
| <CopyableCode code="commit" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Applies a Git commit for uncommitted files in a Workspace. |
| <CopyableCode code="install_npm_packages" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Installs dependency NPM packages (inside a Workspace). |
| <CopyableCode code="make_directory" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Creates a directory inside a Workspace. |
| <CopyableCode code="move_directory" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Moves a directory (inside a Workspace), and all of its contents, to a new location. |
| <CopyableCode code="move_file" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Moves a file (inside a Workspace) to a new location. |
| <CopyableCode code="pull" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Pulls Git commits from the Repository's remote into a Workspace. |
| <CopyableCode code="push" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Pushes Git commits from a Workspace to the Repository's remote. |
| <CopyableCode code="read_file" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Returns the contents of a file (inside a Workspace). |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Performs a Git reset for uncommitted files in a Workspace. |
| <CopyableCode code="search_files" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Finds the contents of a given Workspace directory by filter. |
| <CopyableCode code="write_file" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId, workspacesId" /> | Writes to a file (inside a Workspace). |

## `SELECT` examples

Lists Workspaces in a given Repository.

```sql
SELECT
name,
dataEncryptionState
FROM google.dataform.workspaces
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspaces</code> resource.

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
INSERT INTO google.dataform.workspaces (
locationsId,
projectsId,
repositoriesId,
name,
dataEncryptionState
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ repositoriesId }}',
'{{ name }}',
'{{ dataEncryptionState }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: dataEncryptionState
      value: '{{ dataEncryptionState }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>workspaces</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataform.workspaces
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'
AND workspacesId = '{{ workspacesId }}';
```
