---
title: queries
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - queries
  - dbsql
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

Operations on a <code>queries</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.queries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="create_time" /> | `string` |
| <CopyableCode code="display_name" /> | `string` |
| <CopyableCode code="last_modifier_user_name" /> | `string` |
| <CopyableCode code="lifecycle_state" /> | `string` |
| <CopyableCode code="owner_user_name" /> | `string` |
| <CopyableCode code="parameters" /> | `array` |
| <CopyableCode code="parent_path" /> | `string` |
| <CopyableCode code="query_text" /> | `string` |
| <CopyableCode code="run_as_mode" /> | `string` |
| <CopyableCode code="tags" /> | `array` |
| <CopyableCode code="update_time" /> | `string` |
| <CopyableCode code="warehouse_id" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Gets a query. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets a list of queries accessible to the user, ordered by creation time. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a query. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Moves a query to the trash. Trashed queries immediately disappear from searches and list views, and cannot be used for alerts. You can restore a trashed query through the UI. A trashed query is permanently deleted after 30 days. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Updates a query. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'queries (list)', value: 'list' },
        { label: 'queries (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
description,
create_time,
display_name,
last_modifier_user_name,
lifecycle_state,
owner_user_name,
parameters,
parent_path,
query_text,
run_as_mode,
tags,
update_time,
warehouse_id
FROM databricks_workspace.dbsql.queries
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
description,
create_time,
display_name,
last_modifier_user_name,
lifecycle_state,
owner_user_name,
parameters,
parent_path,
query_text,
run_as_mode,
tags,
update_time,
warehouse_id
FROM databricks_workspace.dbsql.queries
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>queries</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'queries', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.dbsql.queries (
deployment_name,
data__query
)
SELECT 
'{{ deployment_name }}',
'{{ query }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: query
    value:
      description: Example description
      tags:
      - Tag 1
      display_name: Example query
      parent_path: /Workspace/Users/user@acme.com
      query_text: SELECT 1
      parameters:
      - name: foo
        text_value:
          value: bar
        title: foo
      warehouse_id: a7066a8ef796be84
      run_as_mode: OWNER

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>queries</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.dbsql.queries
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>queries</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.dbsql.queries
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
