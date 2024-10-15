---
title: session_host_managements
hide_title: false
hide_table_of_contents: false
keywords:
  - session_host_managements
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>session_host_managements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>session_host_managements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.session_host_managements" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_session_host_managements', value: 'view', },
        { label: 'session_host_managements', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="hostPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_date_time_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="update" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Session host Managements of HostPool. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Get a SessionHostManagement. |
| <CopyableCode code="list_by_host_pool" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | List SessionHostManagements by hostPool. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a SessionHostManagement. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Update a SessionHostManagement. |

## `SELECT` examples

Get a SessionHostManagement.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_session_host_managements', value: 'view', },
        { label: 'session_host_managements', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
hostPoolName,
resourceGroupName,
scheduled_date_time_zone,
subscriptionId,
update
FROM azure.desktop_virtualization.vw_session_host_managements
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.desktop_virtualization.session_host_managements
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>session_host_managements</code> resource.

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
INSERT INTO azure.desktop_virtualization.session_host_managements (
hostPoolName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ hostPoolName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: scheduledDateTimeZone
          value: string
        - name: update
          value:
            - name: deleteOriginalVm
              value: boolean
            - name: maxVmsRemoved
              value: integer
            - name: logOffDelayMinutes
              value: integer
            - name: logOffMessage
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>session_host_managements</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.session_host_managements
SET 
properties = '{{ properties }}'
WHERE 
hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
