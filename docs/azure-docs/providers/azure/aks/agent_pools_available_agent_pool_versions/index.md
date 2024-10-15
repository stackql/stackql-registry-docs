---
title: agent_pools_available_agent_pool_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools_available_agent_pool_versions
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

Creates, updates, deletes, gets or lists a <code>agent_pools_available_agent_pool_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_pools_available_agent_pool_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.agent_pools_available_agent_pool_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agent_pools_available_agent_pool_versions', value: 'view', },
        { label: 'agent_pools_available_agent_pool_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the agent pool version list. |
| <CopyableCode code="name" /> | `text` | The name of the agent pool version list. |
| <CopyableCode code="agent_pool_versions" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the agent pool version list. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the agent pool version list. |
| <CopyableCode code="name" /> | `string` | The name of the agent pool version list. |
| <CopyableCode code="properties" /> | `object` | The list of available agent pool versions. |
| <CopyableCode code="type" /> | `string` | Type of the agent pool version list. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | See [supported Kubernetes versions](https://docs.microsoft.com/azure/aks/supported-kubernetes-versions) for more details about the version lifecycle. |

## `SELECT` examples

See [supported Kubernetes versions](https://docs.microsoft.com/azure/aks/supported-kubernetes-versions) for more details about the version lifecycle.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agent_pools_available_agent_pool_versions', value: 'view', },
        { label: 'agent_pools_available_agent_pool_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
agent_pool_versions,
resourceGroupName,
resourceName,
subscriptionId,
type
FROM azure.aks.vw_agent_pools_available_agent_pool_versions
WHERE resourceGroupName = '{{ resourceGroupName }}'
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
FROM azure.aks.agent_pools_available_agent_pool_versions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

