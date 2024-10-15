---
title: public_ip_addresses_virtual_machine_scale_set_vm_public_ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ip_addresses_virtual_machine_scale_set_vm_public_ip_addresses
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

Creates, updates, deletes, gets or lists a <code>public_ip_addresses_virtual_machine_scale_set_vm_public_ip_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_ip_addresses_virtual_machine_scale_set_vm_public_ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.public_ip_addresses_virtual_machine_scale_set_vm_public_ip_addresses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation complex type. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Public IP address properties. |
| <CopyableCode code="sku" /> | `object` | SKU of a public IP address. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="ipConfigurationName, networkInterfaceName, resourceGroupName, subscriptionId, virtualMachineScaleSetName, virtualmachineIndex" /> | Gets information about all public IP addresses in a virtual machine IP configuration in a virtual machine scale set. |

## `SELECT` examples

Gets information about all public IP addresses in a virtual machine IP configuration in a virtual machine scale set.


```sql
SELECT
id,
name,
etag,
extendedLocation,
location,
properties,
sku,
tags,
type,
zones
FROM azure.network.public_ip_addresses_virtual_machine_scale_set_vm_public_ip_addresses
WHERE ipConfigurationName = '{{ ipConfigurationName }}'
AND networkInterfaceName = '{{ networkInterfaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineScaleSetName = '{{ virtualMachineScaleSetName }}'
AND virtualmachineIndex = '{{ virtualmachineIndex }}';
```