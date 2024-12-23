---
title: model_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - model_versions
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

Operations on a <code>model_versions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.model_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="catalog_name" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="model_name" /> | `string` |
| <CopyableCode code="run_id" /> | `string` |
| <CopyableCode code="run_workspace_id" /> | `string` |
| <CopyableCode code="schema_name" /> | `string` |
| <CopyableCode code="source" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="storage_location" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |
| <CopyableCode code="version" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="full_name, version, deployment_name" /> | Get a model version. |
| <CopyableCode code="getbyalias" /> | `SELECT` | <CopyableCode code="alias, full_name, deployment_name" /> | Get a model version by alias. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="full_name, deployment_name" /> | List model versions. You can list model versions under a particular schema, or list all model versions in the current metastore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="full_name, version, deployment_name" /> | Deletes a model version from the specified registered model. Any aliases assigned to the model version will also be deleted. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="full_name, version, deployment_name" /> | Updates the specified model version. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'model_versions (list)', value: 'list' },
        { label: 'model_versions (get)', value: 'get' },
        { label: 'model_versions (getbyalias)', value: 'getbyalias' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
catalog_name,
comment,
created_at,
created_by,
metastore_id,
model_name,
run_id,
run_workspace_id,
schema_name,
source,
status,
storage_location,
updated_at,
updated_by,
version
FROM databricks_workspace.unitycatalog.model_versions
WHERE full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
catalog_name,
comment,
created_at,
created_by,
metastore_id,
model_name,
run_id,
run_workspace_id,
schema_name,
source,
status,
storage_location,
updated_at,
updated_by,
version
FROM databricks_workspace.unitycatalog.model_versions
WHERE full_name = '{{ full_name }}' AND
version = '{{ version }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getbyalias">

```sql
SELECT
id,
catalog_name,
comment,
created_at,
created_by,
metastore_id,
model_name,
run_id,
run_workspace_id,
schema_name,
source,
status,
storage_location,
updated_at,
updated_by,
version
FROM databricks_workspace.unitycatalog.model_versions
WHERE alias = '{{ alias }}' AND
full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>model_versions</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.model_versions
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE full_name = '{{ full_name }}' AND
version = '{{ version }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>model_versions</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.model_versions
WHERE full_name = '{{ full_name }}' AND
version = '{{ version }}' AND
deployment_name = '{{ deployment_name }}';
```
