---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - tokens
  - workspace
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

Operations on a <code>tokens</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_by_id" /> | `integer` |
| <CopyableCode code="created_by_username" /> | `string` |
| <CopyableCode code="creation_time" /> | `integer` |
| <CopyableCode code="expiry_time" /> | `integer` |
| <CopyableCode code="last_used_day" /> | `integer` |
| <CopyableCode code="owner_id" /> | `integer` |
| <CopyableCode code="token_id" /> | `string` |
| <CopyableCode code="workspace_id" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="token_id, deployment_name" /> | Gets information about a token, specified by its ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Lists all tokens associated with the specified workspace or user. |
| <CopyableCode code="createobotoken" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a token on behalf of a service principal. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="token_id, deployment_name" /> | Deletes a token, specified by its ID. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'tokens (list)', value: 'list' },
        { label: 'tokens (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
comment,
created_by_id,
created_by_username,
creation_time,
expiry_time,
last_used_day,
owner_id,
token_id,
workspace_id
FROM databricks_workspace.workspace.tokens
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
comment,
created_by_id,
created_by_username,
creation_time,
expiry_time,
last_used_day,
owner_id,
token_id,
workspace_id
FROM databricks_workspace.workspace.tokens
WHERE token_id = '{{ token_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tokens</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'tokens', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.workspace.tokens (
deployment_name,
data__application_id,
data__lifetime_seconds,
data__comment
)
SELECT 
'{{ deployment_name }}',
'{{ application_id }}',
'{{ lifetime_seconds }}',
'{{ comment }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: application_id
    value: 6f5ccf28-d83a-4957-9bfb-5bbfac551410
  - name: lifetime_seconds
    value: 3600
  - name: comment
    value: This is for the ABC department automation scripts.

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>tokens</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.workspace.tokens
WHERE token_id = '{{ token_id }}' AND
deployment_name = '{{ deployment_name }}';
```
