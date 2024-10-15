---
title: long_running_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - long_running_backups
  - mysql
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

Creates, updates, deletes, gets or lists a <code>long_running_backups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>long_running_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.long_running_backups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_long_running_backups', value: 'view', },
        { label: 'long_running_backups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="backupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_name_v2" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="completed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a server backup. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupName, resourceGroupName, serverName, subscriptionId" /> | Get backup for a given server. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | List all the backups for a given server. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="backupName, resourceGroupName, serverName, subscriptionId" /> | Create backup for a given server with specified backup name. |

## `SELECT` examples

List all the backups for a given server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_long_running_backups', value: 'view', },
        { label: 'long_running_backups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
backupName,
backup_name_v2,
backup_type,
completed_time,
provisioning_state,
resourceGroupName,
serverName,
source,
subscriptionId
FROM azure.mysql.vw_long_running_backups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.mysql.long_running_backups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>long_running_backups</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.mysql.long_running_backups (
backupName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ backupName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: backupNameV2
          value: string
        - name: backupType
          value: string
        - name: completedTime
          value: string
        - name: source
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>
