---
title: metastores
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - metastores
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

Operations on a <code>metastores</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.metastores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="cloud" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="default_data_access_config_id" /> | `string` |
| <CopyableCode code="delta_sharing_organization_name" /> | `string` |
| <CopyableCode code="delta_sharing_recipient_token_lifetime_in_seconds" /> | `integer` |
| <CopyableCode code="delta_sharing_scope" /> | `string` |
| <CopyableCode code="external_access_enabled" /> | `boolean` |
| <CopyableCode code="global_metastore_id" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="privilege_model_version" /> | `string` |
| <CopyableCode code="region" /> | `string` |
| <CopyableCode code="storage_root" /> | `string` |
| <CopyableCode code="storage_root_credential_id" /> | `string` |
| <CopyableCode code="storage_root_credential_name" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Gets a metastore that matches the supplied ID. The caller must be a metastore admin to retrieve this info. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets an array of the available metastores (as |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new metastore based on a provided name and optional storage root path. By default (if the |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Deletes a metastore. The caller must be a metastore admin. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Updates information for a specific metastore. The caller must be a metastore admin. If the |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'metastores (list)', value: 'list' },
        { label: 'metastores (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
cloud,
created_at,
created_by,
default_data_access_config_id,
delta_sharing_organization_name,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
global_metastore_id,
metastore_id,
owner,
privilege_model_version,
region,
storage_root,
storage_root_credential_id,
storage_root_credential_name,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.metastores
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
cloud,
created_at,
created_by,
default_data_access_config_id,
delta_sharing_organization_name,
delta_sharing_recipient_token_lifetime_in_seconds,
delta_sharing_scope,
external_access_enabled,
global_metastore_id,
metastore_id,
owner,
privilege_model_version,
region,
storage_root,
storage_root_credential_id,
storage_root_credential_name,
updated_at,
updated_by
FROM databricks_workspace.unitycatalog.metastores
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metastores</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'metastores', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.metastores (
deployment_name,
data__name,
data__storage_root,
data__region
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ storage_root }}',
'{{ region }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: storage_root
    value: string
  - name: region
    value: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>metastores</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.metastores
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>metastores</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.metastores
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
