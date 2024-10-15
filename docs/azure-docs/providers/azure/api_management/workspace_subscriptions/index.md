---
title: workspace_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_subscriptions
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

Creates, updates, deletes, gets or lists a <code>workspace_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_subscriptions', value: 'view', },
        { label: 'workspace_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allow_tracing" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="notification_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="owner_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sid" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="state_comment" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Subscription details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Gets the specified Subscription entity. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists all subscriptions of the workspace in an API Management service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Creates or updates the subscription of specified user to the specified product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Deletes the specified subscription. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Updates the details of a subscription specified by its identifier. |
| <CopyableCode code="regenerate_primary_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Regenerates primary key of existing subscription of the workspace in an API Management service instance. |
| <CopyableCode code="regenerate_secondary_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, sid, subscriptionId, workspaceId" /> | Regenerates secondary key of existing subscription of the workspace in an API Management service instance. |

## `SELECT` examples

Lists all subscriptions of the workspace in an API Management service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_subscriptions', value: 'view', },
        { label: 'workspace_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allow_tracing,
created_date,
display_name,
end_date,
expiration_date,
notification_date,
owner_id,
primary_key,
resourceGroupName,
scope,
secondary_key,
serviceName,
sid,
start_date,
state,
state_comment,
subscriptionId,
workspaceId
FROM azure.api_management.vw_workspace_subscriptions
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
FROM azure.api_management.workspace_subscriptions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_subscriptions</code> resource.

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
INSERT INTO azure.api_management.workspace_subscriptions (
resourceGroupName,
serviceName,
sid,
subscriptionId,
workspaceId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ sid }}',
'{{ subscriptionId }}',
'{{ workspaceId }}',
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
        - name: ownerId
          value: string
        - name: scope
          value: string
        - name: displayName
          value: string
        - name: primaryKey
          value: string
        - name: secondaryKey
          value: string
        - name: state
          value: string
        - name: allowTracing
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspace_subscriptions</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.workspace_subscriptions
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND sid = '{{ sid }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```

## `DELETE` example

Deletes the specified <code>workspace_subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.workspace_subscriptions
WHERE If-Match = '{{ If-Match }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND sid = '{{ sid }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
