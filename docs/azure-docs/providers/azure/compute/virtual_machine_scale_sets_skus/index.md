---
title: virtual_machine_scale_sets_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_sets_skus
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_scale_sets_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_sets_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_sets_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | Describes scaling information of a sku. |
| <CopyableCode code="resourceType" /> | `string` | The type of resource the sku applies to. |
| <CopyableCode code="sku" /> | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Gets a list of SKUs available for your VM scale set, including the minimum and maximum VM instances allowed for each SKU. |

## `SELECT` examples

Gets a list of SKUs available for your VM scale set, including the minimum and maximum VM instances allowed for each SKU.


```sql
SELECT
capacity,
resourceType,
sku
FROM azure.compute.virtual_machine_scale_sets_skus
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```