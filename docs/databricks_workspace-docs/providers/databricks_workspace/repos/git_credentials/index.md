---
title: git_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - git_credentials
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

Operations on a <code>git_credentials</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>git_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.repos.git_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="credential_id" /> | `string` |
| <CopyableCode code="git_provider" /> | `string` |
| <CopyableCode code="git_username" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="credential_id, deployment_name" /> | Gets the Git credential with the specified credential ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Lists the calling user's Git credentials. One credential per user is supported. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a Git credential entry for the user. Only one Git credential per user is supported, so any attempts to create credentials if an entry already exists will fail. Use the PATCH endpoint to update existing credentials, or the DELETE endpoint to delete existing credentials. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="credential_id, deployment_name" /> | Deletes the specified Git credential. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="credential_id, deployment_name" /> | Updates the specified Git credential. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'git_credentials (list)', value: 'list' },
        { label: 'git_credentials (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
credential_id,
git_provider,
git_username
FROM databricks_workspace.repos.git_credentials
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
credential_id,
git_provider,
git_username
FROM databricks_workspace.repos.git_credentials
WHERE credential_id = '{{ credential_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>git_credentials</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'git_credentials', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.repos.git_credentials (
deployment_name,
data__git_provider,
data__git_username,
data__personal_access_token
)
SELECT 
'{{ deployment_name }}',
'{{ git_provider }}',
'{{ git_username }}',
'{{ personal_access_token }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: git_provider
    value: gitHub
  - name: git_username
    value: testuser
  - name: personal_access_token
    value: something

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>git_credentials</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.repos.git_credentials
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE credential_id = '{{ credential_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>git_credentials</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.repos.git_credentials
WHERE credential_id = '{{ credential_id }}' AND
deployment_name = '{{ deployment_name }}';
```
