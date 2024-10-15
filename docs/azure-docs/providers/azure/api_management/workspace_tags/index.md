---
title: workspace_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_tags
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

Creates, updates, deletes, gets or lists a <code>workspace_tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_tags" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_tags', value: 'view', },
        { label: 'workspace_tags', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tagId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Tag contract Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, tagId, workspaceId" /> | Gets the details of the tag specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of tags defined within a workspace in a service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, tagId, workspaceId" /> | Creates a tag. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, subscriptionId, tagId, workspaceId" /> | Deletes specific tag of the workspace in an API Management service instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, subscriptionId, tagId, workspaceId" /> | Updates the details of the tag specified by its identifier. |

## `SELECT` examples

Lists a collection of tags defined within a workspace in a service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_tags', value: 'view', },
        { label: 'workspace_tags', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
display_name,
resourceGroupName,
serviceName,
subscriptionId,
tagId,
workspaceId
FROM azure.api_management.vw_workspace_tags
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
FROM azure.api_management.workspace_tags
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_tags</code> resource.

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
INSERT INTO azure.api_management.workspace_tags (
resourceGroupName,
serviceName,
subscriptionId,
tagId,
workspaceId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ tagId }}',
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspace_tags</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.workspace_tags
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tagId = '{{ tagId }}'
AND workspaceId = '{{ workspaceId }}';
```

## `DELETE` example

Deletes the specified <code>workspace_tags</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.workspace_tags
WHERE If-Match = '{{ If-Match }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tagId = '{{ tagId }}'
AND workspaceId = '{{ workspaceId }}';
```
