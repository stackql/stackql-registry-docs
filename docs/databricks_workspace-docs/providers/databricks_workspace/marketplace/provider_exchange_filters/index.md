---
title: provider_exchange_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - provider_exchange_filters
  - marketplace
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

Operations on a <code>provider_exchange_filters</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_exchange_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_exchange_filters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="exchange_id" /> | `string` |
| <CopyableCode code="filter_type" /> | `string` |
| <CopyableCode code="filter_value" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="exchange_id, deployment_name" /> | List exchange filter |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Add an exchange filter. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Delete an exchange filter |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Update an exchange filter. |

## `SELECT` examples

```sql
SELECT
id,
name,
created_at,
created_by,
exchange_id,
filter_type,
filter_value,
updated_at,
updated_by
FROM databricks_workspace.marketplace.provider_exchange_filters
WHERE exchange_id = '{{ exchange_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provider_exchange_filters</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'provider_exchange_filters', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.marketplace.provider_exchange_filters (
deployment_name,
data__filter
)
SELECT 
'{{ deployment_name }}',
'{{ filter }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: filter
    value:
      id: string
      exchange_id: string
      filter_value: string
      name: string
      created_at: 0
      created_by: string
      updated_at: 0
      updated_by: string
      filter_type: GLOBAL_METASTORE_ID

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>provider_exchange_filters</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.marketplace.provider_exchange_filters
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>provider_exchange_filters</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.marketplace.provider_exchange_filters
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
