---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - engagement_fabric
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

Creates, updates, deletes, gets or lists a <code>channels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.engagement_fabric.channels" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_channels', value: 'view', },
        { label: 'channels', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="channelName" /> | `text` | field from the `properties` object |
| <CopyableCode code="channel_functions" /> | `text` | field from the `properties` object |
| <CopyableCode code="channel_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The EngagementFabric channel properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, channelName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, channelName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, channelName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_channels', value: 'view', },
        { label: 'channels', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
channelName,
channel_functions,
channel_type,
credentials,
resourceGroupName,
subscriptionId
FROM azure.engagement_fabric.vw_channels
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.engagement_fabric.channels
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>channels</code> resource.

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
INSERT INTO azure.engagement_fabric.channels (
accountName,
channelName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ channelName }}',
'{{ resourceGroupName }}',
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
        - name: channelType
          value: string
        - name: channelFunctions
          value:
            - string
        - name: credentials
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>channels</code> resource.

```sql
/*+ delete */
DELETE FROM azure.engagement_fabric.channels
WHERE accountName = '{{ accountName }}'
AND channelName = '{{ channelName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
