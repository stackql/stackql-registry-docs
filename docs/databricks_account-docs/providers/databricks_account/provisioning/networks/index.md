---
title: networks
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - networks
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

Operations on a <code>networks</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.provisioning.networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="account_id" /> | `string` |
| <CopyableCode code="creation_time" /> | `integer` |
| <CopyableCode code="error_messages" /> | `array` |
| <CopyableCode code="network_id" /> | `string` |
| <CopyableCode code="network_name" /> | `string` |
| <CopyableCode code="security_group_ids" /> | `array` |
| <CopyableCode code="subnet_ids" /> | `array` |
| <CopyableCode code="vpc_endpoints" /> | `object` |
| <CopyableCode code="vpc_id" /> | `string` |
| <CopyableCode code="vpc_status" /> | `string` |
| <CopyableCode code="warning_messages" /> | `array` |
| <CopyableCode code="workspace_id" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, network_id" /> | Gets a Databricks network configuration, which represents an AWS VPC and its resources.  This requires a pre-existing VPC and subnets. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets a list of all Databricks network configurations for an account, specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a Databricks network configuration that represents an AWS VPC and its resources. The VPC will be used for new Databricks clusters. This requires a pre-existing VPC and subnets. For VPC requirements, see |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, network_id" /> | Deletes a Databricks network configuration, which represents a cloud VPC and its resources. You cannot delete a network that is associated with a workspace. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'networks (list)', value: 'list' },
        { label: 'networks (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
account_id,
creation_time,
error_messages,
network_id,
network_name,
security_group_ids,
subnet_ids,
vpc_endpoints,
vpc_id,
vpc_status,
warning_messages,
workspace_id
FROM databricks_account.provisioning.networks
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
account_id,
creation_time,
error_messages,
network_id,
network_name,
security_group_ids,
subnet_ids,
vpc_endpoints,
vpc_id,
vpc_status,
warning_messages,
workspace_id
FROM databricks_account.provisioning.networks
WHERE account_id = '{{ account_id }}' AND
network_id = '{{ network_id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>networks</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'networks', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.provisioning.networks (
account_id,
data__network_name,
data__vpc_id,
data__subnet_ids,
data__security_group_ids,
data__vpc_endpoints
)
SELECT 
'{{ account_id }}',
'{{ network_name }}',
'{{ vpc_id }}',
'{{ subnet_ids }}',
'{{ security_group_ids }}',
'{{ vpc_endpoints }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: network_name
    value: string
  - name: vpc_id
    value: string
  - name: subnet_ids
    value:
    - string
  - name: security_group_ids
    value:
    - string
  - name: vpc_endpoints
    value:
      rest_api:
      - 497f6eca-6276-4993-bfeb-53cbbbba6f08
      dataplane_relay:
      - 497f6eca-6276-4993-bfeb-53cbbbba6f08

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>networks</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.provisioning.networks
WHERE account_id = '{{ account_id }}' AND
network_id = '{{ network_id }}';
```
