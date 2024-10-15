---
title: reservation_order_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_order_aliases
  - billing_benefits
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

Creates, updates, deletes, gets or lists a <code>reservation_order_aliases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reservation_order_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing_benefits.reservation_order_aliases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reservation_order_aliases', value: 'view', },
        { label: 'reservation_order_aliases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="applied_scope_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="applied_scope_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_scope_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The Azure Region where the reserved resource lives. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="quantity" /> | `text` | field from the `properties` object |
| <CopyableCode code="renew" /> | `text` | field from the `properties` object |
| <CopyableCode code="reservationOrderAliasName" /> | `text` | field from the `properties` object |
| <CopyableCode code="reservation_order_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="reserved_resource_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="reserved_resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="review_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="term" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The Azure Region where the reserved resource lives. |
| <CopyableCode code="properties" /> | `object` | Reservation properties |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reservationOrderAliasName" /> | Get a reservation order alias. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="reservationOrderAliasName, data__sku" /> | Create a reservation order alias. |

## `SELECT` examples

Get a reservation order alias.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_reservation_order_aliases', value: 'view', },
        { label: 'reservation_order_aliases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
applied_scope_properties,
applied_scope_type,
billing_plan,
billing_scope_id,
display_name,
location,
provisioning_state,
quantity,
renew,
reservationOrderAliasName,
reservation_order_id,
reserved_resource_properties,
reserved_resource_type,
review_date_time,
sku,
system_data,
term,
type
FROM azure.billing_benefits.vw_reservation_order_aliases
WHERE reservationOrderAliasName = '{{ reservationOrderAliasName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
sku,
systemData,
type
FROM azure.billing_benefits.reservation_order_aliases
WHERE reservationOrderAliasName = '{{ reservationOrderAliasName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>reservation_order_aliases</code> resource.

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
INSERT INTO azure.billing_benefits.reservation_order_aliases (
reservationOrderAliasName,
data__sku,
sku,
location,
properties
)
SELECT 
'{{ reservationOrderAliasName }}',
'{{ data__sku }}',
'{{ sku }}',
'{{ location }}',
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
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: []
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: location
      value: string
    - name: properties
      value:
        - name: displayName
          value: []
        - name: billingScopeId
          value: []
        - name: term
          value: []
        - name: billingPlan
          value: []
        - name: appliedScopeType
          value: []
        - name: appliedScopeProperties
          value:
            - name: tenantId
              value: []
            - name: managementGroupId
              value: []
            - name: subscriptionId
              value: []
            - name: resourceGroupId
              value: []
            - name: displayName
              value: string
        - name: quantity
          value: integer
        - name: renew
          value: []
        - name: reservedResourceType
          value: []
        - name: reviewDateTime
          value: string
        - name: reservedResourceProperties
          value:
            - name: instanceFlexibility
              value: []

```
</TabItem>
</Tabs>
