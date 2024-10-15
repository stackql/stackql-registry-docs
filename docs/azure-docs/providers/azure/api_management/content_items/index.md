---
title: content_items
hide_title: false
hide_table_of_contents: false
keywords:
  - content_items
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

Creates, updates, deletes, gets or lists a <code>content_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>content_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.content_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_content_items', value: 'view', },
        { label: 'content_items', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentItemId" /> | `text` | field from the `properties` object |
| <CopyableCode code="contentTypeId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Returns the developer portal's content item specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Lists developer portal's content items specified by the provided content type. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new developer portal's content item specified by the provided content type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, contentItemId, contentTypeId, resourceGroupName, serviceName, subscriptionId" /> | Removes the specified developer portal's content item. |

## `SELECT` examples

Lists developer portal's content items specified by the provided content type.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_content_items', value: 'view', },
        { label: 'content_items', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
contentItemId,
contentTypeId,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.api_management.vw_content_items
WHERE contentTypeId = '{{ contentTypeId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.content_items
WHERE contentTypeId = '{{ contentTypeId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>content_items</code> resource.

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
INSERT INTO azure.api_management.content_items (
contentItemId,
contentTypeId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ contentItemId }}',
'{{ contentTypeId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>content_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.content_items
WHERE If-Match = '{{ If-Match }}'
AND contentItemId = '{{ contentItemId }}'
AND contentTypeId = '{{ contentTypeId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
