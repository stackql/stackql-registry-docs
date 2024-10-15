---
title: private_store_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_store_collections
  - marketplace
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

Creates, updates, deletes, gets or lists a <code>private_store_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_store_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.private_store_collections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_store_collections', value: 'view', },
        { label: 'private_store_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="all_subscriptions" /> | `text` | field from the `properties` object |
| <CopyableCode code="applied_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="approve_all_items" /> | `text` | field from the `properties` object |
| <CopyableCode code="approve_all_items_modified_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="claim" /> | `text` | field from the `properties` object |
| <CopyableCode code="collectionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="collection_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="collection_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_offers" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateStoreId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptions_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The collection details |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="collectionId, privateStoreId" /> | Gets private store collection |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateStoreId" /> | Gets private store collections list |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="collectionId, privateStoreId" /> | Create or update private store collection |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="collectionId, privateStoreId" /> | Delete a collection from the given private store. |
| <CopyableCode code="approve_all_items" /> | `EXEC` | <CopyableCode code="collectionId, privateStoreId" /> | Delete all existing offers from the collection and enable approve all items. |
| <CopyableCode code="disable_approve_all_items" /> | `EXEC` | <CopyableCode code="collectionId, privateStoreId" /> | Disable approve all items for the collection. |
| <CopyableCode code="post" /> | `EXEC` | <CopyableCode code="collectionId, privateStoreId" /> | Delete Private store collection. This is a workaround. |
| <CopyableCode code="transfer_offers" /> | `EXEC` | <CopyableCode code="collectionId, privateStoreId" /> | transferring offers (copy or move) from source collection to target collection(s) |

## `SELECT` examples

Gets private store collections list

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_store_collections', value: 'view', },
        { label: 'private_store_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
all_subscriptions,
applied_rules,
approve_all_items,
approve_all_items_modified_at,
claim,
collectionId,
collection_id,
collection_name,
enabled,
number_of_offers,
privateStoreId,
subscriptions_list,
system_data,
type
FROM azure_extras.marketplace.vw_private_store_collections
WHERE privateStoreId = '{{ privateStoreId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure_extras.marketplace.private_store_collections
WHERE privateStoreId = '{{ privateStoreId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_store_collections</code> resource.

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
INSERT INTO azure_extras.marketplace.private_store_collections (
collectionId,
privateStoreId,
properties
)
SELECT 
'{{ collectionId }}',
'{{ privateStoreId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: []
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: collectionId
          value: string
        - name: collectionName
          value: string
        - name: claim
          value: string
        - name: allSubscriptions
          value: boolean
        - name: approveAllItems
          value: boolean
        - name: approveAllItemsModifiedAt
          value: string
        - name: subscriptionsList
          value:
            - string
        - name: enabled
          value: boolean
        - name: numberOfOffers
          value: integer
        - name: appliedRules
          value:
            - - name: type
                value: string
              - name: value
                value:
                  - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>private_store_collections</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.marketplace.private_store_collections
WHERE collectionId = '{{ collectionId }}'
AND privateStoreId = '{{ privateStoreId }}';
```
