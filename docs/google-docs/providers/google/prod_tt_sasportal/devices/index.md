---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - prod_tt_sasportal
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.prod_tt_sasportal.devices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource path name. |
| <CopyableCode code="activeConfig" /> | `object` | Information about the device configuration. |
| <CopyableCode code="currentChannels" /> | `array` | Output only. Current channels with scores. |
| <CopyableCode code="deviceMetadata" /> | `object` | Device data overridable by both SAS Portal and registration requests. |
| <CopyableCode code="displayName" /> | `string` | Device display name. |
| <CopyableCode code="fccId" /> | `string` | The FCC identifier of the device. Refer to https://www.fcc.gov/oet/ea/fccid for FccID format. Accept underscores and periods because some test-SAS customers use them. |
| <CopyableCode code="grantRangeAllowlists" /> | `array` | Only ranges that are within the allowlists are available for new grants. |
| <CopyableCode code="grants" /> | `array` | Output only. Grants held by the device. |
| <CopyableCode code="preloadedConfig" /> | `object` | Information about the device configuration. |
| <CopyableCode code="serialNumber" /> | `string` | A serial number assigned to the device by the device manufacturer. |
| <CopyableCode code="state" /> | `string` | Output only. Device state. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="customers_deployments_devices_list" /> | `SELECT` | <CopyableCode code="customersId, deploymentsId" /> | Lists devices under a node or customer. |
| <CopyableCode code="customers_devices_get" /> | `SELECT` | <CopyableCode code="customersId, devicesId" /> | Gets details about a device. |
| <CopyableCode code="customers_devices_list" /> | `SELECT` | <CopyableCode code="customersId" /> | Lists devices under a node or customer. |
| <CopyableCode code="customers_nodes_devices_list" /> | `SELECT` | <CopyableCode code="customersId, nodesId" /> | Lists devices under a node or customer. |
| <CopyableCode code="deployments_devices_get" /> | `SELECT` | <CopyableCode code="deploymentsId, devicesId" /> | Gets details about a device. |
| <CopyableCode code="nodes_deployments_devices_list" /> | `SELECT` | <CopyableCode code="deploymentsId, nodesId" /> | Lists devices under a node or customer. |
| <CopyableCode code="nodes_devices_get" /> | `SELECT` | <CopyableCode code="devicesId, nodesId" /> | Gets details about a device. |
| <CopyableCode code="nodes_devices_list" /> | `SELECT` | <CopyableCode code="nodesId" /> | Lists devices under a node or customer. |
| <CopyableCode code="nodes_nodes_devices_list" /> | `SELECT` | <CopyableCode code="nodesId, nodesId1" /> | Lists devices under a node or customer. |
| <CopyableCode code="customers_deployments_devices_create" /> | `INSERT` | <CopyableCode code="customersId, deploymentsId" /> | Creates a device under a node or customer. |
| <CopyableCode code="customers_devices_create" /> | `INSERT` | <CopyableCode code="customersId" /> | Creates a device under a node or customer. |
| <CopyableCode code="customers_nodes_devices_create" /> | `INSERT` | <CopyableCode code="customersId, nodesId" /> | Creates a device under a node or customer. |
| <CopyableCode code="nodes_deployments_devices_create" /> | `INSERT` | <CopyableCode code="deploymentsId, nodesId" /> | Creates a device under a node or customer. |
| <CopyableCode code="nodes_devices_create" /> | `INSERT` | <CopyableCode code="nodesId" /> | Creates a device under a node or customer. |
| <CopyableCode code="nodes_nodes_devices_create" /> | `INSERT` | <CopyableCode code="nodesId, nodesId1" /> | Creates a device under a node or customer. |
| <CopyableCode code="customers_devices_delete" /> | `DELETE` | <CopyableCode code="customersId, devicesId" /> | Deletes a device. |
| <CopyableCode code="deployments_devices_delete" /> | `DELETE` | <CopyableCode code="deploymentsId, devicesId" /> | Deletes a device. |
| <CopyableCode code="nodes_devices_delete" /> | `DELETE` | <CopyableCode code="devicesId, nodesId" /> | Deletes a device. |
| <CopyableCode code="customers_devices_patch" /> | `UPDATE` | <CopyableCode code="customersId, devicesId" /> | Updates a device. |
| <CopyableCode code="deployments_devices_patch" /> | `UPDATE` | <CopyableCode code="deploymentsId, devicesId" /> | Updates a device. |
| <CopyableCode code="nodes_devices_patch" /> | `UPDATE` | <CopyableCode code="devicesId, nodesId" /> | Updates a device. |
| <CopyableCode code="customers_devices_move" /> | `EXEC` | <CopyableCode code="customersId, devicesId" /> | Moves a device under another node or customer. |
| <CopyableCode code="customers_devices_sign_device" /> | `EXEC` | <CopyableCode code="customersId, devicesId" /> | Signs a device. |
| <CopyableCode code="deployments_devices_move" /> | `EXEC` | <CopyableCode code="deploymentsId, devicesId" /> | Moves a device under another node or customer. |
| <CopyableCode code="deployments_devices_sign_device" /> | `EXEC` | <CopyableCode code="deploymentsId, devicesId" /> | Signs a device. |
| <CopyableCode code="nodes_devices_move" /> | `EXEC` | <CopyableCode code="devicesId, nodesId" /> | Moves a device under another node or customer. |
| <CopyableCode code="nodes_devices_sign_device" /> | `EXEC` | <CopyableCode code="devicesId, nodesId" /> | Signs a device. |

## `SELECT` examples

Lists devices under a node or customer.

```sql
SELECT
name,
activeConfig,
currentChannels,
deviceMetadata,
displayName,
fccId,
grantRangeAllowlists,
grants,
preloadedConfig,
serialNumber,
state
FROM google.prod_tt_sasportal.devices
WHERE nodesId = '{{ nodesId }}';
```

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
INSERT INTO google.prod_tt_sasportal.devices (
nodesId,
activeConfig,
displayName,
deviceMetadata,
name,
serialNumber,
fccId,
grantRangeAllowlists,
state,
grants,
preloadedConfig
)
SELECT 
'{{ nodesId }}',
'{{ activeConfig }}',
'{{ displayName }}',
'{{ deviceMetadata }}',
'{{ name }}',
'{{ serialNumber }}',
'{{ fccId }}',
'{{ grantRangeAllowlists }}',
'{{ state }}',
'{{ grants }}',
'{{ preloadedConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: activeConfig
      value:
        - name: model
          value:
            - name: firmwareVersion
              value: string
            - name: softwareVersion
              value: string
            - name: name
              value: string
            - name: vendor
              value: string
            - name: hardwareVersion
              value: string
        - name: userId
          value: string
        - name: measurementCapabilities
          value:
            - string
        - name: airInterface
          value:
            - name: supportedSpec
              value: string
            - name: radioTechnology
              value: string
        - name: isSigned
          value: boolean
        - name: state
          value: string
        - name: category
          value: string
        - name: callSign
          value: string
        - name: updateTime
          value: string
        - name: installationParams
          value:
            - name: heightType
              value: string
            - name: longitude
              value: number
            - name: antennaAzimuth
              value: integer
            - name: horizontalAccuracy
              value: number
            - name: indoorDeployment
              value: boolean
            - name: eirpCapability
              value: integer
            - name: antennaGain
              value: number
            - name: antennaModel
              value: string
            - name: height
              value: number
            - name: cpeCbsdIndication
              value: boolean
            - name: antennaBeamwidth
              value: integer
            - name: verticalAccuracy
              value: number
            - name: antennaDowntilt
              value: integer
            - name: latitude
              value: number
    - name: displayName
      value: string
    - name: currentChannels
      value:
        - - name: frequencyRange
            value:
              - name: lowFrequencyMhz
                value: number
              - name: highFrequencyMhz
                value: number
          - name: score
            value: number
    - name: deviceMetadata
      value:
        - name: interferenceCoordinationGroup
          value: string
        - name: nrqzValidation
          value:
            - name: latitude
              value: number
            - name: state
              value: string
            - name: cpiId
              value: string
            - name: caseId
              value: string
            - name: longitude
              value: number
        - name: commonChannelGroup
          value: string
        - name: nrqzValidated
          value: boolean
        - name: antennaModel
          value: string
    - name: name
      value: string
    - name: serialNumber
      value: string
    - name: fccId
      value: string
    - name: grantRangeAllowlists
      value:
        - - name: lowFrequencyMhz
            value: number
          - name: highFrequencyMhz
            value: number
    - name: state
      value: string
    - name: grants
      value:
        - - name: channelType
            value: string
          - name: maxEirp
            value: number
          - name: expireTime
            value: string
          - name: lastHeartbeatTransmitExpireTime
            value: string
          - name: state
            value: string
          - name: grantId
            value: string
          - name: moveList
            value:
              - - name: dpaId
                  value: string
          - name: suspensionReason
            value:
              - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>devices</code> resource.

```sql
/*+ update */
UPDATE google.prod_tt_sasportal.devices
SET 
activeConfig = '{{ activeConfig }}',
displayName = '{{ displayName }}',
deviceMetadata = '{{ deviceMetadata }}',
name = '{{ name }}',
serialNumber = '{{ serialNumber }}',
fccId = '{{ fccId }}',
grantRangeAllowlists = '{{ grantRangeAllowlists }}',
state = '{{ state }}',
grants = '{{ grants }}',
preloadedConfig = '{{ preloadedConfig }}'
WHERE 
devicesId = '{{ devicesId }}'
AND nodesId = '{{ nodesId }}';
```

## `DELETE` example

Deletes the specified <code>devices</code> resource.

```sql
/*+ delete */
DELETE FROM google.prod_tt_sasportal.devices
WHERE devicesId = '{{ devicesId }}'
AND nodesId = '{{ nodesId }}';
```
