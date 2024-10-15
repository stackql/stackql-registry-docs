---
title: tenant_configuration_sync_states
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_configuration_sync_states
  - api_management
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

Creates, updates, deletes, gets or lists a <code>tenant_configuration_sync_states</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_configuration_sync_states</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tenant_configuration_sync_states" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tenant_configuration_sync_states', value: 'view', },
        { label: 'tenant_configuration_sync_states', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="branch" /> | `text` | field from the `properties` object |
| <CopyableCode code="commit_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_change_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_export" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_git_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_synced" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_operation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_date" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Tenant Configuration Synchronization State. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName, resourceGroupName, serviceName, subscriptionId" /> | Gets the status of the most recent synchronization between the configuration database and the Git repository. |

## `SELECT` examples

Gets the status of the most recent synchronization between the configuration database and the Git repository.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tenant_configuration_sync_states', value: 'view', },
        { label: 'tenant_configuration_sync_states', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
branch,
commit_id,
configurationName,
configuration_change_date,
is_export,
is_git_enabled,
is_synced,
last_operation_id,
resourceGroupName,
serviceName,
subscriptionId,
sync_date
FROM azure.api_management.vw_tenant_configuration_sync_states
WHERE configurationName = '{{ configurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.tenant_configuration_sync_states
WHERE configurationName = '{{ configurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

