---
title: product_apis
hide_title: false
hide_table_of_contents: false
keywords:
  - product_apis
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

Creates, updates, deletes, gets or lists a <code>product_apis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.product_apis" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | API Entity Properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="productId, resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of the APIs associated with a product. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, productId, resourceGroupName, serviceName, subscriptionId" /> | Adds an API to the specified product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiId, productId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified API from the specified product. |

## `SELECT` examples

Lists a collection of the APIs associated with a product.


```sql
SELECT
properties
FROM azure.api_management.product_apis
WHERE productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>product_apis</code> resource.

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
INSERT INTO azure.api_management.product_apis (
apiId,
productId,
resourceGroupName,
serviceName,
subscriptionId
)
SELECT 
'{{ apiId }}',
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

Deletes the specified <code>product_apis</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.product_apis
WHERE apiId = '{{ apiId }}'
AND productId = '{{ productId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
