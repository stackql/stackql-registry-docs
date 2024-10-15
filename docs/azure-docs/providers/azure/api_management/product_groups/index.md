---
title: product_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - product_groups
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

Creates, updates, deletes, gets or lists a <code>product_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.product_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Group contract Properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Lists the collection of developer groups associated with the specified product. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupId, productId, resourceGroupName, serviceName, subscriptionId" /> | Adds the association between the specified developer group with the specified product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupId, productId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the association between the specified group and product. |

## `SELECT` examples

Lists the collection of developer groups associated with the specified product.


```sql
SELECT
properties
FROM azure.api_management.product_groups
WHERE productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>product_groups</code> resource.

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
INSERT INTO azure.api_management.product_groups (
groupId,
productId,
resourceGroupName,
serviceName,
subscriptionId
)
SELECT 
'{{ groupId }}',
'{{ productId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>product_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.product_groups
WHERE groupId = '{{ groupId }}'
AND productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
