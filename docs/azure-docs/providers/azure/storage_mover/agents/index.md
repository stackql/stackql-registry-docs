---
title: agents
hide_title: false
hide_table_of_contents: false
keywords:
  - agents
  - storage_mover
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

Creates, updates, deletes, gets or lists a <code>agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_mover.agents" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agents', value: 'view', },
        { label: 'agents', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="agentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="arc_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="arc_vm_uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_status_update" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="memory_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_cores" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageMoverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="upload_limit_schedule" /> | `text` | field from the `properties` object |
| <CopyableCode code="uptime_in_seconds" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentName, resourceGroupName, storageMoverName, subscriptionId" /> | Gets an Agent resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageMoverName, subscriptionId" /> | Lists all Agents in a Storage Mover. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="agentName, resourceGroupName, storageMoverName, subscriptionId, data__properties" /> | Creates or updates an Agent resource, which references a hybrid compute machine that can run jobs. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agentName, resourceGroupName, storageMoverName, subscriptionId" /> | Deletes an Agent resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="agentName, resourceGroupName, storageMoverName, subscriptionId" /> | Creates or updates an Agent resource. |

## `SELECT` examples

Lists all Agents in a Storage Mover.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agents', value: 'view', },
        { label: 'agents', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
agentName,
agent_status,
agent_version,
arc_resource_id,
arc_vm_uuid,
error_details,
last_status_update,
local_ip_address,
memory_in_mb,
number_of_cores,
provisioning_state,
resourceGroupName,
storageMoverName,
subscriptionId,
system_data,
time_zone,
upload_limit_schedule,
uptime_in_seconds
FROM azure.storage_mover.vw_agents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.storage_mover.agents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>agents</code> resource.

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
INSERT INTO azure.storage_mover.agents (
agentName,
resourceGroupName,
storageMoverName,
subscriptionId,
data__properties,
properties,
systemData
)
SELECT 
'{{ agentName }}',
'{{ resourceGroupName }}',
'{{ storageMoverName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: description
          value: string
        - name: agentVersion
          value: string
        - name: arcResourceId
          value: string
        - name: arcVmUuid
          value: string
        - name: agentStatus
          value: string
        - name: lastStatusUpdate
          value: string
        - name: localIPAddress
          value: string
        - name: memoryInMB
          value: integer
        - name: numberOfCores
          value: integer
        - name: uptimeInSeconds
          value: integer
        - name: timeZone
          value: string
        - name: uploadLimitSchedule
          value:
            - name: weeklyRecurrences
              value:
                - - name: days
                    value:
                      - []
                  - name: limitInMbps
                    value: integer
        - name: errorDetails
          value:
            - name: code
              value: string
            - name: message
              value: string
        - name: provisioningState
          value: []
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>agents</code> resource.

```sql
/*+ update */
UPDATE azure.storage_mover.agents
SET 
properties = '{{ properties }}'
WHERE 
agentName = '{{ agentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>agents</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_mover.agents
WHERE agentName = '{{ agentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
