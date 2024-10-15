---
title: recoverable_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - recoverable_databases
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

Creates, updates, deletes, gets or lists a <code>recoverable_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recoverable_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.recoverable_databases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recoverable_databases', value: 'view', },
        { label: 'recoverable_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="elastic_pool_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_available_backup_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_level_objective" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The recoverable database's properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a recoverable database. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of recoverable databases. |

## `SELECT` examples

Gets a list of recoverable databases.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recoverable_databases', value: 'view', },
        { label: 'recoverable_databases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
edition,
elastic_pool_name,
keys,
last_available_backup_date,
resourceGroupName,
serverName,
service_level_objective,
subscriptionId
FROM azure.sql.vw_recoverable_databases
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.recoverable_databases
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

