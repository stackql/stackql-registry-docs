---
title: resource_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_pools
  - connected_vsphere
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

Creates, updates, deletes, gets or lists a <code>resource_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.connected_vsphere.resource_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_pools', value: 'view', },
        { label: 'resource_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the Id. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name. |
| <CopyableCode code="cpu_capacity_m_hz" /> | `text` | field from the `properties` object |
| <CopyableCode code="cpu_limit_m_hz" /> | `text` | field from the `properties` object |
| <CopyableCode code="cpu_overall_usage_m_hz" /> | `text` | field from the `properties` object |
| <CopyableCode code="cpu_reservation_m_hz" /> | `text` | field from the `properties` object |
| <CopyableCode code="cpu_shares_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_resource_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="datastore_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="inventory_item_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="location" /> | `text` | Gets or sets the location. |
| <CopyableCode code="mem_capacity_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="mem_limit_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="mem_overall_usage_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="mem_reservation_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="mem_shares_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="mo_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="mo_ref_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourcePoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="statuses" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets the Resource tags. |
| <CopyableCode code="type" /> | `text` | Gets or sets the type of the resource. |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_center_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name. |
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="location" /> | `string` | Gets or sets the location. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Resource Pool. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Gets or sets the Resource tags. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourcePoolName, subscriptionId" /> | Implements resourcePool GET method. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List of resourcePools in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List of resourcePools in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourcePoolName, subscriptionId, data__location, data__properties" /> | Create Or Update resourcePool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourcePoolName, subscriptionId" /> | Implements resourcePool DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourcePoolName, subscriptionId" /> | API to update certain properties of the resourcePool resource. |

## `SELECT` examples

List of resourcePools in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_pools', value: 'view', },
        { label: 'resource_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cpu_capacity_m_hz,
cpu_limit_m_hz,
cpu_overall_usage_m_hz,
cpu_reservation_m_hz,
cpu_shares_level,
custom_resource_name,
datastore_ids,
extended_location,
inventory_item_id,
kind,
location,
mem_capacity_gb,
mem_limit_mb,
mem_overall_usage_gb,
mem_reservation_mb,
mem_shares_level,
mo_name,
mo_ref_id,
network_ids,
provisioning_state,
resourceGroupName,
resourcePoolName,
statuses,
subscriptionId,
system_data,
tags,
type,
uuid,
v_center_id
FROM azure_isv.connected_vsphere.vw_resource_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
extendedLocation,
kind,
location,
properties,
systemData,
tags,
type
FROM azure_isv.connected_vsphere.resource_pools
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_pools</code> resource.

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
INSERT INTO azure_isv.connected_vsphere.resource_pools (
resourceGroupName,
resourcePoolName,
subscriptionId,
data__location,
data__properties,
properties,
location,
extendedLocation,
systemData,
tags,
kind
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourcePoolName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}',
'{{ extendedLocation }}',
'{{ systemData }}',
'{{ tags }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: uuid
          value: string
        - name: vCenterId
          value: string
        - name: moRefId
          value: string
        - name: inventoryItemId
          value: string
        - name: moName
          value: string
        - name: cpuSharesLevel
          value: string
        - name: cpuReservationMHz
          value: integer
        - name: cpuLimitMHz
          value: integer
        - name: memSharesLevel
          value: string
        - name: memReservationMB
          value: integer
        - name: memLimitMB
          value: integer
        - name: memOverallUsageGB
          value: integer
        - name: memCapacityGB
          value: integer
        - name: cpuOverallUsageMHz
          value: integer
        - name: cpuCapacityMHz
          value: integer
        - name: customResourceName
          value: string
        - name: datastoreIds
          value:
            - string
        - name: networkIds
          value:
            - string
        - name: statuses
          value:
            - - name: type
                value: string
              - name: status
                value: string
              - name: reason
                value: string
              - name: message
                value: string
              - name: severity
                value: string
              - name: lastUpdatedAt
                value: string
        - name: provisioningState
          value: []
    - name: location
      value: string
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
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
    - name: tags
      value: object
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>resource_pools</code> resource.

```sql
/*+ update */
UPDATE azure_isv.connected_vsphere.resource_pools
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourcePoolName = '{{ resourcePoolName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>resource_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.connected_vsphere.resource_pools
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourcePoolName = '{{ resourcePoolName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
