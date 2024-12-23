---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - tables
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

Operations on a <code>tables</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="access_point" /> | `string` |
| <CopyableCode code="browse_only" /> | `boolean` |
| <CopyableCode code="catalog_name" /> | `string` |
| <CopyableCode code="columns" /> | `array` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="data_access_configuration_id" /> | `string` |
| <CopyableCode code="data_source_format" /> | `string` |
| <CopyableCode code="deleted_at" /> | `integer` |
| <CopyableCode code="delta_runtime_properties_kvpairs" /> | `object` |
| <CopyableCode code="effective_predictive_optimization_flag" /> | `object` |
| <CopyableCode code="enable_predictive_optimization" /> | `string` |
| <CopyableCode code="full_name" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="pipeline_id" /> | `string` |
| <CopyableCode code="properties" /> | `object` |
| <CopyableCode code="row_filter" /> | `object` |
| <CopyableCode code="schema_name" /> | `string` |
| <CopyableCode code="sql_path" /> | `string` |
| <CopyableCode code="storage_credential_name" /> | `string` |
| <CopyableCode code="storage_location" /> | `string` |
| <CopyableCode code="table_constraints" /> | `array` |
| <CopyableCode code="table_id" /> | `string` |
| <CopyableCode code="table_type" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |
| <CopyableCode code="view_definition" /> | `string` |
| <CopyableCode code="view_dependencies" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="full_name, deployment_name" /> | Gets a table from the metastore for a specific catalog and schema. The caller must satisfy one of the following requirements: |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="catalog_name, schema_name, deployment_name" /> | Gets an array of all tables for the current metastore under the parent catalog and schema. The caller must be a metastore admin or an owner of (or have the |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="full_name, deployment_name" /> | Deletes a table from the specified parent catalog and schema. The caller must be the owner of the parent catalog, have the |

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'tables (get)', value: 'get' },
        { label: 'tables (list)', value: 'list' }
    ]
}>
<TabItem value="get">

```sql
SELECT
name,
access_point,
browse_only,
catalog_name,
columns,
comment,
created_at,
created_by,
data_access_configuration_id,
data_source_format,
deleted_at,
delta_runtime_properties_kvpairs,
effective_predictive_optimization_flag,
enable_predictive_optimization,
full_name,
metastore_id,
owner,
pipeline_id,
properties,
row_filter,
schema_name,
sql_path,
storage_credential_name,
storage_location,
table_constraints,
table_id,
table_type,
updated_at,
updated_by,
view_definition,
view_dependencies
FROM databricks_workspace.unitycatalog.tables
WHERE full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="list">

```sql
SELECT
name,
access_point,
browse_only,
catalog_name,
columns,
comment,
created_at,
created_by,
data_access_configuration_id,
data_source_format,
deleted_at,
delta_runtime_properties_kvpairs,
effective_predictive_optimization_flag,
enable_predictive_optimization,
full_name,
metastore_id,
owner,
pipeline_id,
properties,
row_filter,
schema_name,
sql_path,
storage_credential_name,
storage_location,
table_constraints,
table_id,
table_type,
updated_at,
updated_by,
view_definition,
view_dependencies
FROM databricks_workspace.unitycatalog.tables
WHERE catalog_name = '{{ catalog_name }}' AND
schema_name = '{{ schema_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>tables</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.tables
WHERE full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```
