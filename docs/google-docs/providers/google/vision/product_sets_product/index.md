---
title: product_sets_product
hide_title: false
hide_table_of_contents: false
keywords:
  - product_sets_product
  - vision
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

Creates, updates, deletes, gets or lists a <code>product_sets_product</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_sets_product</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vision.product_sets_product" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_product_sets_add_product" /> | `INSERT` | <CopyableCode code="locationsId, productSetsId, projectsId" /> | Adds a Product to the specified ProductSet. If the Product is already present, no change is made. One Product can be added to at most 100 ProductSets. Possible errors: * Returns NOT_FOUND if the Product or the ProductSet doesn't exist. |
| <CopyableCode code="projects_locations_product_sets_remove_product" /> | `DELETE` | <CopyableCode code="locationsId, productSetsId, projectsId" /> | Removes a Product from the specified ProductSet. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>product_sets_product</code> resource.

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
INSERT INTO google.vision.product_sets_product (
locationsId,
productSetsId,
projectsId,
product
)
SELECT 
'{{ locationsId }}',
'{{ productSetsId }}',
'{{ projectsId }}',
'{{ product }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: product
      value: '{{ product }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>product_sets_product</code> resource.

```sql
/*+ delete */
DELETE FROM google.vision.product_sets_product
WHERE locationsId = '{{ locationsId }}'
AND productSetsId = '{{ productSetsId }}'
AND projectsId = '{{ projectsId }}';
```
