---
title: watchlist_items
hide_title: false
hide_table_of_contents: false
keywords:
  - watchlist_items
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

Creates, updates, deletes, gets or lists a <code>watchlist_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchlist_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.watchlist_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_watchlist_items', value: 'view', },
        { label: 'watchlist_items', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="entity_mapping" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="is_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="items_key_value" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="watchlistAlias" /> | `text` | field from the `properties` object |
| <CopyableCode code="watchlistItemId" /> | `text` | field from the `properties` object |
| <CopyableCode code="watchlist_item_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="watchlist_item_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Describes watchlist item properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, watchlistAlias, watchlistItemId, workspaceName" /> | Get a watchlist item. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, watchlistAlias, workspaceName" /> | Get all watchlist Items. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, watchlistAlias, watchlistItemId, workspaceName" /> | Create or update a watchlist item. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, watchlistAlias, watchlistItemId, workspaceName" /> | Delete a watchlist item. |

## `SELECT` examples

Get all watchlist Items.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_watchlist_items', value: 'view', },
        { label: 'watchlist_items', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
created,
created_by,
entity_mapping,
etag,
is_deleted,
items_key_value,
resourceGroupName,
subscriptionId,
tenant_id,
updated,
updated_by,
watchlistAlias,
watchlistItemId,
watchlist_item_id,
watchlist_item_type,
workspaceName
FROM azure.sentinel.vw_watchlist_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watchlistAlias = '{{ watchlistAlias }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.sentinel.watchlist_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watchlistAlias = '{{ watchlistAlias }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>watchlist_items</code> resource.

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
INSERT INTO azure.sentinel.watchlist_items (
resourceGroupName,
subscriptionId,
watchlistAlias,
watchlistItemId,
workspaceName,
etag,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ watchlistAlias }}',
'{{ watchlistItemId }}',
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
        - name: watchlistItemType
          value: string
        - name: watchlistItemId
          value: string
        - name: tenantId
          value: string
        - name: isDeleted
          value: boolean
        - name: created
          value: string
        - name: updated
          value: string
        - name: createdBy
          value:
            - name: email
              value: string
            - name: name
              value: string
            - name: objectId
              value: string
        - name: itemsKeyValue
          value: object
        - name: entityMapping
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>watchlist_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.watchlist_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watchlistAlias = '{{ watchlistAlias }}'
AND watchlistItemId = '{{ watchlistItemId }}'
AND workspaceName = '{{ workspaceName }}';
```
