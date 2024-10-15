---
title: virtual_machine_scale_set_rolling_upgrades_latest
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_rolling_upgrades_latest
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_scale_set_rolling_upgrades_latest</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_rolling_upgrades_latest</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_set_rolling_upgrades_latest" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_scale_set_rolling_upgrades_latest', value: 'view', },
        { label: 'virtual_machine_scale_set_rolling_upgrades_latest', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="running_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="vmScaleSetName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The status of the latest virtual machine scale set rolling upgrade. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Gets the status of the latest virtual machine scale set rolling upgrade. |

## `SELECT` examples

Gets the status of the latest virtual machine scale set rolling upgrade.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_scale_set_rolling_upgrades_latest', value: 'view', },
        { label: 'virtual_machine_scale_set_rolling_upgrades_latest', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
error,
location,
policy,
progress,
resourceGroupName,
running_status,
subscriptionId,
tags,
type,
vmScaleSetName
FROM azure.compute.vw_virtual_machine_scale_set_rolling_upgrades_latest
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.compute.virtual_machine_scale_set_rolling_upgrades_latest
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```
</TabItem></Tabs>

