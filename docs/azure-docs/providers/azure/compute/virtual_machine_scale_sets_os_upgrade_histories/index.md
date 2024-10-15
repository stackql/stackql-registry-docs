---
title: virtual_machine_scale_sets_os_upgrade_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_sets_os_upgrade_histories
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_scale_sets_os_upgrade_histories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_sets_os_upgrade_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_sets_os_upgrade_histories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes each OS upgrade on the Virtual Machine Scale Set. |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Gets list of OS upgrades on a VM scale set instance. |

## `SELECT` examples

Gets list of OS upgrades on a VM scale set instance.


```sql
SELECT
location,
properties,
type
FROM azure.compute.virtual_machine_scale_sets_os_upgrade_histories
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```