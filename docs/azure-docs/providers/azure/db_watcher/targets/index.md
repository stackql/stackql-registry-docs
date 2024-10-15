---
title: targets
hide_title: false
hide_table_of_contents: false
keywords:
  - targets
  - db_watcher
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

Creates, updates, deletes, gets or lists a <code>targets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.db_watcher.targets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_targets', value: 'view', },
        { label: 'targets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connection_server_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="targetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_authentication_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_vault" /> | `text` | field from the `properties` object |
| <CopyableCode code="watcherName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The generic properties of a target. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, targetName, watcherName" /> | Get a Target |
| <CopyableCode code="list_by_watcher" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, watcherName" /> | List Target resources by Watcher |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, targetName, watcherName" /> | Create a Target |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, targetName, watcherName" /> | Delete a Target |

## `SELECT` examples

List Target resources by Watcher

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_targets', value: 'view', },
        { label: 'targets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
connection_server_name,
provisioning_state,
resourceGroupName,
subscriptionId,
targetName,
target_authentication_type,
target_type,
target_vault,
watcherName
FROM azure.db_watcher.vw_targets
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.db_watcher.targets
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>targets</code> resource.

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
INSERT INTO azure.db_watcher.targets (
resourceGroupName,
subscriptionId,
targetName,
watcherName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ targetName }}',
'{{ watcherName }}',
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
        - name: targetType
          value: string
        - name: targetAuthenticationType
          value: []
        - name: targetVault
          value:
            - name: akvResourceId
              value: string
            - name: akvTargetUser
              value: string
            - name: akvTargetPassword
              value: string
        - name: connectionServerName
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>targets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.db_watcher.targets
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetName = '{{ targetName }}'
AND watcherName = '{{ watcherName }}';
```
