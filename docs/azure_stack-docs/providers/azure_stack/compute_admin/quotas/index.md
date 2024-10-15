---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - compute_admin
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

Creates, updates, deletes, gets or lists a <code>quotas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.compute_admin.quotas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quotas', value: 'view', },
        { label: 'quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="availability_set_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="cores_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="ddagpu_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="max_allocation_premium_managed_disks_and_snapshots" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_allocation_standard_managed_disks_and_snapshots" /> | `text` | field from the `properties` object |
| <CopyableCode code="partitioned_gpu_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="quotaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
| <CopyableCode code="virtual_machine_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_scale_set_count" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties for a Compute Quota |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, quotaName, subscriptionId" /> | Get an existing Compute Quota. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get a list of existing Compute quotas. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="location, quotaName, subscriptionId" /> | Creates or Updates a Compute Quota with the provided quota parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="location, quotaName, subscriptionId" /> | Delete an existing Compute quota. |

## `SELECT` examples

Get a list of existing Compute quotas.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quotas', value: 'view', },
        { label: 'quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
availability_set_count,
cores_limit,
ddagpu_count,
location,
max_allocation_premium_managed_disks_and_snapshots,
max_allocation_standard_managed_disks_and_snapshots,
partitioned_gpu_count,
quotaName,
subscriptionId,
type,
virtual_machine_count,
vm_scale_set_count
FROM azure_stack.compute_admin.vw_quotas
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure_stack.compute_admin.quotas
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>quotas</code> resource.

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
INSERT INTO azure_stack.compute_admin.quotas (
location,
quotaName,
subscriptionId,
properties,
location
)
SELECT 
'{{ location }}',
'{{ quotaName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: availabilitySetCount
          value: integer
        - name: coresLimit
          value: integer
        - name: virtualMachineCount
          value: integer
        - name: vmScaleSetCount
          value: integer
        - name: maxAllocationStandardManagedDisksAndSnapshots
          value: integer
        - name: maxAllocationPremiumManagedDisksAndSnapshots
          value: integer
        - name: ddagpuCount
          value: integer
        - name: partitionedGpuCount
          value: integer
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>quotas</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.compute_admin.quotas
WHERE location = '{{ location }}'
AND quotaName = '{{ quotaName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
