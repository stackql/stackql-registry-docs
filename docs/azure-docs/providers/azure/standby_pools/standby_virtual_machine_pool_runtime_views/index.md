---
title: standby_virtual_machine_pool_runtime_views
hide_title: false
hide_table_of_contents: false
keywords:
  - standby_virtual_machine_pool_runtime_views
  - standby_pools
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

Creates, updates, deletes, gets or lists a <code>standby_virtual_machine_pool_runtime_views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>standby_virtual_machine_pool_runtime_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.standby_pools.standby_virtual_machine_pool_runtime_views" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_standby_virtual_machine_pool_runtime_views', value: 'view', },
        { label: 'standby_virtual_machine_pool_runtime_views', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="instance_count_summary" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runtimeView" /> | `text` | field from the `properties` object |
| <CopyableCode code="standbyVirtualMachinePoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Contains information about a standby pool as last known by the StandbyPool resource provider. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, runtimeView, standbyVirtualMachinePoolName, subscriptionId" /> | Get a StandbyVirtualMachinePoolRuntimeViewResource |
| <CopyableCode code="list_by_standby_pool" /> | `SELECT` | <CopyableCode code="resourceGroupName, standbyVirtualMachinePoolName, subscriptionId" /> | List StandbyVirtualMachinePoolRuntimeViewResource resources by StandbyVirtualMachinePoolResource |

## `SELECT` examples

List StandbyVirtualMachinePoolRuntimeViewResource resources by StandbyVirtualMachinePoolResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_standby_virtual_machine_pool_runtime_views', value: 'view', },
        { label: 'standby_virtual_machine_pool_runtime_views', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
instance_count_summary,
provisioning_state,
resourceGroupName,
runtimeView,
standbyVirtualMachinePoolName,
subscriptionId
FROM azure.standby_pools.vw_standby_virtual_machine_pool_runtime_views
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND standbyVirtualMachinePoolName = '{{ standbyVirtualMachinePoolName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.standby_pools.standby_virtual_machine_pool_runtime_views
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND standbyVirtualMachinePoolName = '{{ standbyVirtualMachinePoolName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>
