---
title: recoverable_managed_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - recoverable_managed_databases
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

Creates, updates, deletes, gets or lists a <code>recoverable_managed_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recoverable_managed_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.recoverable_managed_databases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recoverable_managed_databases', value: 'view', },
        { label: 'recoverable_managed_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="last_available_backup_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="recoverableDatabaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The recoverable managed database's properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, recoverableDatabaseName, resourceGroupName, subscriptionId" /> | Gets a recoverable managed database. |

## `SELECT` examples

Gets a recoverable managed database.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recoverable_managed_databases', value: 'view', },
        { label: 'recoverable_managed_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
last_available_backup_date,
managedInstanceName,
recoverableDatabaseName,
resourceGroupName,
subscriptionId
FROM azure.sql.vw_recoverable_managed_databases
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND recoverableDatabaseName = '{{ recoverableDatabaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.recoverable_managed_databases
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND recoverableDatabaseName = '{{ recoverableDatabaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

