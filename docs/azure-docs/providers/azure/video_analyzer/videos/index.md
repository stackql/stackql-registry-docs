---
title: videos
hide_title: false
hide_table_of_contents: false
keywords:
  - videos
  - video_analyzer
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

Creates, updates, deletes, gets or lists a <code>videos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>videos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.videos" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_videos', value: 'view', },
        { label: 'videos', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="archival" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_urls" /> | `text` | field from the `properties` object |
| <CopyableCode code="flags" /> | `text` | field from the `properties` object |
| <CopyableCode code="media_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
| <CopyableCode code="videoName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Application level properties for the video resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, videoName" /> | Retrieves an existing video resource with the given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves a list of video resources that have been created, along with their JSON representations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, videoName" /> | Creates a new video resource or updates an existing video resource with the given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, videoName" /> | Deletes an existing video resource and its underlying data. This operation is irreversible. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, videoName" /> | Updates individual properties of an existing video resource with the given name. |

## `SELECT` examples

Retrieves a list of video resources that have been created, along with their JSON representations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_videos', value: 'view', },
        { label: 'videos', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
accountName,
archival,
content_urls,
flags,
media_info,
resourceGroupName,
subscriptionId,
title,
type,
videoName
FROM azure.video_analyzer.vw_videos
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.video_analyzer.videos
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>videos</code> resource.

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
INSERT INTO azure.video_analyzer.videos (
accountName,
resourceGroupName,
subscriptionId,
videoName,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ videoName }}',
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
        - name: title
          value: string
        - name: description
          value: string
        - name: type
          value: string
        - name: flags
          value:
            - name: canStream
              value: boolean
            - name: hasData
              value: boolean
            - name: isInUse
              value: boolean
        - name: contentUrls
          value:
            - name: downloadUrl
              value: string
            - name: archiveBaseUrl
              value: string
            - name: rtspTunnelUrl
              value: string
            - name: previewImageUrls
              value:
                - name: small
                  value: string
                - name: medium
                  value: string
                - name: large
                  value: string
        - name: mediaInfo
          value:
            - name: segmentLength
              value: string
        - name: archival
          value:
            - name: retentionPeriod
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>videos</code> resource.

```sql
/*+ update */
UPDATE azure.video_analyzer.videos
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND videoName = '{{ videoName }}';
```

## `DELETE` example

Deletes the specified <code>videos</code> resource.

```sql
/*+ delete */
DELETE FROM azure.video_analyzer.videos
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND videoName = '{{ videoName }}';
```
