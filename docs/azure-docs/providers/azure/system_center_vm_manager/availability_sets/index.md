---
title: availability_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_sets
  - system_center_vm_manager
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

Creates, updates, deletes, gets or lists a <code>availability_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>availability_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.availability_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_availability_sets', value: 'view', },
        { label: 'availability_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availabilitySetResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_set_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="vmm_server_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="availabilitySetResourceName, resourceGroupName, subscriptionId" /> | Implements AvailabilitySet GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List of AvailabilitySets in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List of AvailabilitySets in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="availabilitySetResourceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Onboards the ScVmm availability set as an Azure resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="availabilitySetResourceName, resourceGroupName, subscriptionId" /> | Deregisters the ScVmm availability set from Azure. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="availabilitySetResourceName, resourceGroupName, subscriptionId" /> | Updates the AvailabilitySets resource. |

## `SELECT` examples

List of AvailabilitySets in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_availability_sets', value: 'view', },
        { label: 'availability_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
availabilitySetResourceName,
availability_set_name,
extended_location,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
vmm_server_id
FROM azure.system_center_vm_manager.vw_availability_sets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.system_center_vm_manager.availability_sets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>availability_sets</code> resource.

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
INSERT INTO azure.system_center_vm_manager.availability_sets (
availabilitySetResourceName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ availabilitySetResourceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: availabilitySetName
          value: string
        - name: vmmServerId
          value: string
        - name: provisioningState
          value: []
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>availability_sets</code> resource.

```sql
/*+ update */
UPDATE azure.system_center_vm_manager.availability_sets
SET 
tags = '{{ tags }}'
WHERE 
availabilitySetResourceName = '{{ availabilitySetResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>availability_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.system_center_vm_manager.availability_sets
WHERE availabilitySetResourceName = '{{ availabilitySetResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
