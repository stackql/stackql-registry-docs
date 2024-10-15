---
title: skus_nested_resource_type_seconds
hide_title: false
hide_table_of_contents: false
keywords:
  - skus_nested_resource_type_seconds
  - provider_hub
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

Creates, updates, deletes, gets or lists a <code>skus_nested_resource_type_seconds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skus_nested_resource_type_seconds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.skus_nested_resource_type_seconds" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, sku, subscriptionId" /> | Gets the sku details for the given resource type and sku name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, sku, subscriptionId" /> | Creates or updates the resource type skus in the given resource type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, sku, subscriptionId" /> | Deletes a resource type sku. |

## `SELECT` examples

Gets the sku details for the given resource type and sku name.


```sql
SELECT
properties
FROM azure.provider_hub.skus_nested_resource_type_seconds
WHERE nestedResourceTypeFirst = '{{ nestedResourceTypeFirst }}'
AND nestedResourceTypeSecond = '{{ nestedResourceTypeSecond }}'
AND providerNamespace = '{{ providerNamespace }}'
AND resourceType = '{{ resourceType }}'
AND sku = '{{ sku }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>skus_nested_resource_type_seconds</code> resource.

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
INSERT INTO azure.provider_hub.skus_nested_resource_type_seconds (
nestedResourceTypeFirst,
nestedResourceTypeSecond,
providerNamespace,
resourceType,
sku,
subscriptionId,
properties
)
SELECT 
'{{ nestedResourceTypeFirst }}',
'{{ nestedResourceTypeSecond }}',
'{{ providerNamespace }}',
'{{ resourceType }}',
'{{ sku }}',
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
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>skus_nested_resource_type_seconds</code> resource.

```sql
/*+ delete */
DELETE FROM azure.provider_hub.skus_nested_resource_type_seconds
WHERE nestedResourceTypeFirst = '{{ nestedResourceTypeFirst }}'
AND nestedResourceTypeSecond = '{{ nestedResourceTypeSecond }}'
AND providerNamespace = '{{ providerNamespace }}'
AND resourceType = '{{ resourceType }}'
AND sku = '{{ sku }}'
AND subscriptionId = '{{ subscriptionId }}';
```
