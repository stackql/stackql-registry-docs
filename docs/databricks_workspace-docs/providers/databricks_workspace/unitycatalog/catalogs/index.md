---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - catalogs
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

Operations on a <code>catalogs</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.catalogs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="browse_only" /> | `boolean` |
| <CopyableCode code="catalog_type" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="connection_name" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="effective_predictive_optimization_flag" /> | `object` |
| <CopyableCode code="enable_predictive_optimization" /> | `string` |
| <CopyableCode code="full_name" /> | `string` |
| <CopyableCode code="isolation_mode" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="options" /> | `object` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="properties" /> | `object` |
| <CopyableCode code="provider_name" /> | `string` |
| <CopyableCode code="provisioning_info" /> | `object` |
| <CopyableCode code="securable_kind" /> | `string` |
| <CopyableCode code="securable_type" /> | `string` |
| <CopyableCode code="share_name" /> | `string` |
| <CopyableCode code="storage_location" /> | `string` |
| <CopyableCode code="storage_root" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets the specified catalog in a metastore. The caller must be a metastore admin, the owner of the catalog, or a user that has the |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets an array of catalogs in the metastore. If the caller is the metastore admin, all catalogs will be retrieved. Otherwise, only catalogs owned by the caller (or for which the caller has the |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new catalog instance in the parent metastore if the caller is a metastore admin or has the |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Deletes the catalog that matches the supplied name. The caller must be a metastore admin or the owner of the catalog. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates the catalog that matches the supplied name. The caller must be either the owner of the catalog, or a metastore admin (when changing the owner field of the catalog). |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'catalogs (list)', value: 'list' },
        { label: 'catalogs (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
browse_only,
catalog_type,
comment,
connection_name,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
full_name,
isolation_mode,
metastore_id,
options,
owner,
properties,
provider_name,
provisioning_info,
securable_kind,
securable_type,
share_name,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.catalogs
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
browse_only,
catalog_type,
comment,
connection_name,
created_at,
created_by,
effective_predictive_optimization_flag,
enable_predictive_optimization,
full_name,
isolation_mode,
metastore_id,
options,
owner,
properties,
provider_name,
provisioning_info,
securable_kind,
securable_type,
share_name,
storage_location,
storage_root,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.catalogs
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>catalogs</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'catalogs', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.catalogs (
deployment_name,
data__name,
data__comment,
data__properties,
data__storage_root,
data__provider_name,
data__share_name,
data__connection_name,
data__options
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ comment }}',
'{{ properties }}',
'{{ storage_root }}',
'{{ provider_name }}',
'{{ share_name }}',
'{{ connection_name }}',
'{{ options }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: comment
    value: string
  - name: properties
    value:
      property1: string
      property2: string
  - name: storage_root
    value: string
  - name: provider_name
    value: string
  - name: share_name
    value: string
  - name: connection_name
    value: string
  - name: options
    value:
      property1: string
      property2: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>catalogs</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.catalogs
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>catalogs</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.catalogs
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
