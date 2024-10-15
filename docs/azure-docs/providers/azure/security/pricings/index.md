---
title: pricings
hide_title: false
hide_table_of_contents: false
keywords:
  - pricings
  - security
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

Creates, updates, deletes, gets or lists a <code>pricings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pricings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.pricings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pricings', value: 'view', },
        { label: 'pricings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="deprecated" /> | `text` | field from the `properties` object |
| <CopyableCode code="enablement_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="enforce" /> | `text` | field from the `properties` object |
| <CopyableCode code="extensions" /> | `text` | field from the `properties` object |
| <CopyableCode code="free_trial_remaining_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="inherited" /> | `text` | field from the `properties` object |
| <CopyableCode code="inherited_from" /> | `text` | field from the `properties` object |
| <CopyableCode code="pricingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="pricing_tier" /> | `text` | field from the `properties` object |
| <CopyableCode code="replaced_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="resources_coverage_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopeId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sub_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Pricing properties for the relevant scope |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pricingName, scopeId" /> | Get the Defender plans pricing configurations of the selected scope (valid scopes are resource id or a subscription id). At the resource level, supported resource types are 'VirtualMachines, VMSS and ARC Machines'. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scopeId" /> | Lists Microsoft Defender for Cloud pricing configurations of the scopeId, that match the optional given $filter. Valid scopes are: subscription id or a specific resource id (Supported resources are: 'VirtualMachines, VMSS and ARC Machines'). Valid $filter is: 'name in ({planName1},{planName2},...)'. If $filter is not provided, the unfiltered list will be returned. If '$filter=name in (planName1,planName2)' is provided, the returned list includes the pricings set for 'planName1' and 'planName2' only. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="pricingName, scopeId" /> | Deletes a provided Microsoft Defender for Cloud pricing configuration in a specific resource. Valid only for resource scope (Supported resources are: 'VirtualMachines, VMSS and ARC MachinesS'). |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="pricingName, scopeId" /> | Updates a provided Microsoft Defender for Cloud pricing configuration in the scope. Valid scopes are: subscription id or a specific resource id (Supported resources are: 'VirtualMachines, VMSS and ARC Machines' and only for plan='VirtualMachines' and subPlan='P1'). |

## `SELECT` examples

Lists Microsoft Defender for Cloud pricing configurations of the scopeId, that match the optional given $filter. Valid scopes are: subscription id or a specific resource id (Supported resources are: 'VirtualMachines, VMSS and ARC Machines'). Valid $filter is: 'name in ({planName1},{planName2},...)'. If $filter is not provided, the unfiltered list will be returned. If '$filter=name in (planName1,planName2)' is provided, the returned list includes the pricings set for 'planName1' and 'planName2' only.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pricings', value: 'view', },
        { label: 'pricings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
deprecated,
enablement_time,
enforce,
extensions,
free_trial_remaining_time,
inherited,
inherited_from,
pricingName,
pricing_tier,
replaced_by,
resources_coverage_status,
scopeId,
sub_plan,
type
FROM azure.security.vw_pricings
WHERE scopeId = '{{ scopeId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.pricings
WHERE scopeId = '{{ scopeId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>pricings</code> resource.

```sql
/*+ update */
REPLACE azure.security.pricings
SET 
properties = '{{ properties }}'
WHERE 
pricingName = '{{ pricingName }}'
AND scopeId = '{{ scopeId }}';
```

## `DELETE` example

Deletes the specified <code>pricings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.pricings
WHERE pricingName = '{{ pricingName }}'
AND scopeId = '{{ scopeId }}';
```
