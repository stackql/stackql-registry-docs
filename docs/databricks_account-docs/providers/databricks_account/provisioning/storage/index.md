---
title: storage
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - storage
  - provisioning
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

Operations on a <code>storage</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.storage" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="account_id" /> | `string` |
| <CopyableCode code="creation_time" /> | `integer` |
| <CopyableCode code="root_bucket_info" /> | `object` |
| <CopyableCode code="storage_configuration_id" /> | `string` |
| <CopyableCode code="storage_configuration_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, storage_configuration_id" /> | Gets a Databricks storage configuration for an account, both specified by ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets a list of all Databricks storage configurations for your account, specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates new storage configuration for an account, specified by ID. Uploads a storage configuration object that represents the root AWS S3 bucket in your account. Databricks stores related workspace assets including DBFS, cluster logs, and job results. For the AWS S3 bucket, you need to configure the required bucket policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, storage_configuration_id" /> | Deletes a Databricks storage configuration. You cannot delete a storage configuration that is associated with any workspace. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'storage (list)', value: 'list' },
        { label: 'storage (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
account_id,
creation_time,
root_bucket_info,
storage_configuration_id,
storage_configuration_name
FROM databricks_account.provisioning.storage
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
account_id,
creation_time,
root_bucket_info,
storage_configuration_id,
storage_configuration_name
FROM databricks_account.provisioning.storage
WHERE account_id = '{{ account_id }}' AND
storage_configuration_id = '{{ storage_configuration_id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'storage', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.provisioning.storage (
account_id,
data__storage_configuration_name,
data__root_bucket_info
)
SELECT 
'{{ account_id }}',
'{{ storage_configuration_name }}',
'{{ root_bucket_info }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: storage_configuration_name
    value: storage_conf_1
  - name: root_bucket_info
    value:
      bucket_name: string

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>storage</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.provisioning.storage
WHERE account_id = '{{ account_id }}' AND
storage_configuration_id = '{{ storage_configuration_id }}';
```
