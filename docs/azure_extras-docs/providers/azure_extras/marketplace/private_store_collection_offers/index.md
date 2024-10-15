---
title: private_store_collection_offers
hide_title: false
hide_table_of_contents: false
keywords:
  - private_store_collection_offers
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

Creates, updates, deletes, gets or lists a <code>private_store_collection_offers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_store_collection_offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.private_store_collection_offers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_store_collection_offers', value: 'view', },
        { label: 'private_store_collection_offers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="collectionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_file_uris" /> | `text` | field from the `properties` object |
| <CopyableCode code="modified_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="offerId" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="plans" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateStoreId" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_store_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="specific_plan_ids_limitation" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="unique_offer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="update_suppressed_due_idempotence" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="collectionId, offerId, privateStoreId" /> | Gets information about a specific offer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="collectionId, privateStoreId" /> | Get a list of all private offers in the given private store and collection |
| <CopyableCode code="list_by_contexts" /> | `SELECT` | <CopyableCode code="collectionId, privateStoreId" /> | Get a list of all offers in the given collection according to the required contexts. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="collectionId, offerId, privateStoreId" /> | Update or add an offer to a specific collection of the private store. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="collectionId, offerId, privateStoreId" /> | Deletes an offer from the given collection of private store. |
| <CopyableCode code="post" /> | `EXEC` | <CopyableCode code="collectionId, offerId, privateStoreId" /> | Delete Private store offer. This is a workaround. |
| <CopyableCode code="upsert_offer_with_multi_context" /> | `EXEC` | <CopyableCode code="collectionId, offerId, privateStoreId" /> | Upsert an offer with multiple context details. |

## `SELECT` examples

Get a list of all private offers in the given private store and collection

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_store_collection_offers', value: 'view', },
        { label: 'private_store_collection_offers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
collectionId,
created_at,
e_tag,
icon_file_uris,
modified_at,
offerId,
offer_display_name,
plans,
privateStoreId,
private_store_id,
publisher_display_name,
specific_plan_ids_limitation,
system_data,
type,
unique_offer_id,
update_suppressed_due_idempotence
FROM azure_extras.marketplace.vw_private_store_collection_offers
WHERE collectionId = '{{ collectionId }}'
AND privateStoreId = '{{ privateStoreId }}';
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
FROM azure_extras.marketplace.private_store_collection_offers
WHERE collectionId = '{{ collectionId }}'
AND privateStoreId = '{{ privateStoreId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_store_collection_offers</code> resource.

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
INSERT INTO azure_extras.marketplace.private_store_collection_offers (
collectionId,
offerId,
privateStoreId,
properties
)
SELECT 
'{{ collectionId }}',
'{{ offerId }}',
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
        - name: uniqueOfferId
          value: string
        - name: offerDisplayName
          value: string
        - name: publisherDisplayName
          value: string
        - name: eTag
          value: string
        - name: privateStoreId
          value: string
        - name: createdAt
          value: string
        - name: modifiedAt
          value: string
        - name: specificPlanIdsLimitation
          value:
            - string
        - name: updateSuppressedDueIdempotence
          value: boolean
        - name: iconFileUris
          value: object
        - name: plans
          value:
            - - name: skuId
                value: string
              - name: planId
                value: string
              - name: planDisplayName
                value: string
              - name: accessibility
                value: string
              - name: altStackReference
                value: string
              - name: stackType
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>private_store_collection_offers</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.marketplace.private_store_collection_offers
WHERE collectionId = '{{ collectionId }}'
AND offerId = '{{ offerId }}'
AND privateStoreId = '{{ privateStoreId }}';
```
