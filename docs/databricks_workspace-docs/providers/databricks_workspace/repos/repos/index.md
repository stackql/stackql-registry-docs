---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - repos
  - repos
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>repos</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.repos.repos" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="branch" /> | `string` |
| <CopyableCode code="head_commit_id" /> | `string` |
| <CopyableCode code="path" /> | `string` |
| <CopyableCode code="provider" /> | `string` |
| <CopyableCode code="url" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="repo_id, deployment_name" /> | Returns the repo with the given repo ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Returns repos that the calling user has Manage permissions on. Use |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a repo in the workspace and links it to the remote Git repo specified. Note that repos created programmatically must be linked to a remote Git repo, unlike repos created in the browser. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="repo_id, deployment_name" /> | Deletes the specified repo. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="repo_id, deployment_name" /> | Updates the repo to a different branch or tag, or updates the repo to the latest commit on the same branch. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'repos (list)', value: 'list' },
        { label: 'repos (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
branch,
head_commit_id,
path,
provider,
url
FROM databricks_workspace.repos.repos
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
branch,
head_commit_id,
path,
provider,
url
FROM databricks_workspace.repos.repos
WHERE repo_id = '{{ repo_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>repos</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'repos', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.repos.repos (
deployment_name,
data__branch,
data__path,
data__provider,
data__sparse_checkout,
data__url
)
SELECT 
'{{ deployment_name }}',
'{{ branch }}',
'{{ path }}',
'{{ provider }}',
'{{ sparse_checkout }}',
'{{ url }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: branch
    value: main
  - name: path
    value: /Users/user@company.com/clitest
  - name: provider
    value: gitHub
  - name: sparse_checkout
    value:
      patterns:
      - parent-folder/child-folder
      - src
      - test
  - name: url
    value: https://github.com/databricks/cli.git

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>repos</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.repos.repos
SET { field = value }
WHERE repo_id = '{{ repo_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>repos</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.repos.repos
WHERE repo_id = '{{ repo_id }}' AND
deployment_name = '{{ deployment_name }}';
```
