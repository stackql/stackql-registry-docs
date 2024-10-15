---
title: bare_metal_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - bare_metal_machines
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

Creates, updates, deletes, gets or lists a <code>bare_metal_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bare_metal_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.bare_metal_machines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bare_metal_machines', value: 'view', },
        { label: 'bare_metal_machines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="associated_resource_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="bareMetalMachineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="bmc_connection_string" /> | `text` | field from the `properties` object |
| <CopyableCode code="bmc_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="bmc_mac_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="boot_mac_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cordon_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hardware_inventory" /> | `text` | field from the `properties` object |
| <CopyableCode code="hardware_validation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="hybrid_aks_clusters_associated_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetes_node_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetes_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="machine_cluster_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_roles" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_sku_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="oam_ipv4_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="oam_ipv6_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_image" /> | `text` | field from the `properties` object |
| <CopyableCode code="power_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="rack_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="rack_slot" /> | `text` | field from the `properties` object |
| <CopyableCode code="ready_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runtime_protection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_rotation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="virtual_machines_associated_ids" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Get properties of the provided bare metal machine. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get a list of bare metal machines in the provided resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of bare metal machines in the provided subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new bare metal machine or update the properties of the existing one.
All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Delete the provided bare metal machine.
All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Patch properties of the provided bare metal machine, or update tags associated with the bare metal machine. Properties and tag updates can be done independently. |
| <CopyableCode code="cordon" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Cordon the provided bare metal machine's Kubernetes node. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Power off the provided bare metal machine. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Reimage the provided bare metal machine. |
| <CopyableCode code="replace" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Replace the provided bare metal machine. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Restart the provided bare metal machine. |
| <CopyableCode code="run_command" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId, data__limitTimeSeconds, data__script" /> | Run the command or the script on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available. |
| <CopyableCode code="run_data_extracts" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId, data__commands, data__limitTimeSeconds" /> | Run one or more data extractions on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available. |
| <CopyableCode code="run_read_commands" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId, data__commands, data__limitTimeSeconds" /> | Run one or more read-only commands on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Start the provided bare metal machine. |
| <CopyableCode code="uncordon" /> | `EXEC` | <CopyableCode code="bareMetalMachineName, resourceGroupName, subscriptionId" /> | Uncordon the provided bare metal machine's Kubernetes node. |

## `SELECT` examples

Get a list of bare metal machines in the provided subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bare_metal_machines', value: 'view', },
        { label: 'bare_metal_machines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
associated_resource_ids,
bareMetalMachineName,
bmc_connection_string,
bmc_credentials,
bmc_mac_address,
boot_mac_address,
cluster_id,
cordon_status,
detailed_status,
detailed_status_message,
extended_location,
hardware_inventory,
hardware_validation_status,
hybrid_aks_clusters_associated_ids,
kubernetes_node_name,
kubernetes_version,
location,
machine_cluster_version,
machine_details,
machine_name,
machine_roles,
machine_sku_id,
oam_ipv4_address,
oam_ipv6_address,
os_image,
power_state,
provisioning_state,
rack_id,
rack_slot,
ready_state,
resourceGroupName,
runtime_protection_status,
secret_rotation_status,
serial_number,
service_tag,
subscriptionId,
tags,
virtual_machines_associated_ids
FROM azure.nexus.vw_bare_metal_machines
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
FROM azure.nexus.bare_metal_machines
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bare_metal_machines</code> resource.

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
INSERT INTO azure.nexus.bare_metal_machines (
bareMetalMachineName,
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
'{{ bareMetalMachineName }}',
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
        - name: associatedResourceIds
          value:
            - string
        - name: bmcConnectionString
          value: string
        - name: bmcCredentials
          value:
            - name: password
              value: string
            - name: username
              value: string
        - name: bmcMacAddress
          value: string
        - name: bootMacAddress
          value: string
        - name: clusterId
          value: string
        - name: cordonStatus
          value: string
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: hardwareInventory
          value:
            - name: additionalHostInformation
              value: string
            - name: interfaces
              value:
                - - name: linkStatus
                    value: string
                  - name: macAddress
                    value: string
                  - name: name
                    value: string
                  - name: networkInterfaceId
                    value: string
            - name: nics
              value:
                - - name: lldpNeighbor
                    value:
                      - name: portDescription
                        value: string
                      - name: portName
                        value: string
                      - name: systemDescription
                        value: string
                      - name: systemName
                        value: string
                  - name: macAddress
                    value: string
                  - name: name
                    value: string
        - name: hardwareValidationStatus
          value:
            - name: lastValidationTime
              value: string
            - name: result
              value: string
        - name: hybridAksClustersAssociatedIds
          value:
            - string
        - name: kubernetesNodeName
          value: string
        - name: kubernetesVersion
          value: string
        - name: machineClusterVersion
          value: string
        - name: machineDetails
          value: string
        - name: machineName
          value: string
        - name: machineRoles
          value:
            - string
        - name: machineSkuId
          value: string
        - name: oamIpv4Address
          value: string
        - name: oamIpv6Address
          value: string
        - name: osImage
          value: string
        - name: powerState
          value: string
        - name: provisioningState
          value: string
        - name: rackId
          value: string
        - name: rackSlot
          value: integer
        - name: readyState
          value: string
        - name: runtimeProtectionStatus
          value:
            - name: definitionsLastUpdated
              value: string
            - name: definitionsVersion
              value: string
            - name: scanCompletedTime
              value: string
            - name: scanScheduledTime
              value: string
            - name: scanStartedTime
              value: string
        - name: secretRotationStatus
          value:
            - - name: expirePeriodDays
                value: integer
              - name: lastRotationTime
                value: string
              - name: rotationPeriodDays
                value: integer
              - name: secretArchiveReference
                value:
                  - name: keyVaultId
                    value: string
                  - name: secretName
                    value: string
                  - name: secretVersion
                    value: string
              - name: secretType
                value: string
        - name: serialNumber
          value: string
        - name: serviceTag
          value: string
        - name: virtualMachinesAssociatedIds
          value:
            - string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>bare_metal_machines</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.bare_metal_machines
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
bareMetalMachineName = '{{ bareMetalMachineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>bare_metal_machines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.bare_metal_machines
WHERE bareMetalMachineName = '{{ bareMetalMachineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
