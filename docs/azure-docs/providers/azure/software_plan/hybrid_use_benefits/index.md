---
title: hybrid_use_benefits
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_use_benefits
  - software_plan
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

Creates, updates, deletes, gets or lists a <code>hybrid_use_benefits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hybrid_use_benefits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.software_plan.hybrid_use_benefits" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hybrid_use_benefits', value: 'view', },
        { label: 'hybrid_use_benefits', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `integer` | Indicates the revision of the hybrid use benefit |
| <CopyableCode code="last_updated_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="planId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `integer` | Indicates the revision of the hybrid use benefit |
| <CopyableCode code="properties" /> | `object` | Hybrid use benefit properties |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="planId, scope" /> | Gets a given plan ID |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get all hybrid use benefits associated with an ARM resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="planId, scope, data__sku" /> | Create a new hybrid use benefit under a given scope |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="planId, scope" /> | Deletes a given plan ID |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="planId, scope, data__sku" /> | Updates an existing hybrid use benefit |

## `SELECT` examples

Get all hybrid use benefits associated with an ARM resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hybrid_use_benefits', value: 'view', },
        { label: 'hybrid_use_benefits', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
created_date,
etag,
last_updated_date,
planId,
provisioning_state,
scope,
sku,
type
FROM azure.software_plan.vw_hybrid_use_benefits
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
sku,
type
FROM azure.software_plan.hybrid_use_benefits
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hybrid_use_benefits</code> resource.

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
INSERT INTO azure.software_plan.hybrid_use_benefits (
planId,
scope,
data__sku,
sku,
properties
)
SELECT 
'{{ planId }}',
'{{ scope }}',
'{{ data__sku }}',
'{{ sku }}',
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
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: etag
      value: integer
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: createdDate
          value: string
        - name: lastUpdatedDate
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>hybrid_use_benefits</code> resource.

```sql
/*+ update */
UPDATE azure.software_plan.hybrid_use_benefits
SET 
sku = '{{ sku }}',
properties = '{{ properties }}'
WHERE 
planId = '{{ planId }}'
AND scope = '{{ scope }}'
AND data__sku = '{{ data__sku }}';
```

## `DELETE` example

Deletes the specified <code>hybrid_use_benefits</code> resource.

```sql
/*+ delete */
DELETE FROM azure.software_plan.hybrid_use_benefits
WHERE planId = '{{ planId }}'
AND scope = '{{ scope }}';
```
