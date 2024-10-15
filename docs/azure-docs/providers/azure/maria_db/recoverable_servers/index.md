---
title: recoverable_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - recoverable_servers
  - maria_db
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

Creates, updates, deletes, gets or lists a <code>recoverable_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recoverable_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.recoverable_servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recoverable_servers', value: 'view', },
        { label: 'recoverable_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="edition" /> | `text` | field from the `properties` object |
| <CopyableCode code="hardware_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_available_backup_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_level_objective" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_core" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The recoverable server's properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a recoverable MariaDB Server. |

## `SELECT` examples

Gets a recoverable MariaDB Server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recoverable_servers', value: 'view', },
        { label: 'recoverable_servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
edition,
hardware_generation,
last_available_backup_date_time,
resourceGroupName,
serverName,
service_level_objective,
subscriptionId,
v_core,
version
FROM azure.maria_db.vw_recoverable_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.maria_db.recoverable_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

