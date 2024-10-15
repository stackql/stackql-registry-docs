---
title: fleets_virtual_machine_scale_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets_virtual_machine_scale_sets
  - azure_fleet
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

Creates, updates, deletes, gets or lists a <code>fleets_virtual_machine_scale_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets_virtual_machine_scale_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_fleet.fleets_virtual_machine_scale_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The compute RP resource id of the virtualMachineScaleSet 
"subscriptions/{subId}/resourceGroups/{rgName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}" |
| <CopyableCode code="name" /> | `string` | The name of the virtualMachineScaleSet |
| <CopyableCode code="error" /> | `object` | ApiError for Fleet |
| <CopyableCode code="operationStatus" /> | `string` | The status of the current operation. |
| <CopyableCode code="type" /> | `string` | Type of the virtualMachineScaleSet |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | List VirtualMachineScaleSet resources by Fleet |

## `SELECT` examples

List VirtualMachineScaleSet resources by Fleet


```sql
SELECT
id,
name,
error,
operationStatus,
type
FROM azure.azure_fleet.fleets_virtual_machine_scale_sets
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```