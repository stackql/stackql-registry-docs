---
title: diagnostics_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics_packages
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

Creates, updates, deletes, gets or lists a <code>diagnostics_packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>diagnostics_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.diagnostics_packages" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostics_packages', value: 'view', },
        { label: 'diagnostics_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="diagnosticsPackageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="packetCoreControlPlaneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Diagnostics package properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diagnosticsPackageName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Gets information about the specified diagnostics package. |
| <CopyableCode code="list_by_packet_core_control_plane" /> | `SELECT` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Lists all the diagnostics packages under a packet core control plane. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diagnosticsPackageName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Creates or updates a diagnostics package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diagnosticsPackageName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Deletes the specified diagnostics package. |

## `SELECT` examples

Lists all the diagnostics packages under a packet core control plane.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_diagnostics_packages', value: 'view', },
        { label: 'diagnostics_packages', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
diagnosticsPackageName,
packetCoreControlPlaneName,
provisioning_state,
reason,
resourceGroupName,
status,
subscriptionId
FROM azure.mobile_network.vw_diagnostics_packages
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.mobile_network.diagnostics_packages
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>diagnostics_packages</code> resource.

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
INSERT INTO azure.mobile_network.diagnostics_packages (
diagnosticsPackageName,
packetCoreControlPlaneName,
resourceGroupName,
subscriptionId
)
SELECT 
'{{ diagnosticsPackageName }}',
'{{ packetCoreControlPlaneName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>diagnostics_packages</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.diagnostics_packages
WHERE diagnosticsPackageName = '{{ diagnosticsPackageName }}'
AND packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
