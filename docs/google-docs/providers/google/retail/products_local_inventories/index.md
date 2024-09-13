---
title: products_local_inventories
hide_title: false
hide_table_of_contents: false
keywords:
  - products_local_inventories
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

Creates, updates, deletes, gets or lists a <code>products_local_inventories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>products_local_inventories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.products_local_inventories" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_branches_products_add_local_inventories" /> | `INSERT` | <CopyableCode code="branchesId, catalogsId, locationsId, productsId, projectsId" /> | Updates local inventory information for a Product at a list of places, while respecting the last update timestamps of each inventory field. This process is asynchronous and does not require the Product to exist before updating inventory information. If the request is valid, the update will be enqueued and processed downstream. As a consequence, when a response is returned, updates are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts. Local inventory information can only be modified using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories. The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards. If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete. |
| <CopyableCode code="projects_locations_catalogs_branches_products_remove_local_inventories" /> | `DELETE` | <CopyableCode code="branchesId, catalogsId, locationsId, productsId, projectsId" /> | Remove local inventory information for a Product at a list of places at a removal timestamp. This process is asynchronous. If the request is valid, the removal will be enqueued and processed downstream. As a consequence, when a response is returned, removals are not immediately manifested in the Product queried by ProductService.GetProduct or ProductService.ListProducts. Local inventory information can only be removed using this method. ProductService.CreateProduct and ProductService.UpdateProduct has no effect on local inventories. The returned Operations will be obsolete after 1 day, and GetOperation API will return NOT_FOUND afterwards. If conflicting updates are issued, the Operations associated with the stale updates will not be marked as done until being obsolete. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>products_local_inventories</code> resource.

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
INSERT INTO google.retail.products_local_inventories (
branchesId,
catalogsId,
locationsId,
productsId,
projectsId,
localInventories,
addMask,
addTime,
allowMissing
)
SELECT 
'{{ branchesId }}',
'{{ catalogsId }}',
'{{ locationsId }}',
'{{ productsId }}',
'{{ projectsId }}',
'{{ localInventories }}',
'{{ addMask }}',
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
      - name: localInventories
        value: '{{ localInventories }}'
      - name: addMask
        value: '{{ addMask }}'
      - name: addTime
        value: '{{ addTime }}'
      - name: allowMissing
        value: '{{ allowMissing }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>products_local_inventories</code> resource.

```sql
/*+ delete */
DELETE FROM google.retail.products_local_inventories
WHERE branchesId = '{{ branchesId }}'
AND catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND productsId = '{{ productsId }}'
AND projectsId = '{{ projectsId }}';
```
