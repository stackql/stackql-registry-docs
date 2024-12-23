---
title: registered_models
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - registered_models
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

Operations on a <code>registered_models</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registered_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.registered_models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="catalog_name" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="full_name" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="schema_name" /> | `string` |
| <CopyableCode code="securable_kind" /> | `string` |
| <CopyableCode code="securable_type" /> | `string` |
| <CopyableCode code="storage_location" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="full_name, deployment_name" /> | Get a registered model. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List registered models. You can list registered models under a particular schema, or list all registered models in the current metastore. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new registered model in Unity Catalog. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="full_name, deployment_name" /> | Deletes a registered model and all its model versions from the specified parent catalog and schema. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="full_name, deployment_name" /> | Updates the specified registered model. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'registered_models (list)', value: 'list' },
        { label: 'registered_models (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
catalog_name,
comment,
created_at,
created_by,
full_name,
metastore_id,
owner,
schema_name,
securable_kind,
securable_type,
storage_location,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.registered_models
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
catalog_name,
comment,
created_at,
created_by,
full_name,
metastore_id,
owner,
schema_name,
securable_kind,
securable_type,
storage_location,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.registered_models
WHERE full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registered_models</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'registered_models', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.registered_models (
deployment_name,
data__name,
data__catalog_name,
data__schema_name,
data__comment
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ catalog_name }}',
'{{ schema_name }}',
'{{ comment }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: revenue_forecasting_model
  - name: catalog_name
    value: main
  - name: schema_name
    value: default
  - name: comment
    value: This model contains model versions that forecast future revenue, given
      historical data

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>registered_models</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.registered_models
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>registered_models</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.registered_models
WHERE full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```
