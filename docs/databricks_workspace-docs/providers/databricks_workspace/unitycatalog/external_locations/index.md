---
title: external_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - external_locations
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

Operations on a <code>external_locations</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.external_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="access_point" /> | `string` |
| <CopyableCode code="browse_only" /> | `boolean` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="credential_id" /> | `string` |
| <CopyableCode code="credential_name" /> | `string` |
| <CopyableCode code="isolation_mode" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="read_only" /> | `boolean` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |
| <CopyableCode code="url" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets an external location from the metastore. The caller must be either a metastore admin, the owner of the external location, or a user that has some privilege on the external location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets an array of external locations ( |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new external location entry in the metastore. The caller must be a metastore admin or have the |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Deletes the specified external location from the metastore. The caller must be the owner of the external location. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates an external location in the metastore. The caller must be the owner of the external location, or be a metastore admin. In the second case, the admin can only update the name of the external location. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'external_locations (list)', value: 'list' },
        { label: 'external_locations (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
access_point,
browse_only,
comment,
created_at,
created_by,
credential_id,
credential_name,
isolation_mode,
metastore_id,
owner,
read_only,
updated_at,
updated_by,
url
FROM databricks_workspace.unitycatalog.external_locations
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
access_point,
browse_only,
comment,
created_at,
created_by,
credential_id,
credential_name,
isolation_mode,
metastore_id,
owner,
read_only,
updated_at,
updated_by,
url
FROM databricks_workspace.unitycatalog.external_locations
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>external_locations</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'external_locations', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.external_locations (
deployment_name,
data__name,
data__url,
data__credential_name,
data__read_only,
data__comment,
data__access_point,
data__skip_validation
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ url }}',
'{{ credential_name }}',
'{{ read_only }}',
'{{ comment }}',
'{{ access_point }}',
'{{ skip_validation }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: url
    value: string
  - name: credential_name
    value: string
  - name: read_only
    value: true
  - name: comment
    value: string
  - name: access_point
    value: string
  - name: skip_validation
    value: true

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>external_locations</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.external_locations
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>external_locations</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.external_locations
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
