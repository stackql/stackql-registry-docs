---
title: restorable_dropped_managed_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_dropped_managed_databases
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

Creates, updates, deletes, gets or lists a <code>restorable_dropped_managed_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>restorable_dropped_managed_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.restorable_dropped_managed_databases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restorable_dropped_managed_databases', value: 'view', },
        { label: 'restorable_dropped_managed_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="database_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="deletion_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="earliest_restore_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restorableDroppedDatabaseId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The restorable dropped managed database's properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, restorableDroppedDatabaseId, subscriptionId" /> | Gets a restorable dropped managed database. |

## `SELECT` examples

Gets a restorable dropped managed database.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_restorable_dropped_managed_databases', value: 'view', },
        { label: 'restorable_dropped_managed_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_date,
database_name,
deletion_date,
earliest_restore_date,
location,
managedInstanceName,
resourceGroupName,
restorableDroppedDatabaseId,
subscriptionId,
tags
FROM azure.sql.vw_restorable_dropped_managed_databases
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND restorableDroppedDatabaseId = '{{ restorableDroppedDatabaseId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.sql.restorable_dropped_managed_databases
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND restorableDroppedDatabaseId = '{{ restorableDroppedDatabaseId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

