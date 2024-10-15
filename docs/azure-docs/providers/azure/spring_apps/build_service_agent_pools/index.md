---
title: build_service_agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_agent_pools
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>build_service_agent_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>build_service_agent_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.build_service_agent_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_build_service_agent_pools', value: 'view', },
        { label: 'build_service_agent_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agentPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="buildServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="pool_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Build service agent pool properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentPoolName, buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | Get build service agent pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | List build service agent pool. |
| <CopyableCode code="update_put" /> | `EXEC` | <CopyableCode code="agentPoolName, buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | Create or update build service agent pool. |

## `SELECT` examples

List build service agent pool.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_build_service_agent_pools', value: 'view', },
        { label: 'build_service_agent_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
agentPoolName,
buildServiceName,
pool_size,
provisioning_state,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.spring_apps.vw_build_service_agent_pools
WHERE buildServiceName = '{{ buildServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.build_service_agent_pools
WHERE buildServiceName = '{{ buildServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

