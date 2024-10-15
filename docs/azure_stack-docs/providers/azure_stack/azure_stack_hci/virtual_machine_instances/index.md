---
title: virtual_machine_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_instances
  - azure_stack_hci
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.virtual_machine_instances" /></td></tr>
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
| <CopyableCode code="guest_agent_install_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="hardware_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="http_proxy_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="instance_view" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_uid" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="properties" /> | `object` | Properties under the virtual machine instance resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Gets a virtual machine instance |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Lists all of the virtual machine instances within the specified parent resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceUri" /> | The operation to create or update a virtual machine instance. Please note some properties can be set only during virtual machine instance creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri" /> | The operation to delete a virtual machine instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceUri" /> | The operation to update a virtual machine instance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to restart a virtual machine instance. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to start a virtual machine instance. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="resourceUri" /> | The operation to stop a virtual machine instance. |

## `SELECT` examples

Gets a virtual machine instance

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
guest_agent_install_status,
hardware_profile,
http_proxy_config,
identity,
instance_view,
network_profile,
os_profile,
provisioning_state,
resourceUri,
resource_uid,
security_profile,
status,
storage_profile,
vm_id
FROM azure_stack.azure_stack_hci.vw_virtual_machine_instances
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
identity,
properties
FROM azure_stack.azure_stack_hci.virtual_machine_instances
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
INSERT INTO azure_stack.azure_stack_hci.virtual_machine_instances (
resourceUri,
properties,
extendedLocation,
identity
)
SELECT 
'{{ resourceUri }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: hardwareProfile
          value:
            - name: vmSize
              value: string
            - name: processors
              value: integer
            - name: memoryMB
              value: integer
            - name: dynamicMemoryConfig
              value:
                - name: maximumMemoryMB
                  value: integer
                - name: minimumMemoryMB
                  value: integer
                - name: targetMemoryBuffer
                  value: integer
        - name: networkProfile
          value:
            - name: networkInterfaces
              value:
                - - name: id
                    value: string
        - name: osProfile
          value:
            - name: adminPassword
              value: string
            - name: adminUsername
              value: string
            - name: computerName
              value: string
            - name: linuxConfiguration
              value:
                - name: disablePasswordAuthentication
                  value: boolean
                - name: ssh
                  value:
                    - name: publicKeys
                      value:
                        - - name: path
                            value: string
                          - name: keyData
                            value: string
                - name: provisionVMAgent
                  value: boolean
                - name: provisionVMConfigAgent
                  value: boolean
            - name: windowsConfiguration
              value:
                - name: enableAutomaticUpdates
                  value: boolean
                - name: timeZone
                  value: string
                - name: provisionVMAgent
                  value: boolean
                - name: provisionVMConfigAgent
                  value: boolean
        - name: securityProfile
          value:
            - name: enableTPM
              value: boolean
            - name: uefiSettings
              value:
                - name: secureBootEnabled
                  value: boolean
            - name: securityType
              value: string
        - name: storageProfile
          value:
            - name: dataDisks
              value:
                - - name: id
                    value: string
            - name: imageReference
              value:
                - name: id
                  value: string
            - name: osDisk
              value:
                - name: id
                  value: string
                - name: osType
                  value: string
            - name: vmConfigStoragePathId
              value: string
        - name: httpProxyConfig
          value:
            - name: httpProxy
              value: string
            - name: httpsProxy
              value: string
            - name: noProxy
              value:
                - string
            - name: trustedCa
              value: string
        - name: provisioningState
          value: string
        - name: instanceView
          value:
            - name: vmAgent
              value:
                - name: vmConfigAgentVersion
                  value: string
                - name: statuses
                  value:
                    - - name: code
                        value: string
                      - name: level
                        value: string
                      - name: displayStatus
                        value: string
                      - name: message
                        value: string
                      - name: time
                        value: string
        - name: status
          value:
            - name: errorCode
              value: string
            - name: errorMessage
              value: string
            - name: powerState
              value: string
            - name: provisioningStatus
              value:
                - name: operationId
                  value: string
                - name: status
                  value: string
        - name: guestAgentInstallStatus
          value:
            - name: vmUuid
              value: string
            - name: status
              value: string
            - name: lastStatusChange
              value: string
            - name: agentVersion
              value: string
            - name: errorDetails
              value:
                - - name: code
                    value: string
                  - name: message
                    value: string
                  - name: target
                    value: string
                  - name: details
                    value:
                      - - name: code
                          value: string
                        - name: message
                          value: string
                        - name: target
                          value: string
                        - name: details
                          value:
                            - - name: code
                                value: string
                              - name: message
                                value: string
                              - name: target
                                value: string
                              - name: details
                                value:
                                  - - name: code
                                      value: string
                                    - name: message
                                      value: string
                                    - name: target
                                      value: string
                                    - name: details
                                      value:
                                        - - name: code
                                            value: string
                                          - name: message
                                            value: string
                                          - name: target
                                            value: string
                                          - name: details
                                            value:
                                              - - name: code
                                                  value: string
                                                - name: message
                                                  value: string
                                                - name: target
                                                  value: string
                                                - name: details
                                                  value:
                                                    - - name: code
                                                        value: string
                                                      - name: message
                                                        value: string
                                                      - name: target
                                                        value: string
                                                      - name: details
                                                        value:
                                                          - - name: code
                                                              value: string
                                                            - name: message
                                                              value: string
                                                            - name: target
                                                              value: string
                                                            - name: details
                                                              value:
                                                                - []
                                                            - name: additionalInfo
                                                              value:
                                                                - []
                                                      - name: additionalInfo
                                                        value:
                                                          - - name: type
                                                              value: string
                                                            - name: info
                                                              value: object
                                                - name: additionalInfo
                                                  value:
                                                    - - name: type
                                                        value: string
                                                      - name: info
                                                        value: object
                                          - name: additionalInfo
                                            value:
                                              - - name: type
                                                  value: string
                                                - name: info
                                                  value: object
                                    - name: additionalInfo
                                      value:
                                        - - name: type
                                            value: string
                                          - name: info
                                            value: object
                              - name: additionalInfo
                                value:
                                  - - name: type
                                      value: string
                                    - name: info
                                      value: object
                        - name: additionalInfo
                          value:
                            - - name: type
                                value: string
                              - name: info
                                value: object
                  - name: additionalInfo
                    value:
                      - - name: type
                          value: string
                        - name: info
                          value: object
        - name: vmId
          value: string
        - name: resourceUid
          value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machine_instances</code> resource.

```sql
/*+ update */
UPDATE azure_stack.azure_stack_hci.virtual_machine_instances
SET 
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resourceUri = '{{ resourceUri }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machine_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.virtual_machine_instances
WHERE resourceUri = '{{ resourceUri }}';
```
