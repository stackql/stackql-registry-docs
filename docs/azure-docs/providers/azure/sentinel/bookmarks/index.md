---
title: bookmarks
hide_title: false
hide_table_of_contents: false
keywords:
  - bookmarks
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>bookmarks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bookmarks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.bookmarks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bookmarks', value: 'view', },
        { label: 'bookmarks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bookmarkId" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="event_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="incident_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="query" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_result" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Describes bookmark properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bookmarkId, resourceGroupName, subscriptionId, workspaceName" /> | Gets a bookmark. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all bookmarks. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bookmarkId, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates the bookmark. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bookmarkId, resourceGroupName, subscriptionId, workspaceName" /> | Delete the bookmark. |

## `SELECT` examples

Gets all bookmarks.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bookmarks', value: 'view', },
        { label: 'bookmarks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
bookmarkId,
created,
created_by,
display_name,
etag,
event_time,
incident_info,
labels,
notes,
query,
query_end_time,
query_result,
query_start_time,
resourceGroupName,
subscriptionId,
updated,
updated_by,
workspaceName
FROM azure.sentinel.vw_bookmarks
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.sentinel.bookmarks
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bookmarks</code> resource.

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
INSERT INTO azure.sentinel.bookmarks (
bookmarkId,
resourceGroupName,
subscriptionId,
workspaceName,
etag,
properties
)
SELECT 
'{{ bookmarkId }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: created
          value: string
        - name: createdBy
          value:
            - name: email
              value: string
            - name: name
              value: string
            - name: objectId
              value: string
        - name: displayName
          value: string
        - name: labels
          value:
            - []
        - name: notes
          value: string
        - name: query
          value: string
        - name: queryResult
          value: string
        - name: updated
          value: string
        - name: eventTime
          value: string
        - name: queryStartTime
          value: string
        - name: queryEndTime
          value: string
        - name: incidentInfo
          value:
            - name: incidentId
              value: string
            - name: severity
              value: []
            - name: title
              value: string
            - name: relationName
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>bookmarks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.bookmarks
WHERE bookmarkId = '{{ bookmarkId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
