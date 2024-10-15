---
title: watchlists
hide_title: false
hide_table_of_contents: false
keywords:
  - watchlists
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

Creates, updates, deletes, gets or lists a <code>watchlists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchlists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.watchlists" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_watchlists', value: 'view', },
        { label: 'watchlists', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="is_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="items_search_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_lines_to_skip" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider" /> | `text` | field from the `properties` object |
| <CopyableCode code="raw_content" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="upload_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="watchlistAlias" /> | `text` | field from the `properties` object |
| <CopyableCode code="watchlist_alias" /> | `text` | field from the `properties` object |
| <CopyableCode code="watchlist_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="watchlist_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Describes watchlist properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, watchlistAlias, workspaceName" /> | Get a watchlist, without its watchlist items. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Get all watchlists, without watchlist items. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, watchlistAlias, workspaceName" /> | Create or update a Watchlist and its Watchlist Items (bulk creation, e.g. through text/csv content type). To create a Watchlist and its Items, we should call this endpoint with rawContent and contentType properties. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, watchlistAlias, workspaceName" /> | Delete a watchlist. |

## `SELECT` examples

Get all watchlists, without watchlist items.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_watchlists', value: 'view', },
        { label: 'watchlists', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
content_type,
created,
created_by,
default_duration,
display_name,
etag,
is_deleted,
items_search_key,
labels,
number_of_lines_to_skip,
provider,
raw_content,
resourceGroupName,
source,
subscriptionId,
tenant_id,
updated,
updated_by,
upload_status,
watchlistAlias,
watchlist_alias,
watchlist_id,
watchlist_type,
workspaceName
FROM azure.sentinel.vw_watchlists
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
FROM azure.sentinel.watchlists
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>watchlists</code> resource.

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
INSERT INTO azure.sentinel.watchlists (
resourceGroupName,
subscriptionId,
watchlistAlias,
workspaceName,
etag,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ watchlistAlias }}',
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
        - name: watchlistId
          value: string
        - name: displayName
          value: string
        - name: provider
          value: string
        - name: source
          value: string
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
        - name: description
          value: string
        - name: watchlistType
          value: string
        - name: watchlistAlias
          value: string
        - name: isDeleted
          value: boolean
        - name: labels
          value:
            - []
        - name: defaultDuration
          value: string
        - name: tenantId
          value: string
        - name: numberOfLinesToSkip
          value: integer
        - name: rawContent
          value: string
        - name: itemsSearchKey
          value: string
        - name: contentType
          value: string
        - name: uploadStatus
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>watchlists</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.watchlists
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND watchlistAlias = '{{ watchlistAlias }}'
AND workspaceName = '{{ workspaceName }}';
```
