---
title: packet_core_control_planes
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_core_control_planes
  - mobile_network
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

Creates, updates, deletes, gets or lists a <code>packet_core_control_planes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packet_core_control_planes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.packet_core_control_planes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_packet_core_control_planes', value: 'view', },
        { label: 'packet_core_control_planes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="control_plane_access_interface" /> | `text` | field from the `properties` object |
| <CopyableCode code="control_plane_access_virtual_ipv4_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="core_network_technology" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics_upload" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_hub" /> | `text` | field from the `properties` object |
| <CopyableCode code="home_network_private_keys_provisioning" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (User assigned identity) |
| <CopyableCode code="installation" /> | `text` | field from the `properties` object |
| <CopyableCode code="installed_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="interop_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_diagnostics_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="packetCoreControlPlaneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="platform" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rollback_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="signaling" /> | `text` | field from the `properties` object |
| <CopyableCode code="sites" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="ue_mtu" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_consent" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (User assigned identity) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Packet core control plane properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Gets information about the specified packet core control plane. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the packet core control planes in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the packet core control planes in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a packet core control plane. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Deletes the specified packet core control plane. |
| <CopyableCode code="collect_diagnostics_package" /> | `EXEC` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId, data__storageAccountBlobUrl" /> | Collect a diagnostics package for the specified packet core control plane. This action will upload the diagnostics to a storage account. |
| <CopyableCode code="reinstall" /> | `EXEC` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Reinstall the specified packet core control plane. This action will try to restore the packet core to the installed state that was disrupted by a transient failure. This action will cause a service outage. |
| <CopyableCode code="rollback" /> | `EXEC` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Roll back the specified packet core control plane to the previous version, "rollbackVersion". Multiple consecutive rollbacks are not possible. This action may cause a service outage. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Patch packet core control plane resource. |

## `SELECT` examples

Lists all the packet core control planes in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_packet_core_control_planes', value: 'view', },
        { label: 'packet_core_control_planes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
control_plane_access_interface,
control_plane_access_virtual_ipv4_addresses,
core_network_technology,
diagnostics_upload,
event_hub,
home_network_private_keys_provisioning,
identity,
installation,
installed_version,
interop_settings,
local_diagnostics_access,
location,
packetCoreControlPlaneName,
platform,
provisioning_state,
resourceGroupName,
rollback_version,
signaling,
sites,
sku,
subscriptionId,
tags,
ue_mtu,
user_consent,
version
FROM azure.mobile_network.vw_packet_core_control_planes
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.mobile_network.packet_core_control_planes
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>packet_core_control_planes</code> resource.

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
INSERT INTO azure.mobile_network.packet_core_control_planes (
packetCoreControlPlaneName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
identity,
tags,
location
)
SELECT 
'{{ packetCoreControlPlaneName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: provisioningState
          value: []
        - name: installation
          value:
            - name: desiredState
              value: []
            - name: state
              value: []
            - name: reinstallRequired
              value: []
            - name: reasons
              value:
                - []
            - name: operation
              value:
                - name: id
                  value: string
        - name: sites
          value:
            - - name: id
                value: string
        - name: platform
          value:
            - name: type
              value: []
            - name: azureStackEdgeDevice
              value:
                - name: id
                  value: string
            - name: azureStackEdgeDevices
              value:
                - - name: id
                    value: string
            - name: azureStackHciCluster
              value:
                - name: id
                  value: string
            - name: connectedCluster
              value:
                - name: id
                  value: string
            - name: customLocation
              value:
                - name: id
                  value: string
        - name: coreNetworkTechnology
          value: []
        - name: version
          value: string
        - name: installedVersion
          value: string
        - name: rollbackVersion
          value: string
        - name: controlPlaneAccessInterface
          value:
            - name: name
              value: string
            - name: ipv4Address
              value: []
            - name: ipv4Subnet
              value: []
            - name: vlanId
              value: integer
            - name: ipv4AddressList
              value:
                - []
            - name: bfdIpv4Endpoints
              value:
                - []
        - name: controlPlaneAccessVirtualIpv4Addresses
          value:
            - []
        - name: sku
          value: []
        - name: ueMtu
          value: integer
        - name: localDiagnosticsAccess
          value:
            - name: authenticationType
              value: string
            - name: httpsServerCertificate
              value:
                - name: certificateUrl
                  value: string
                - name: provisioning
                  value:
                    - name: state
                      value: string
                    - name: reason
                      value: string
        - name: diagnosticsUpload
          value:
            - name: storageAccountContainerUrl
              value: string
        - name: eventHub
          value:
            - name: id
              value: string
            - name: reportingInterval
              value: integer
        - name: signaling
          value:
            - name: nasReroute
              value:
                - name: macroMmeGroupId
                  value: integer
            - name: nasEncryption
              value:
                - []
        - name: interopSettings
          value: object
        - name: homeNetworkPrivateKeysProvisioning
          value:
            - name: state
              value: string
        - name: userConsent
          value:
            - name: allowSupportTelemetryAccess
              value: boolean
    - name: identity
      value:
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>packet_core_control_planes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.packet_core_control_planes
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
