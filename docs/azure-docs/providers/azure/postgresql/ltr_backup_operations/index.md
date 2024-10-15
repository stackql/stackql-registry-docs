---
title: ltr_backup_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - ltr_backup_operations
  - postgresql
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

Creates, updates, deletes, gets or lists a <code>ltr_backup_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ltr_backup_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql.ltr_backup_operations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ltr_backup_operations', value: 'view', },
        { label: 'ltr_backup_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="backupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_transferred_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="datasource_size_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="percent_complete" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Response for the backup request. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupName, resourceGroupName, serverName, subscriptionId" /> | Gets the result of the give long term retention backup operation for the flexible server. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets the result of the give long term retention backup operations for the flexible server. |

## `SELECT` examples

Gets the result of the give long term retention backup operations for the flexible server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ltr_backup_operations', value: 'view', },
        { label: 'ltr_backup_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
backupName,
backup_metadata,
backup_name,
data_transferred_in_bytes,
datasource_size_in_bytes,
end_time,
error_code,
error_message,
percent_complete,
resourceGroupName,
serverName,
start_time,
status,
subscriptionId
FROM azure.postgresql.vw_ltr_backup_operations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.postgresql.ltr_backup_operations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

