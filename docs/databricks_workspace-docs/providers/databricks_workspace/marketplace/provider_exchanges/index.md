---
title: provider_exchanges
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - provider_exchanges
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

Operations on a <code>provider_exchanges</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_exchanges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_exchanges" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="filters" /> | `array` |
| <CopyableCode code="linked_listings" /> | `array` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Get an exchange. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List exchanges visible to provider |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Create an exchange |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | This removes a listing from marketplace. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Update an exchange |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'provider_exchanges (list)', value: 'list' },
        { label: 'provider_exchanges (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
comment,
created_at,
created_by,
filters,
linked_listings,
updated_at,
updated_by
FROM databricks_workspace.marketplace.provider_exchanges
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
comment,
created_at,
created_by,
filters,
linked_listings,
updated_at,
updated_by
FROM databricks_workspace.marketplace.provider_exchanges
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provider_exchanges</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'provider_exchanges', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.marketplace.provider_exchanges (
deployment_name,
data__exchange
)
SELECT 
'{{ deployment_name }}',
'{{ exchange }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: exchange
    value:
      id: string
      name: string
      comment: string
      filters:
      - id: string
        exchange_id: string
        filter_value: string
        name: string
        created_at: 0
        created_by: string
        updated_at: 0
        updated_by: string
        filter_type: GLOBAL_METASTORE_ID
      created_at: 0
      created_by: string
      updated_at: 0
      updated_by: string
      linked_listings:
      - id: string
        exchange_id: string
        exchange_name: string
        listing_id: string
        listing_name: string
        created_at: 0
        created_by: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>provider_exchanges</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.marketplace.provider_exchanges
SET { field = value }
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>provider_exchanges</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.marketplace.provider_exchanges
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
