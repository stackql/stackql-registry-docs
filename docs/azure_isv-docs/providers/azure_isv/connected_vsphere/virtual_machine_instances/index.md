---
title: virtual_machine_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_instances
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.connected_vsphere.virtual_machine_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_instances', value: 'view', },
        { label: 'virtual_machine_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hardware_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="infrastructure_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="placement_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="power_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_uid" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="statuses" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine Instance. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Retrieves information about a virtual machine instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Lists all of the virtual machine instances within the specified parent resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceUri, data__properties" /> | The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri" /> | The operation to delete a virtual machine instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceUri" /> | The operation to update a virtual machine instance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to restart a virtual machine instance. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to start a virtual machine instance. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to power off (stop) a virtual machine instance. |

## `SELECT` examples

Retrieves information about a virtual machine instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_instances', value: 'view', },
        { label: 'virtual_machine_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
extended_location,
hardware_profile,
infrastructure_profile,
network_profile,
os_profile,
placement_profile,
power_state,
provisioning_state,
resourceUri,
resource_uid,
security_profile,
statuses,
storage_profile
FROM azure_isv.connected_vsphere.vw_virtual_machine_instances
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
properties
FROM azure_isv.connected_vsphere.virtual_machine_instances
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machine_instances</code> resource.

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
INSERT INTO azure_isv.connected_vsphere.virtual_machine_instances (
resourceUri,
data__properties,
properties,
extendedLocation
)
SELECT 
'{{ resourceUri }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ extendedLocation }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: placementProfile
          value:
            - name: resourcePoolId
              value: string
            - name: clusterId
              value: string
            - name: hostId
              value: string
            - name: datastoreId
              value: string
        - name: osProfile
          value:
            - name: computerName
              value: string
            - name: adminUsername
              value: string
            - name: adminPassword
              value: string
            - name: guestId
              value: string
            - name: osType
              value: []
            - name: osSku
              value: string
            - name: toolsRunningStatus
              value: string
            - name: toolsVersionStatus
              value: string
            - name: toolsVersion
              value: string
            - name: windowsConfiguration
              value:
                - name: fullName
                  value: string
                - name: orgName
                  value: string
                - name: domainName
                  value: string
                - name: domainUsername
                  value: string
                - name: domainUserPassword
                  value: string
                - name: workGroupName
                  value: string
                - name: productId
                  value: string
                - name: autoLogon
                  value: boolean
                - name: autoLogonCount
                  value: integer
                - name: timeZone
                  value: string
                - name: firstLogonCommands
                  value:
                    - string
        - name: hardwareProfile
          value:
            - name: memorySizeMB
              value: integer
            - name: numCPUs
              value: integer
            - name: numCoresPerSocket
              value: integer
            - name: cpuHotAddEnabled
              value: boolean
            - name: cpuHotRemoveEnabled
              value: boolean
            - name: memoryHotAddEnabled
              value: boolean
        - name: networkProfile
          value:
            - name: networkInterfaces
              value:
                - - name: name
                    value: string
                  - name: label
                    value: string
                  - name: ipAddresses
                    value:
                      - string
                  - name: macAddress
                    value: string
                  - name: networkId
                    value: string
                  - name: nicType
                    value: []
                  - name: powerOnBoot
                    value: []
                  - name: networkMoRefId
                    value: string
                  - name: networkMoName
                    value: string
                  - name: deviceKey
                    value: integer
                  - name: ipSettings
                    value:
                      - name: allocationMethod
                        value: []
                      - name: dnsServers
                        value:
                          - string
                      - name: gateway
                        value:
                          - string
                      - name: ipAddress
                        value: string
                      - name: subnetMask
                        value: string
                      - name: primaryWinsServer
                        value: string
                      - name: secondaryWinsServer
                        value: string
                      - name: ipAddressInfo
                        value:
                          - - name: allocationMethod
                              value: string
                            - name: ipAddress
                              value: string
                            - name: subnetMask
                              value: string
        - name: storageProfile
          value:
            - name: disks
              value:
                - - name: name
                    value: string
                  - name: label
                    value: string
                  - name: diskObjectId
                    value: string
                  - name: diskSizeGB
                    value: integer
                  - name: deviceKey
                    value: integer
                  - name: diskMode
                    value: []
                  - name: controllerKey
                    value: integer
                  - name: unitNumber
                    value: integer
                  - name: deviceName
                    value: string
                  - name: diskType
                    value: []
            - name: scsiControllers
              value:
                - - name: type
                    value: []
                  - name: controllerKey
                    value: integer
                  - name: busNumber
                    value: integer
                  - name: scsiCtlrUnitNumber
                    value: integer
                  - name: sharing
                    value: []
        - name: securityProfile
          value:
            - name: uefiSettings
              value:
                - name: secureBootEnabled
                  value: boolean
        - name: infrastructureProfile
          value:
            - name: templateId
              value: string
            - name: vCenterId
              value: string
            - name: moRefId
              value: string
            - name: inventoryItemId
              value: string
            - name: moName
              value: string
            - name: folderPath
              value: string
            - name: instanceUuid
              value: string
            - name: smbiosUuid
              value: string
            - name: firmwareType
              value: []
            - name: customResourceName
              value: string
        - name: powerState
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
        - name: resourceUid
          value: string
    - name: extendedLocation
      value:
        - name: type
          value: string
        - name: name
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machine_instances</code> resource.

```sql
/*+ update */
UPDATE azure_isv.connected_vsphere.virtual_machine_instances
SET 
properties = '{{ properties }}'
WHERE 
resourceUri = '{{ resourceUri }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machine_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.connected_vsphere.virtual_machine_instances
WHERE resourceUri = '{{ resourceUri }}';
```
