---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
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

Creates, updates, deletes, gets or lists a <code>virtual_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.connected_vsphere.virtual_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_networks', value: 'view', },
        { label: 'virtual_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the Id. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name. |
| <CopyableCode code="custom_resource_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="inventory_item_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="location" /> | `text` | Gets or sets the location. |
| <CopyableCode code="mo_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="mo_ref_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="statuses" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets the Resource tags. |
| <CopyableCode code="type" /> | `text` | Gets or sets the type of the resource. |
| <CopyableCode code="uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_center_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualNetworkName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name. |
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="location" /> | `string` | Gets or sets the location. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Network. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Gets or sets the Resource tags. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Implements virtual network GET method. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List of virtualNetworks in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List of virtualNetworks in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName, data__location, data__properties" /> | Create Or Update virtual network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Implements virtual network DELETE method. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | API to update certain properties of the virtual network resource. |

## `SELECT` examples

List of virtualNetworks in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_networks', value: 'view', },
        { label: 'virtual_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
custom_resource_name,
extended_location,
inventory_item_id,
kind,
location,
mo_name,
mo_ref_id,
provisioning_state,
resourceGroupName,
statuses,
subscriptionId,
system_data,
tags,
type,
uuid,
v_center_id,
virtualNetworkName
FROM azure_isv.connected_vsphere.vw_virtual_networks
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
FROM azure_isv.connected_vsphere.virtual_networks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_networks</code> resource.

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
INSERT INTO azure_isv.connected_vsphere.virtual_networks (
resourceGroupName,
subscriptionId,
virtualNetworkName,
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
'{{ subscriptionId }}',
'{{ virtualNetworkName }}',
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
        - name: customResourceName
          value: string
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

Updates a <code>virtual_networks</code> resource.

```sql
/*+ update */
UPDATE azure_isv.connected_vsphere.virtual_networks
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.connected_vsphere.virtual_networks
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}';
```
