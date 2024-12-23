---
title: metastores
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - metastores
  - unity_catalog
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>metastores</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.unity_catalog.metastores" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, metastore_id" /> | Gets a Unity Catalog metastore from an account, both specified by ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets all Unity Catalog metastores associated with an account specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a Unity Catalog metastore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, metastore_id" /> | Deletes a Unity Catalog metastore for an account, both specified by ID. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="account_id, metastore_id" /> | Updates an existing Unity Catalog metastore. |

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
FROM databricks_account.unity_catalog.metastores
WHERE account_id = '{{ account_id }}';
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
FROM databricks_account.unity_catalog.metastores
WHERE account_id = '{{ account_id }}' AND
metastore_id = '{{ metastore_id }}';
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
INSERT INTO databricks_account.unity_catalog.metastores (
account_id,
data__metastore_info
)
SELECT 
'{{ account_id }}',
'{{ metastore_info }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: metastore_info
    value:
      name: string
      storage_root: string
      region: string

```

</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>metastores</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_account.unity_catalog.metastores
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE account_id = '{{ account_id }}' AND
metastore_id = '{{ metastore_id }}';
```

## `DELETE` example

Deletes a <code>metastores</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.unity_catalog.metastores
WHERE account_id = '{{ account_id }}' AND
metastore_id = '{{ metastore_id }}';
```
