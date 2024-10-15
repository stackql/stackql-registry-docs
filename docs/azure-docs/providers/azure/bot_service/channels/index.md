---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - bot_service
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.channels" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Specifies the resource ID. |
| <CopyableCode code="name" /> | `text` | Specifies the name of the resource. |
| <CopyableCode code="channelName" /> | `text` | field from the `properties` object |
| <CopyableCode code="channel_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Entity Tag. |
| <CopyableCode code="kind" /> | `text` | Indicates the type of bot service |
| <CopyableCode code="location" /> | `text` | Specifies the location of the resource. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The SKU of the cognitive services account. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="type" /> | `text` | Specifies the type of the resource. |
| <CopyableCode code="zones" /> | `text` | Entity zones |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource ID. |
| <CopyableCode code="name" /> | `string` | Specifies the name of the resource. |
| <CopyableCode code="etag" /> | `string` | Entity Tag. |
| <CopyableCode code="kind" /> | `string` | Indicates the type of bot service |
| <CopyableCode code="location" /> | `string` | Specifies the location of the resource. |
| <CopyableCode code="properties" /> | `object` | Channel definition |
| <CopyableCode code="sku" /> | `object` | The SKU of the cognitive services account. |
| <CopyableCode code="tags" /> | `object` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the resource. |
| <CopyableCode code="zones" /> | `array` | Entity zones |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="channelName, resourceGroupName, resourceName, subscriptionId" /> | Returns a BotService Channel registration specified by the parameters. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns all the Channel registrations of a particular BotService resource |
| <CopyableCode code="list_with_keys" /> | `SELECT` | <CopyableCode code="channelName, resourceGroupName, resourceName, subscriptionId" /> | Lists a Channel registration for a Bot Service including secrets |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="channelName, resourceGroupName, resourceName, subscriptionId" /> | Creates a Channel registration for a Bot Service |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="channelName, resourceGroupName, resourceName, subscriptionId" /> | Deletes a Channel registration from a Bot Service |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="channelName, resourceGroupName, resourceName, subscriptionId" /> | Updates a Channel registration for a Bot Service |

## `SELECT` examples

Returns all the Channel registrations of a particular BotService resource

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
id,
name,
channelName,
channel_name,
etag,
kind,
location,
provisioning_state,
resourceGroupName,
resourceName,
sku,
subscriptionId,
tags,
type,
zones
FROM azure.bot_service.vw_channels
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
kind,
location,
properties,
sku,
tags,
type,
zones
FROM azure.bot_service.channels
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
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
INSERT INTO azure.bot_service.channels (
channelName,
resourceGroupName,
resourceName,
subscriptionId,
location,
tags,
sku,
kind,
etag,
properties
)
SELECT 
'{{ channelName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ kind }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: []
        - name: tier
          value: string
    - name: kind
      value: []
    - name: etag
      value: string
    - name: zones
      value:
        - string
    - name: properties
      value:
        - name: channelName
          value: string
        - name: etag
          value: string
        - name: provisioningState
          value: string
        - name: location
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>channels</code> resource.

```sql
/*+ update */
UPDATE azure.bot_service.channels
SET 
location = '{{ location }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
kind = '{{ kind }}',
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
channelName = '{{ channelName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>channels</code> resource.

```sql
/*+ delete */
DELETE FROM azure.bot_service.channels
WHERE channelName = '{{ channelName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
