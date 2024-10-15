---
title: racks
hide_title: false
hide_table_of_contents: false
keywords:
  - racks
  - nexus
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

Creates, updates, deletes, gets or lists a <code>racks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>racks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.racks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_racks', value: 'view', },
        { label: 'racks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availability_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="rackName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rack_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="rack_serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="rack_sku_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="rackName, resourceGroupName, subscriptionId" /> | Get properties of the provided rack. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of racks in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of racks in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="rackName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new rack or update properties of the existing one.
All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="rackName, resourceGroupName, subscriptionId" /> | Delete the provided rack.
All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="rackName, resourceGroupName, subscriptionId" /> | Patch properties of the provided rack, or update the tags associated with the rack. Properties and tag updates can be done independently. |

## `SELECT` examples

Get a list of racks in the provided subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_racks', value: 'view', },
        { label: 'racks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
availability_zone,
cluster_id,
detailed_status,
detailed_status_message,
extended_location,
location,
provisioning_state,
rackName,
rack_location,
rack_serial_number,
rack_sku_id,
resourceGroupName,
subscriptionId,
tags
FROM azure.nexus.vw_racks
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
FROM azure.nexus.racks
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>racks</code> resource.

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
INSERT INTO azure.nexus.racks (
rackName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
data__properties,
extendedLocation,
properties,
tags,
location
)
SELECT 
'{{ rackName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ data__properties }}',
'{{ extendedLocation }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: availabilityZone
          value: string
        - name: clusterId
          value: string
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: provisioningState
          value: string
        - name: rackLocation
          value: string
        - name: rackSerialNumber
          value: string
        - name: rackSkuId
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>racks</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.racks
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
rackName = '{{ rackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>racks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.racks
WHERE rackName = '{{ rackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
