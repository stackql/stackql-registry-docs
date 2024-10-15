---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.devices" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_devices', value: 'view', },
        { label: 'devices', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The object name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="configured_role_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="culture" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_box_edge_device_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_residency" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_hcs_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_local_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_software_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="edge_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag for the devices. |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Msi identity details of the resource |
| <CopyableCode code="kind" /> | `text` | The kind of the device. |
| <CopyableCode code="kubernetes_workload_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the device. This is a supported and registered Azure geographical region (for example, West US, East US, or Southeast Asia). The geographical region of a device cannot be changed once it is created, but if an identical geographical region is specified on update, the request will succeed. |
| <CopyableCode code="model_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_move_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The list of tags that describe the device. These tags can be used to view and group this device (across resource groups). |
| <CopyableCode code="time_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="etag" /> | `string` | The etag for the devices. |
| <CopyableCode code="identity" /> | `object` | Msi identity details of the resource |
| <CopyableCode code="kind" /> | `string` | The kind of the device. |
| <CopyableCode code="location" /> | `string` | The location of the device. This is a supported and registered Azure geographical region (for example, West US, East US, or Southeast Asia). The geographical region of a device cannot be changed once it is created, but if an identical geographical region is specified on update, the request will succeed. |
| <CopyableCode code="properties" /> | `object` | The properties of the Data Box Edge/Gateway device. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The list of tags that describe the device. These tags can be used to view and group this device (across resource groups). |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Gets the properties of the Data Box Edge/Data Box Gateway device. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the Data Box Edge/Data Box Gateway devices in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the Data Box Edge/Data Box Gateway devices in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates a Data Box Edge/Data Box Gateway resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Deletes the Data Box Edge/Data Box Gateway device. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Modifies a Data Box Edge/Data Box Gateway resource. |
| <CopyableCode code="download_updates" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="generate_certificate" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> | Generates certificate for activation key. |
| <CopyableCode code="install_updates" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="scan_for_updates" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="upload_certificate" /> | `EXEC` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId, data__properties" /> | Uploads registration certificate for the device. |

## `SELECT` examples

Gets all the Data Box Edge/Data Box Gateway devices in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_devices', value: 'view', },
        { label: 'devices', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
configured_role_types,
culture,
data_box_edge_device_status,
data_residency,
deviceName,
device_hcs_version,
device_local_capacity,
device_model,
device_software_version,
device_type,
edge_profile,
etag,
friendly_name,
identity,
kind,
kubernetes_workload_profile,
location,
model_description,
node_count,
resourceGroupName,
resource_move_details,
serial_number,
sku,
subscriptionId,
system_data,
tags,
time_zone,
type
FROM azure.data_box_edge.vw_devices
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
kind,
location,
properties,
sku,
systemData,
tags,
type
FROM azure.data_box_edge.devices
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>devices</code> resource.

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
INSERT INTO azure.data_box_edge.devices (
deviceName,
resourceGroupName,
subscriptionId,
data__location,
location,
tags,
sku,
etag,
identity,
properties
)
SELECT 
'{{ deviceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ etag }}',
'{{ identity }}',
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
    - name: location
      value: string
    - name: tags
      value: object
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
      value: string
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
    - name: kind
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
    - name: properties
      value:
        - name: dataBoxEdgeDeviceStatus
          value: string
        - name: serialNumber
          value: string
        - name: description
          value: string
        - name: modelDescription
          value: string
        - name: deviceType
          value: string
        - name: friendlyName
          value: string
        - name: culture
          value: string
        - name: deviceModel
          value: string
        - name: deviceSoftwareVersion
          value: string
        - name: deviceLocalCapacity
          value: integer
        - name: timeZone
          value: string
        - name: deviceHcsVersion
          value: string
        - name: configuredRoleTypes
          value:
            - string
        - name: nodeCount
          value: integer
        - name: resourceMoveDetails
          value:
            - name: operationInProgress
              value: string
            - name: operationInProgressLockTimeoutInUTC
              value: string
        - name: edgeProfile
          value:
            - name: subscription
              value:
                - name: registrationId
                  value: string
                - name: id
                  value: string
                - name: state
                  value: string
                - name: registrationDate
                  value: string
                - name: subscriptionId
                  value: string
                - name: properties
                  value:
                    - name: tenantId
                      value: string
                    - name: locationPlacementId
                      value: string
                    - name: quotaId
                      value: string
                    - name: serializedDetails
                      value: string
                    - name: registeredFeatures
                      value:
                        - - name: name
                            value: string
                          - name: state
                            value: string
        - name: dataResidency
          value:
            - name: type
              value: string
        - name: kubernetesWorkloadProfile
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>devices</code> resource.

```sql
/*+ update */
UPDATE azure.data_box_edge.devices
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>devices</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_box_edge.devices
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
