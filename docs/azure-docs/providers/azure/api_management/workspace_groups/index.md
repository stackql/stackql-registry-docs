---
title: workspace_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_groups
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

Creates, updates, deletes, gets or lists a <code>workspace_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_groups', value: 'view', },
        { label: 'workspace_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="built_in" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="groupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Group contract Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the details of the group specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of groups defined within a workspace in a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates or Updates a group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, groupId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes specific group of the workspace in an API Management service instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, groupId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Updates the details of the group specified by its identifier. |

## `SELECT` examples

Lists a collection of groups defined within a workspace in a service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_groups', value: 'view', },
        { label: 'workspace_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
built_in,
display_name,
external_id,
groupId,
resourceGroupName,
serviceName,
subscriptionId,
type,
workspaceId
FROM azure.api_management.vw_workspace_groups
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
FROM azure.api_management.workspace_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_groups</code> resource.

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
INSERT INTO azure.api_management.workspace_groups (
groupId,
resourceGroupName,
serviceName,
subscriptionId,
workspaceId,
properties
)
SELECT 
'{{ groupId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: displayName
          value: string
        - name: description
          value: string
        - name: type
          value: string
        - name: externalId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspace_groups</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.workspace_groups
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND groupId = '{{ groupId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```

## `DELETE` example

Deletes the specified <code>workspace_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.workspace_groups
WHERE If-Match = '{{ If-Match }}'
AND groupId = '{{ groupId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
