---
title: incident_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_tasks
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

Creates, updates, deletes, gets or lists a <code>incident_tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>incident_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.incident_tasks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_incident_tasks', value: 'view', },
        { label: 'incident_tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="incidentId" /> | `text` | field from the `properties` object |
| <CopyableCode code="incidentTaskId" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an incident task |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="incidentId, incidentTaskId, resourceGroupName, subscriptionId, workspaceName" /> | Gets an incident task. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets all incident tasks. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="incidentId, incidentTaskId, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Creates or updates the incident task. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="incidentId, incidentTaskId, resourceGroupName, subscriptionId, workspaceName" /> | Delete the incident task. |

## `SELECT` examples

Gets all incident tasks.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_incident_tasks', value: 'view', },
        { label: 'incident_tasks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
created_by,
created_time_utc,
etag,
incidentId,
incidentTaskId,
last_modified_by,
last_modified_time_utc,
resourceGroupName,
status,
subscriptionId,
title,
workspaceName
FROM azure.sentinel.vw_incident_tasks
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
FROM azure.sentinel.incident_tasks
WHERE incidentId = '{{ incidentId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>incident_tasks</code> resource.

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
INSERT INTO azure.sentinel.incident_tasks (
incidentId,
incidentTaskId,
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
etag,
properties
)
SELECT 
'{{ incidentId }}',
'{{ incidentTaskId }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
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
        - name: title
          value: string
        - name: description
          value: string
        - name: status
          value: []
        - name: createdTimeUtc
          value: string
        - name: lastModifiedTimeUtc
          value: string
        - name: createdBy
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

Deletes the specified <code>incident_tasks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.incident_tasks
WHERE incidentId = '{{ incidentId }}'
AND incidentTaskId = '{{ incidentTaskId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
