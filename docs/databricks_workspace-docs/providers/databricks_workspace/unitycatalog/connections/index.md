---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - connections
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

Operations on a <code>connections</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="connection_id" /> | `string` |
| <CopyableCode code="connection_type" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="credential_type" /> | `string` |
| <CopyableCode code="full_name" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="options" /> | `object` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="properties" /> | `object` |
| <CopyableCode code="provisioning_info" /> | `object` |
| <CopyableCode code="read_only" /> | `boolean` |
| <CopyableCode code="securable_kind" /> | `string` |
| <CopyableCode code="securable_type" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |
| <CopyableCode code="url" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets a connection from it's name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List all connections. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new connection |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Deletes the connection that matches the supplied name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates the connection that matches the supplied name. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'connections (list)', value: 'list' },
        { label: 'connections (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
comment,
connection_id,
connection_type,
created_at,
created_by,
credential_type,
full_name,
metastore_id,
options,
owner,
properties,
provisioning_info,
read_only,
securable_kind,
securable_type,
updated_at,
updated_by,
url
FROM databricks_workspace.unitycatalog.connections
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
comment,
connection_id,
connection_type,
created_at,
created_by,
credential_type,
full_name,
metastore_id,
options,
owner,
properties,
provisioning_info,
read_only,
securable_kind,
securable_type,
updated_at,
updated_by,
url
FROM databricks_workspace.unitycatalog.connections
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connections</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'connections', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.connections (
deployment_name,
data__name,
data__connection_type,
data__options,
data__read_only,
data__comment,
data__properties
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ connection_type }}',
'{{ options }}',
'{{ read_only }}',
'{{ comment }}',
'{{ properties }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: connection_type
    value: MYSQL
  - name: options
    value:
      property1: string
      property2: string
  - name: read_only
    value: true
  - name: comment
    value: string
  - name: properties
    value:
      property1: string
      property2: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connections</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.connections
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>connections</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.connections
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
