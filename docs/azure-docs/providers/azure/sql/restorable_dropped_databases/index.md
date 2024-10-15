---
title: restorable_dropped_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_dropped_databases
  - sql
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>restorable_dropped_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restorable_dropped_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.restorable_dropped_databases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restorable_dropped_databases', value: 'view', },
        { label: 'restorable_dropped_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="backup_storage_redundancy" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="earliest_restore_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="max_size_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorableDroppedDatabaseId" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | An ARM Resource SKU. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The restorable dropped database's properties. |
| <CopyableCode code="sku" /> | `object` | An ARM Resource SKU. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, restorableDroppedDatabaseId, serverName, subscriptionId" /> | Gets a restorable dropped database. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of restorable dropped databases. |

## `SELECT` examples

Gets a list of restorable dropped databases.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restorable_dropped_databases', value: 'view', },
        { label: 'restorable_dropped_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
backup_storage_redundancy,
creation_date,
database_name,
deletion_date,
earliest_restore_date,
keys,
location,
max_size_bytes,
resourceGroupName,
restorableDroppedDatabaseId,
serverName,
sku,
subscriptionId,
tags
FROM azure.sql.vw_restorable_dropped_databases
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure.sql.restorable_dropped_databases
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

