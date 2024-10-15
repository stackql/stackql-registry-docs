---
title: extended_ue_information
hide_title: false
hide_table_of_contents: false
keywords:
  - extended_ue_information
  - mobile_network
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

Creates, updates, deletes, gets or lists a <code>extended_ue_information</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extended_ue_information</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.extended_ue_information" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_extended_ue_information', value: 'view', },
        { label: 'extended_ue_information', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="last_read_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="packetCoreControlPlaneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rat_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="ueId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Extended UE Information Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId, ueId" /> | Gets extended information about the specified UE from the packet core. |

## `SELECT` examples

Gets extended information about the specified UE from the packet core.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_extended_ue_information', value: 'view', },
        { label: 'extended_ue_information', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
last_read_at,
packetCoreControlPlaneName,
rat_type,
resourceGroupName,
subscriptionId,
ueId
FROM azure.mobile_network.vw_extended_ue_information
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND ueId = '{{ ueId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.mobile_network.extended_ue_information
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND ueId = '{{ ueId }}';
```
</TabItem></Tabs>

