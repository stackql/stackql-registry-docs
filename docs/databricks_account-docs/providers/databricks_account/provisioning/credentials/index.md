---
title: credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - credentials
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

Operations on a <code>credentials</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="account_id" /> | `string` |
| <CopyableCode code="aws_credentials" /> | `object` |
| <CopyableCode code="creation_time" /> | `integer` |
| <CopyableCode code="credentials_id" /> | `string` |
| <CopyableCode code="credentials_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, credentials_id" /> | Gets a Databricks credential configuration object for an account, both specified by ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets all Databricks credential configurations associated with an account specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a Databricks credential configuration that represents cloud cross-account credentials for a specified account. Databricks uses this to set up network infrastructure properly to host Databricks clusters. For your AWS IAM role, you need to trust the External ID (the Databricks Account API account ID)  in the returned credential object, and configure the required access policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, credentials_id" /> | Deletes a Databricks credential configuration object for an account, both specified by ID. You cannot delete a credential that is associated with any workspace. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'credentials (list)', value: 'list' },
        { label: 'credentials (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
account_id,
aws_credentials,
creation_time,
credentials_id,
credentials_name
FROM databricks_account.provisioning.credentials
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
account_id,
aws_credentials,
creation_time,
credentials_id,
credentials_name
FROM databricks_account.provisioning.credentials
WHERE account_id = '{{ account_id }}' AND
credentials_id = '{{ credentials_id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>credentials</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'credentials', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.provisioning.credentials (
account_id,
data__credentials_name,
data__aws_credentials
)
SELECT 
'{{ account_id }}',
'{{ credentials_name }}',
'{{ aws_credentials }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: credentials_name
    value: credential_1
  - name: aws_credentials
    value:
      sts_role:
        role_arn: arn-aws-iam::111110000000:role/test_role

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>credentials</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.provisioning.credentials
WHERE account_id = '{{ account_id }}' AND
credentials_id = '{{ credentials_id }}';
```
