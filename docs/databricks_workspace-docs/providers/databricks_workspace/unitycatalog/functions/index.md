---
title: functions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - functions
  - unitycatalog
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

Operations on a <code>functions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.functions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="browse_only" /> | `boolean` |
| <CopyableCode code="catalog_name" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="data_type" /> | `string` |
| <CopyableCode code="external_language" /> | `string` |
| <CopyableCode code="external_name" /> | `string` |
| <CopyableCode code="full_data_type" /> | `string` |
| <CopyableCode code="full_name" /> | `string` |
| <CopyableCode code="function_id" /> | `string` |
| <CopyableCode code="input_params" /> | `object` |
| <CopyableCode code="is_deterministic" /> | `boolean` |
| <CopyableCode code="is_null_call" /> | `boolean` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="parameter_style" /> | `string` |
| <CopyableCode code="properties" /> | `string` |
| <CopyableCode code="return_params" /> | `object` |
| <CopyableCode code="routine_body" /> | `string` |
| <CopyableCode code="routine_definition" /> | `string` |
| <CopyableCode code="routine_dependencies" /> | `object` |
| <CopyableCode code="schema_name" /> | `string` |
| <CopyableCode code="security_type" /> | `string` |
| <CopyableCode code="specific_name" /> | `string` |
| <CopyableCode code="sql_data_access" /> | `string` |
| <CopyableCode code="sql_path" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets a function from within a parent catalog and schema. For the fetch to succeed, the user must satisfy one of the following requirements: |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="catalog_name, schema_name, deployment_name" /> | List functions within the specified parent catalog and schema. If the user is a metastore admin, all functions are returned in the output list. Otherwise, the user must have the |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Deletes the function that matches the supplied name. For the deletion to succeed, the user must satisfy one of the following conditions: |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates the function that matches the supplied name. Only the owner of the function can be updated. If the user is not a metastore admin, the user must be a member of the group that is the new function owner. |

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'functions (get)', value: 'get' },
        { label: 'functions (list)', value: 'list' }
    ]
}>
<TabItem value="get">

```sql
SELECT
name,
browse_only,
catalog_name,
comment,
created_at,
created_by,
data_type,
external_language,
external_name,
full_data_type,
full_name,
function_id,
input_params,
is_deterministic,
is_null_call,
metastore_id,
owner,
parameter_style,
properties,
return_params,
routine_body,
routine_definition,
routine_dependencies,
schema_name,
security_type,
specific_name,
sql_data_access,
sql_path,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.functions
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="list">

```sql
SELECT
name,
browse_only,
catalog_name,
comment,
created_at,
created_by,
data_type,
external_language,
external_name,
full_data_type,
full_name,
function_id,
input_params,
is_deterministic,
is_null_call,
metastore_id,
owner,
parameter_style,
properties,
return_params,
routine_body,
routine_definition,
routine_dependencies,
schema_name,
security_type,
specific_name,
sql_data_access,
sql_path,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.functions
WHERE catalog_name = '{{ catalog_name }}' AND
schema_name = '{{ schema_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>functions</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'functions', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.functions (
deployment_name,
data__function_info
)
SELECT 
'{{ deployment_name }}',
'{{ function_info }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: function_info
    value:
      name: string
      catalog_name: string
      schema_name: string
      input_params:
        parameters:
        - name: string
          type_text: string
          type_json: string
          type_name: BOOLEAN
          type_precision: 0
          type_scale: 0
          type_interval_type: string
          position: 0
          parameter_mode: IN
          parameter_type: PARAM
          parameter_default: string
          comment: string
      data_type: BOOLEAN
      full_data_type: string
      return_params:
        parameters:
        - name: string
          type_text: string
          type_json: string
          type_name: BOOLEAN
          type_precision: 0
          type_scale: 0
          type_interval_type: string
          position: 0
          parameter_mode: IN
          parameter_type: PARAM
          parameter_default: string
          comment: string
      routine_definition: string
      routine_dependencies:
        dependencies:
        - table:
            table_full_name: string
          function:
            function_full_name: string
      is_deterministic: true
      is_null_call: true
      specific_name: string
      external_name: string
      external_language: string
      sql_path: string
      comment: string
      properties: string
      routine_body: SQL
      security_type: DEFINER
      sql_data_access: CONTAINS_SQL
      parameter_style: S

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>functions</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.functions
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>functions</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.functions
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
