---
title: incident_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_comments
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

Creates, updates, deletes, gets or lists a <code>incident_comments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>incident_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.incident_comments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_incident_comments', value: 'view', },
        { label: 'incident_comments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="author" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="incidentCommentId" /> | `text` | field from the `properties` object |
| <CopyableCode code="incidentId" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="message" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Incident comment property bag. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets a comment for a given incident. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets all comments for a given incident. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a comment for a given incident. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a comment for a given incident. |

## `SELECT` examples

Gets all comments for a given incident.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_incident_comments', value: 'view', },
        { label: 'incident_comments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
author,
created_time_utc,
etag,
incidentCommentId,
incidentId,
last_modified_time_utc,
message,
resourceGroupName,
subscriptionId,
workspaceName
FROM azure.sentinel.vw_incident_comments
WHERE incidentId = '{{ incidentId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.sentinel.incident_comments
WHERE incidentId = '{{ incidentId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>incident_comments</code> resource.

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
INSERT INTO azure.sentinel.incident_comments (
incidentCommentId,
incidentId,
resourceGroupName,
subscriptionId,
workspaceName,
etag,
properties
)
SELECT 
'{{ incidentCommentId }}',
'{{ incidentId }}',
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
        - name: createdTimeUtc
          value: string
        - name: lastModifiedTimeUtc
          value: string
        - name: message
          value: string
        - name: author
          value:
            - name: email
              value: string
            - name: name
              value: string
            - name: objectId
              value: string
            - name: userPrincipalName
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>incident_comments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.incident_comments
WHERE incidentCommentId = '{{ incidentCommentId }}'
AND incidentId = '{{ incidentId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
