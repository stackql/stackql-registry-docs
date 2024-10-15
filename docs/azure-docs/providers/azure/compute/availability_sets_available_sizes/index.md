---
title: availability_sets_available_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_sets_available_sizes
  - compute
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

Creates, updates, deletes, gets or lists a <code>availability_sets_available_sizes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>availability_sets_available_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.availability_sets_available_sizes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the virtual machine size. |
| <CopyableCode code="maxDataDiskCount" /> | `integer` | The maximum number of data disks that can be attached to the virtual machine size. |
| <CopyableCode code="memoryInMB" /> | `integer` | The amount of memory, in MB, supported by the virtual machine size. |
| <CopyableCode code="numberOfCores" /> | `integer` | The number of cores supported by the virtual machine size. For Constrained vCPU capable VM sizes, this number represents the total vCPUs of quota that the VM uses. For accurate vCPU count, please refer to https://docs.microsoft.com/azure/virtual-machines/constrained-vcpu or https://docs.microsoft.com/rest/api/compute/resourceskus/list |
| <CopyableCode code="osDiskSizeInMB" /> | `integer` | The OS disk size, in MB, allowed by the virtual machine size. |
| <CopyableCode code="resourceDiskSizeInMB" /> | `integer` | The resource disk size, in MB, allowed by the virtual machine size. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="availabilitySetName, resourceGroupName, subscriptionId" /> | Lists all available virtual machine sizes that can be used to create a new virtual machine in an existing availability set. |

## `SELECT` examples

Lists all available virtual machine sizes that can be used to create a new virtual machine in an existing availability set.


```sql
SELECT
name,
maxDataDiskCount,
memoryInMB,
numberOfCores,
osDiskSizeInMB,
resourceDiskSizeInMB
FROM azure.compute.availability_sets_available_sizes
WHERE availabilitySetName = '{{ availabilitySetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```