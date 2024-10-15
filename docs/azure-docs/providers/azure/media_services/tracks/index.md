---
title: tracks
hide_title: false
hide_table_of_contents: false
keywords:
  - tracks
  - media_services
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

Creates, updates, deletes, gets or lists a <code>tracks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tracks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.tracks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tracks', value: 'view', },
        { label: 'tracks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="assetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="track" /> | `text` | field from the `properties` object |
| <CopyableCode code="trackName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a video, audio or text track in the asset. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, assetName, resourceGroupName, subscriptionId, trackName" /> | Get the details of a Track in the Asset |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, assetName, resourceGroupName, subscriptionId" /> | Lists the Tracks in the asset |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, assetName, resourceGroupName, subscriptionId, trackName" /> | Create or update a Track in the asset |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, assetName, resourceGroupName, subscriptionId, trackName" /> | Deletes a Track in the asset |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, assetName, resourceGroupName, subscriptionId, trackName" /> | Updates an existing Track in the asset |

## `SELECT` examples

Lists the Tracks in the asset

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tracks', value: 'view', },
        { label: 'tracks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
assetName,
provisioning_state,
resourceGroupName,
subscriptionId,
track,
trackName
FROM azure.media_services.vw_tracks
WHERE accountName = '{{ accountName }}'
AND assetName = '{{ assetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.media_services.tracks
WHERE accountName = '{{ accountName }}'
AND assetName = '{{ assetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tracks</code> resource.

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
INSERT INTO azure.media_services.tracks (
accountName,
assetName,
resourceGroupName,
subscriptionId,
trackName,
properties
)
SELECT 
'{{ accountName }}',
'{{ assetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ trackName }}',
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
        - name: track
          value:
            - name: '@odata.type'
              value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tracks</code> resource.

```sql
/*+ update */
UPDATE azure.media_services.tracks
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND assetName = '{{ assetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trackName = '{{ trackName }}';
```

## `DELETE` example

Deletes the specified <code>tracks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.media_services.tracks
WHERE accountName = '{{ accountName }}'
AND assetName = '{{ assetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trackName = '{{ trackName }}';
```
