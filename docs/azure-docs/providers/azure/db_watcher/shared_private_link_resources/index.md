---
title: shared_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_private_link_resources
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

Creates, updates, deletes, gets or lists a <code>shared_private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shared_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.db_watcher.shared_private_link_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_private_link_resources', value: 'view', },
        { label: 'shared_private_link_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dns_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sharedPrivateLinkResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="watcherName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The generic properties of a Shared Private Link resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sharedPrivateLinkResourceName, subscriptionId, watcherName" /> | Get a SharedPrivateLinkResource |
| <CopyableCode code="list_by_watcher" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, watcherName" /> | List SharedPrivateLinkResource resources by Watcher |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sharedPrivateLinkResourceName, subscriptionId, watcherName" /> | Create a SharedPrivateLinkResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sharedPrivateLinkResourceName, subscriptionId, watcherName" /> | Delete a SharedPrivateLinkResource |

## `SELECT` examples

List SharedPrivateLinkResource resources by Watcher

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_private_link_resources', value: 'view', },
        { label: 'shared_private_link_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dns_zone,
group_id,
private_link_resource_id,
provisioning_state,
request_message,
resourceGroupName,
sharedPrivateLinkResourceName,
status,
subscriptionId,
watcherName
FROM azure.db_watcher.vw_shared_private_link_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.db_watcher.shared_private_link_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>shared_private_link_resources</code> resource.

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
INSERT INTO azure.db_watcher.shared_private_link_resources (
resourceGroupName,
sharedPrivateLinkResourceName,
subscriptionId,
watcherName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sharedPrivateLinkResourceName }}',
'{{ subscriptionId }}',
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
        - name: privateLinkResourceId
          value: string
        - name: groupId
          value: string
        - name: requestMessage
          value: string
        - name: dnsZone
          value: string
        - name: status
          value: []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>shared_private_link_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.db_watcher.shared_private_link_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sharedPrivateLinkResourceName = '{{ sharedPrivateLinkResourceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watcherName = '{{ watcherName }}';
```
