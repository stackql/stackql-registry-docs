---
title: interfaces_virtual_machine_scale_set_network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - interfaces_virtual_machine_scale_set_network_interfaces
  - network
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

Creates, updates, deletes, gets or lists a <code>interfaces_virtual_machine_scale_set_network_interfaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>interfaces_virtual_machine_scale_set_network_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.interfaces_virtual_machine_scale_set_network_interfaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_interfaces_virtual_machine_scale_set_network_interfaces', value: 'view', },
        { label: 'interfaces_virtual_machine_scale_set_network_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="auxiliary_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="auxiliary_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_tcp_state_tracking" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="dscp_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_accelerated_networking" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_ip_forwarding" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="hosted_workloads" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="mac_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="migration_phase" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkInterfaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_security_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="nic_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tap_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtualMachineScaleSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_machine" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualmachineIndex" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_encryption_supported" /> | `text` | field from the `properties` object |
| <CopyableCode code="workload_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation complex type. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | NetworkInterface properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex" /> | Get the specified network interface in a virtual machine scale set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineScaleSetName" /> | Gets all network interfaces in a virtual machine scale set. |

## `SELECT` examples

Gets all network interfaces in a virtual machine scale set.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_interfaces_virtual_machine_scale_set_network_interfaces', value: 'view', },
        { label: 'interfaces_virtual_machine_scale_set_network_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
auxiliary_mode,
auxiliary_sku,
disable_tcp_state_tracking,
dns_settings,
dscp_configuration,
enable_accelerated_networking,
enable_ip_forwarding,
etag,
extended_location,
hosted_workloads,
ip_configurations,
location,
mac_address,
migration_phase,
networkInterfaceName,
network_security_group,
nic_type,
primary,
private_endpoint,
private_link_service,
provisioning_state,
resourceGroupName,
resource_guid,
subscriptionId,
tags,
tap_configurations,
type,
virtualMachineScaleSetName,
virtual_machine,
virtualmachineIndex,
vnet_encryption_supported,
workload_type
FROM azure.network.vw_interfaces_virtual_machine_scale_set_network_interfaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineScaleSetName = '{{ virtualMachineScaleSetName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
extendedLocation,
location,
properties,
tags,
type
FROM azure.network.interfaces_virtual_machine_scale_set_network_interfaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineScaleSetName = '{{ virtualMachineScaleSetName }}';
```
</TabItem></Tabs>

