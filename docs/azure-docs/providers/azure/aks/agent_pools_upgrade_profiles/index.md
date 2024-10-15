---
title: agent_pools_upgrade_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools_upgrade_profiles
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

Creates, updates, deletes, gets or lists a <code>agent_pools_upgrade_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_pools_upgrade_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.agent_pools_upgrade_profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agent_pools_upgrade_profiles', value: 'view', },
        { label: 'agent_pools_upgrade_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the agent pool upgrade profile. |
| <CopyableCode code="name" /> | `text` | The name of the agent pool upgrade profile. |
| <CopyableCode code="agentPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kubernetes_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="latest_node_image_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the agent pool upgrade profile. |
| <CopyableCode code="upgrades" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the agent pool upgrade profile. |
| <CopyableCode code="name" /> | `string` | The name of the agent pool upgrade profile. |
| <CopyableCode code="properties" /> | `object` | The list of available upgrade versions. |
| <CopyableCode code="type" /> | `string` | The type of the agent pool upgrade profile. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentPoolName, resourceGroupName, resourceName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agent_pools_upgrade_profiles', value: 'view', },
        { label: 'agent_pools_upgrade_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
agentPoolName,
kubernetes_version,
latest_node_image_version,
os_type,
resourceGroupName,
resourceName,
subscriptionId,
type,
upgrades
FROM azure.aks.vw_agent_pools_upgrade_profiles
WHERE agentPoolName = '{{ agentPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.aks.agent_pools_upgrade_profiles
WHERE agentPoolName = '{{ agentPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

