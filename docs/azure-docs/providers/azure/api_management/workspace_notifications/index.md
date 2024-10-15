---
title: workspace_notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_notifications
  - api_management
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

Creates, updates, deletes, gets or lists a <code>workspace_notifications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_notifications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_notifications', value: 'view', },
        { label: 'workspace_notifications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="notificationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="recipients" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Notification Contract properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="notificationName, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the details of the Notification specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of properties defined within a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="notificationName, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Create or Update API Management publisher notification for the workspace. |

## `SELECT` examples

Lists a collection of properties defined within a service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_notifications', value: 'view', },
        { label: 'workspace_notifications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
notificationName,
recipients,
resourceGroupName,
serviceName,
subscriptionId,
title,
workspaceId
FROM azure.api_management.vw_workspace_notifications
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.workspace_notifications
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_notifications</code> resource.

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
INSERT INTO azure.api_management.workspace_notifications (
notificationName,
resourceGroupName,
serviceName,
subscriptionId,
workspaceId
)
SELECT 
'{{ notificationName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ workspaceId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>
