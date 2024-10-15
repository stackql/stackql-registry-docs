---
title: job_target_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - job_target_groups
  - sql
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

Creates, updates, deletes, gets or lists a <code>job_target_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_target_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_target_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_target_groups', value: 'view', },
        { label: 'job_target_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="jobAgentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="members" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="targetGroupName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of job target group. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId, targetGroupName" /> | Gets a target group. |
| <CopyableCode code="list_by_agent" /> | `SELECT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Gets all target groups in an agent. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId, targetGroupName" /> | Creates or updates a target group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId, targetGroupName" /> | Deletes a target group. |

## `SELECT` examples

Gets all target groups in an agent.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_target_groups', value: 'view', },
        { label: 'job_target_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
jobAgentName,
members,
resourceGroupName,
serverName,
subscriptionId,
targetGroupName
FROM azure.sql.vw_job_target_groups
WHERE jobAgentName = '{{ jobAgentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.job_target_groups
WHERE jobAgentName = '{{ jobAgentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_target_groups</code> resource.

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
INSERT INTO azure.sql.job_target_groups (
jobAgentName,
resourceGroupName,
serverName,
subscriptionId,
targetGroupName,
properties
)
SELECT 
'{{ jobAgentName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ targetGroupName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: members
          value:
            - - name: membershipType
                value: string
              - name: type
                value: string
              - name: serverName
                value: string
              - name: databaseName
                value: string
              - name: elasticPoolName
                value: string
              - name: shardMapName
                value: string
              - name: refreshCredential
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>job_target_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.job_target_groups
WHERE jobAgentName = '{{ jobAgentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND targetGroupName = '{{ targetGroupName }}';
```
