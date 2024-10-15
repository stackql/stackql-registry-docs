---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
  - orbital
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

Creates, updates, deletes, gets or lists a <code>contacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.orbital.contacts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_contacts', value: 'view', },
        { label: 'contacts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="antenna_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="contactName" /> | `text` | field from the `properties` object |
| <CopyableCode code="contact_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_azimuth_degrees" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_elevation_degrees" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="ground_station_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="maximum_elevation_degrees" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reservation_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="reservation_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rx_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="rx_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="spacecraftName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_azimuth_degrees" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_elevation_degrees" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tx_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="tx_start_time" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the Contact Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contactName, resourceGroupName, spacecraftName, subscriptionId" /> | Gets the specified contact in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, spacecraftName, subscriptionId" /> | Returns list of contacts by spacecraftName. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="contactName, resourceGroupName, spacecraftName, subscriptionId, data__properties" /> | Creates a contact. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="contactName, resourceGroupName, spacecraftName, subscriptionId" /> | Deletes a specified contact. |

## `SELECT` examples

Returns list of contacts by spacecraftName.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_contacts', value: 'view', },
        { label: 'contacts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
antenna_configuration,
contactName,
contact_profile,
end_azimuth_degrees,
end_elevation_degrees,
error_message,
ground_station_name,
maximum_elevation_degrees,
provisioning_state,
reservation_end_time,
reservation_start_time,
resourceGroupName,
rx_end_time,
rx_start_time,
spacecraftName,
start_azimuth_degrees,
start_elevation_degrees,
status,
subscriptionId,
tx_end_time,
tx_start_time
FROM azure.orbital.vw_contacts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND spacecraftName = '{{ spacecraftName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.orbital.contacts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND spacecraftName = '{{ spacecraftName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>contacts</code> resource.

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
INSERT INTO azure.orbital.contacts (
contactName,
resourceGroupName,
spacecraftName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ contactName }}',
'{{ resourceGroupName }}',
'{{ spacecraftName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: status
          value: string
        - name: reservationStartTime
          value: string
        - name: reservationEndTime
          value: string
        - name: rxStartTime
          value: string
        - name: rxEndTime
          value: string
        - name: txStartTime
          value: string
        - name: txEndTime
          value: string
        - name: errorMessage
          value: string
        - name: maximumElevationDegrees
          value: number
        - name: startAzimuthDegrees
          value: number
        - name: endAzimuthDegrees
          value: number
        - name: groundStationName
          value: string
        - name: startElevationDegrees
          value: number
        - name: endElevationDegrees
          value: number
        - name: antennaConfiguration
          value:
            - name: destinationIp
              value: string
            - name: sourceIps
              value:
                - string
        - name: contactProfile
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>contacts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.orbital.contacts
WHERE contactName = '{{ contactName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND spacecraftName = '{{ spacecraftName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
