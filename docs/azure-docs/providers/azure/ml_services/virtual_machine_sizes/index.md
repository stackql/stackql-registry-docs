---
title: virtual_machine_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_sizes
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_sizes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.virtual_machine_sizes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the virtual machine size. |
| <CopyableCode code="estimatedVMPrices" /> | `object` | The estimated price info for using a VM. |
| <CopyableCode code="family" /> | `string` | The family name of the virtual machine size. |
| <CopyableCode code="gpus" /> | `integer` | The number of gPUs supported by the virtual machine size. |
| <CopyableCode code="lowPriorityCapable" /> | `boolean` | Specifies if the virtual machine size supports low priority VMs. |
| <CopyableCode code="maxResourceVolumeMB" /> | `integer` | The resource volume size, in MB, allowed by the virtual machine size. |
| <CopyableCode code="memoryGB" /> | `number` | The amount of memory, in GB, supported by the virtual machine size. |
| <CopyableCode code="osVhdSizeMB" /> | `integer` | The OS VHD disk size, in MB, allowed by the virtual machine size. |
| <CopyableCode code="premiumIO" /> | `boolean` | Specifies if the virtual machine size supports premium IO. |
| <CopyableCode code="supportedComputeTypes" /> | `array` | Specifies the compute types supported by the virtual machine size. |
| <CopyableCode code="vCPUs" /> | `integer` | The number of vCPUs supported by the virtual machine size. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns supported VM Sizes in a location |

## `SELECT` examples

Returns supported VM Sizes in a location


```sql
SELECT
name,
estimatedVMPrices,
family,
gpus,
lowPriorityCapable,
maxResourceVolumeMB,
memoryGB,
osVhdSizeMB,
premiumIO,
supportedComputeTypes,
vCPUs
FROM azure.ml_services.virtual_machine_sizes
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```