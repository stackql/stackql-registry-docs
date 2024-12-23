---
title: provider_exchange_listings
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - provider_exchange_listings
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

Operations on a <code>provider_exchange_listings</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_exchange_listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_exchange_listings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="exchange_id" /> | `string` |
| <CopyableCode code="exchange_name" /> | `string` |
| <CopyableCode code="listing_id" /> | `string` |
| <CopyableCode code="listing_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listexchangesforlisting" /> | `SELECT` | <CopyableCode code="listing_id, deployment_name" /> | List exchanges associated with a listing |
| <CopyableCode code="listlistingsforexchange" /> | `SELECT` | <CopyableCode code="exchange_id, deployment_name" /> | List listings associated with an exchange |
| <CopyableCode code="addlistingtoexchange" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Associate an exchange with a listing |
| <CopyableCode code="deletelistingfromexchange" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Disassociate an exchange with a listing |

## `SELECT` examples

<Tabs
    defaultValue="listexchangesforlisting"
    values={[
        { label: 'provider_exchange_listings (listexchangesforlisting)', value: 'listexchangesforlisting' },
        { label: 'provider_exchange_listings (listlistingsforexchange)', value: 'listlistingsforexchange' }
    ]
}>
<TabItem value="listexchangesforlisting">

```sql
SELECT
id,
created_at,
created_by,
exchange_id,
exchange_name,
listing_id,
listing_name
FROM databricks_workspace.marketplace.provider_exchange_listings
WHERE listing_id = '{{ listing_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="listlistingsforexchange">

```sql
SELECT
id,
created_at,
created_by,
exchange_id,
exchange_name,
listing_id,
listing_name
FROM databricks_workspace.marketplace.provider_exchange_listings
WHERE exchange_id = '{{ exchange_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provider_exchange_listings</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'provider_exchange_listings', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.marketplace.provider_exchange_listings (
deployment_name,
data__listing_id,
data__exchange_id
)
SELECT 
'{{ deployment_name }}',
'{{ listing_id }}',
'{{ exchange_id }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: listing_id
    value: string
  - name: exchange_id
    value: string

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>provider_exchange_listings</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.marketplace.provider_exchange_listings
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
