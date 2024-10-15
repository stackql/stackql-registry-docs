---
title: managed_clusters_command_results
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters_command_results
  - aks
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

Creates, updates, deletes, gets or lists a <code>managed_clusters_command_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_clusters_command_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.managed_clusters_command_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_clusters_command_results', value: 'view', },
        { label: 'managed_clusters_command_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The command id. |
| <CopyableCode code="commandId" /> | `text` | field from the `properties` object |
| <CopyableCode code="exit_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="finished_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="logs" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="started_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The command id. |
| <CopyableCode code="properties" /> | `object` | The results of a run command |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="commandId, resourceGroupName, resourceName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_clusters_command_results', value: 'view', },
        { label: 'managed_clusters_command_results', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
commandId,
exit_code,
finished_at,
logs,
provisioning_state,
reason,
resourceGroupName,
resourceName,
started_at,
subscriptionId
FROM azure.aks.vw_managed_clusters_command_results
WHERE commandId = '{{ commandId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
properties
FROM azure.aks.managed_clusters_command_results
WHERE commandId = '{{ commandId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

