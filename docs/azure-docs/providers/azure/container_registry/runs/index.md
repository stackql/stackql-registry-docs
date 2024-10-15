---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.runs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_runs', value: 'view', },
        { label: 'runs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agent_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_pool_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_registries" /> | `text` | field from the `properties` object |
| <CopyableCode code="finish_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_update_trigger" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_archive_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_artifact" /> | `text` | field from the `properties` object |
| <CopyableCode code="output_images" /> | `text` | field from the `properties` object |
| <CopyableCode code="platform" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runId" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_error_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_registry_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_trigger" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="task" /> | `text` | field from the `properties` object |
| <CopyableCode code="timer_trigger" /> | `text` | field from the `properties` object |
| <CopyableCode code="update_trigger_token" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties for a run. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, runId, subscriptionId" /> | Gets the detailed information for a given run. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Gets all the runs for a registry. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="registryName, resourceGroupName, runId, subscriptionId" /> | Patch the run properties. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, runId, subscriptionId" /> | Cancel an existing run. |

## `SELECT` examples

Gets all the runs for a registry.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_runs', value: 'view', },
        { label: 'runs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
agent_configuration,
agent_pool_name,
create_time,
custom_registries,
finish_time,
image_update_trigger,
is_archive_enabled,
last_updated_time,
log_artifact,
output_images,
platform,
provisioning_state,
registryName,
resourceGroupName,
runId,
run_error_message,
run_id,
run_type,
source_registry_auth,
source_trigger,
start_time,
status,
subscriptionId,
task,
timer_trigger,
update_trigger_token
FROM azure.container_registry.vw_runs
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_registry.runs
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>runs</code> resource.

```sql
/*+ update */
UPDATE azure.container_registry.runs
SET 
isArchiveEnabled = true|false
WHERE 
registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runId = '{{ runId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
