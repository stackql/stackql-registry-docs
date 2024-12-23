---
title: vpc_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - vpc_endpoints
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

Operations on a <code>vpc_endpoints</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.vpc_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="account_id" /> | `string` |
| <CopyableCode code="aws_account_id" /> | `string` |
| <CopyableCode code="aws_endpoint_service_id" /> | `string` |
| <CopyableCode code="aws_vpc_endpoint_id" /> | `string` |
| <CopyableCode code="region" /> | `string` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="use_case" /> | `string` |
| <CopyableCode code="vpc_endpoint_id" /> | `string` |
| <CopyableCode code="vpc_endpoint_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, vpc_endpoint_id" /> | Gets a VPC endpoint configuration, which represents a |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets a list of all VPC endpoints for an account, specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a VPC endpoint configuration, which represents a |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, vpc_endpoint_id" /> | Deletes a VPC endpoint configuration, which represents an |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'vpc_endpoints (list)', value: 'list' },
        { label: 'vpc_endpoints (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
account_id,
aws_account_id,
aws_endpoint_service_id,
aws_vpc_endpoint_id,
region,
state,
use_case,
vpc_endpoint_id,
vpc_endpoint_name
FROM databricks_account.provisioning.vpc_endpoints
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
account_id,
aws_account_id,
aws_endpoint_service_id,
aws_vpc_endpoint_id,
region,
state,
use_case,
vpc_endpoint_id,
vpc_endpoint_name
FROM databricks_account.provisioning.vpc_endpoints
WHERE account_id = '{{ account_id }}' AND
vpc_endpoint_id = '{{ vpc_endpoint_id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_endpoints</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'vpc_endpoints', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.provisioning.vpc_endpoints (
account_id,
data__vpc_endpoint_name,
data__aws_vpc_endpoint_id,
data__region
)
SELECT 
'{{ account_id }}',
'{{ vpc_endpoint_name }}',
'{{ aws_vpc_endpoint_id }}',
'{{ region }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: vpc_endpoint_name
    value: string
  - name: aws_vpc_endpoint_id
    value: string
  - name: region
    value: string

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>vpc_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.provisioning.vpc_endpoints
WHERE account_id = '{{ account_id }}' AND
vpc_endpoint_id = '{{ vpc_endpoint_id }}';
```
