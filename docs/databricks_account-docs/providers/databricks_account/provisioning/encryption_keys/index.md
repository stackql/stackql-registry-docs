---
title: encryption_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - encryption_keys
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

Operations on a <code>encryption_keys</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>encryption_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.encryption_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="account_id" /> | `string` |
| <CopyableCode code="aws_key_info" /> | `object` |
| <CopyableCode code="creation_time" /> | `integer` |
| <CopyableCode code="customer_managed_key_id" /> | `string` |
| <CopyableCode code="use_cases" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, customer_managed_key_id" /> | Gets a customer-managed key configuration object for an account, specified by ID. This operation uploads a reference to a customer-managed key to Databricks. If assigned as a workspace's customer-managed key for managed services, Databricks uses the key to encrypt the workspaces notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history. If it is specified as a workspace's customer-managed key for storage, the key encrypts the workspace's root S3 bucket (which contains the workspace's root DBFS and system data) and, optionally, cluster EBS volume data. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets all customer-managed key configuration objects for an account. If the key is specified as a workspace's managed services customer-managed key, Databricks uses the key to encrypt the workspace's notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history. If the key is specified as a workspace's storage customer-managed key, the key is used to encrypt the workspace's root S3 bucket and optionally can encrypt cluster EBS volumes data in the data plane. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a customer-managed key configuration object for an account, specified by ID. This operation uploads a reference to a customer-managed key to Databricks. If the key is assigned as a workspace's customer-managed key for managed services, Databricks uses the key to encrypt the workspaces notebooks and secrets in the control plane, in addition to Databricks SQL queries and query history. If it is specified as a workspace's customer-managed key for workspace storage, the key encrypts the workspace's root S3 bucket (which contains the workspace's root DBFS and system data) and, optionally, cluster EBS volume data. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, customer_managed_key_id" /> | Deletes a customer-managed key configuration object for an account. You cannot delete a configuration that is associated with a running workspace. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'encryption_keys (list)', value: 'list' },
        { label: 'encryption_keys (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
account_id,
aws_key_info,
creation_time,
customer_managed_key_id,
use_cases
FROM databricks_account.provisioning.encryption_keys
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
account_id,
aws_key_info,
creation_time,
customer_managed_key_id,
use_cases
FROM databricks_account.provisioning.encryption_keys
WHERE account_id = '{{ account_id }}' AND
customer_managed_key_id = '{{ customer_managed_key_id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>encryption_keys</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'encryption_keys', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.provisioning.encryption_keys (
account_id,
data__aws_key_info,
data__use_cases
)
SELECT 
'{{ account_id }}',
'{{ aws_key_info }}',
'{{ use_cases }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: aws_key_info
    value:
      key_arn: arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321
      key_alias: alias/projectKey
      reuse_key_for_cluster_volumes: true
  - name: use_cases
    value:
    - MANAGED_SERVICES
    - STORAGE

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>encryption_keys</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.provisioning.encryption_keys
WHERE account_id = '{{ account_id }}' AND
customer_managed_key_id = '{{ customer_managed_key_id }}';
```
