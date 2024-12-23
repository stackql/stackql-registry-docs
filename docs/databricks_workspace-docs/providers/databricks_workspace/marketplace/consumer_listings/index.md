---
title: consumer_listings
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - consumer_listings
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

Operations on a <code>consumer_listings</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.consumer_listings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="detail" /> | `object` |
| <CopyableCode code="summary" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Get a published listing in the Databricks Marketplace that the consumer has access to. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List all published listings in the Databricks Marketplace that the consumer has access to. |
| <CopyableCode code="search" /> | `SELECT` | <CopyableCode code="query, deployment_name" /> | Search published listings in the Databricks Marketplace that the consumer has access to. This query supports a variety of different search parameters and performs fuzzy matching. |
| <CopyableCode code="batchget" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Batch get a published listing in the Databricks Marketplace that the consumer has access to. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'consumer_listings (list)', value: 'list' },
        { label: 'consumer_listings (get)', value: 'get' },
        { label: 'consumer_listings (search)', value: 'search' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
detail,
summary
FROM databricks_workspace.marketplace.consumer_listings
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
detail,
summary
FROM databricks_workspace.marketplace.consumer_listings
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="search">

```sql
SELECT
id,
detail,
summary
FROM databricks_workspace.marketplace.consumer_listings
WHERE query = '{{ query }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>
