---
title: log_delivery
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - log_delivery
  - logging
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

Operations on a <code>log_delivery</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_delivery</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.logging.log_delivery" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="account_id" /> | `string` |
| <CopyableCode code="config_id" /> | `string` |
| <CopyableCode code="config_name" /> | `string` |
| <CopyableCode code="creation_time" /> | `integer` |
| <CopyableCode code="credentials_id" /> | `string` |
| <CopyableCode code="delivery_path_prefix" /> | `string` |
| <CopyableCode code="delivery_start_time" /> | `string` |
| <CopyableCode code="log_delivery_status" /> | `object` |
| <CopyableCode code="log_type" /> | `string` |
| <CopyableCode code="output_format" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="storage_configuration_id" /> | `string` |
| <CopyableCode code="update_time" /> | `integer` |
| <CopyableCode code="workspace_ids_filter" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, log_delivery_configuration_id" /> | Gets a Databricks log delivery configuration object for an account, both specified by ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets all Databricks log delivery configurations associated with an account specified by ID. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a new Databricks log delivery configuration to enable delivery of the specified type of logs to your storage location. This requires that you already created a |
| <CopyableCode code="patchstatus" /> | `EXEC` | <CopyableCode code="account_id, log_delivery_configuration_id" /> | Enables or disables a log delivery configuration. Deletion of delivery configurations is not supported, so disable log delivery configurations that are no longer needed. Note that you can't re-enable a delivery configuration if this would violate the delivery configuration limits described under |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'log_delivery (list)', value: 'list' },
        { label: 'log_delivery (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
account_id,
config_id,
config_name,
creation_time,
credentials_id,
delivery_path_prefix,
delivery_start_time,
log_delivery_status,
log_type,
output_format,
status,
storage_configuration_id,
update_time,
workspace_ids_filter
FROM databricks_account.logging.log_delivery
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
account_id,
config_id,
config_name,
creation_time,
credentials_id,
delivery_path_prefix,
delivery_start_time,
log_delivery_status,
log_type,
output_format,
status,
storage_configuration_id,
update_time,
workspace_ids_filter
FROM databricks_account.logging.log_delivery
WHERE account_id = '{{ account_id }}' AND
log_delivery_configuration_id = '{{ log_delivery_configuration_id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>log_delivery</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'log_delivery', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.logging.log_delivery (
account_id,
data__log_delivery_configuration
)
SELECT 
'{{ account_id }}',
'{{ log_delivery_configuration }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: log_delivery_configuration
    value:
      config_name: string
      status: ENABLED
      log_type: BILLABLE_USAGE
      output_format: CSV
      credentials_id: c7814269-df58-4ca3-85e9-f6672ef43d77
      storage_configuration_id: 04aae505-1b1e-4cb9-997d-e1c49282675d
      workspace_ids_filter:
      - 0
      delivery_path_prefix: string
      delivery_start_time: string

```

</TabItem>
</Tabs>
