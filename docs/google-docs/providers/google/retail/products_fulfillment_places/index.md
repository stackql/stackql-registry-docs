
---
title: products_fulfillment_places
hide_title: false
hide_table_of_contents: false
keywords:
  - products_fulfillment_places
  - retail
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

Creates, updates, deletes or gets an <code>products_fulfillment_place</code> resource or lists <code>products_fulfillment_places</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products_fulfillment_places</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.products_fulfillment_places" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_branches_products_add_fulfillment_places" /> | `INSERT` | <CopyableCode code="branchesId, catalogsId, locationsId, productsId, projectsId" /> | We recommend that you use the ProductService.AddLocalInventories method instead of the ProductService.AddFulfillmentPlaces method. ProductService.AddLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data. Incrementally adds place IDs to Product.fulfillment_info.place_ids. This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the added place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts. The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards. If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete. |
| <CopyableCode code="projects_locations_catalogs_branches_products_remove_fulfillment_places" /> | `DELETE` | <CopyableCode code="branchesId, catalogsId, locationsId, productsId, projectsId" /> | We recommend that you use the ProductService.RemoveLocalInventories method instead of the ProductService.RemoveFulfillmentPlaces method. ProductService.RemoveLocalInventories achieves the same results but provides more fine-grained control over ingesting local inventory data. Incrementally removes place IDs from a Product.fulfillment_info.place_ids. This process is asynchronous and does not require the Product to exist before updating fulfillment information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, the removed place IDs are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts. The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards. If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>products_fulfillment_places</code> resource.

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
INSERT INTO google.retail.products_fulfillment_places (
branchesId,
catalogsId,
locationsId,
productsId,
projectsId,
type,
placeIds,
addTime,
allowMissing
)
SELECT 
'{{ branchesId }}',
'{{ catalogsId }}',
'{{ locationsId }}',
'{{ productsId }}',
'{{ projectsId }}',
'{{ type }}',
'{{ placeIds }}',
'{{ addTime }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: type
        value: '{{ type }}'
      - name: placeIds
        value: '{{ placeIds }}'
      - name: addTime
        value: '{{ addTime }}'
      - name: allowMissing
        value: '{{ allowMissing }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified products_fulfillment_place resource.

```sql
DELETE FROM google.retail.products_fulfillment_places
WHERE branchesId = '{{ branchesId }}'
AND catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND productsId = '{{ productsId }}'
AND projectsId = '{{ projectsId }}';
```
