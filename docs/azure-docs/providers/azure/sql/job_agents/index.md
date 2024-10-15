---
title: job_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - job_agents
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

Creates, updates, deletes, gets or lists a <code>job_agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_agents" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_agents', value: 'view', },
        { label: 'job_agents', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="database_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobAgentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | An ARM Resource SKU. |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of a job agent. |
| <CopyableCode code="sku" /> | `object` | An ARM Resource SKU. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Gets a job agent. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of job agents in a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId, data__location" /> | Creates or updates a job agent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Deletes a job agent. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Updates a job agent. |

## `SELECT` examples

Gets a list of job agents in a server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_agents', value: 'view', },
        { label: 'job_agents', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
database_id,
jobAgentName,
location,
resourceGroupName,
serverName,
sku,
state,
subscriptionId,
tags
FROM azure.sql.vw_job_agents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure.sql.job_agents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_agents</code> resource.

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
INSERT INTO azure.sql.job_agents (
jobAgentName,
resourceGroupName,
serverName,
subscriptionId,
data__location,
location,
tags,
sku,
properties
)
SELECT 
'{{ jobAgentName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: properties
      value:
        - name: databaseId
          value: string
        - name: state
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>job_agents</code> resource.

```sql
/*+ update */
UPDATE azure.sql.job_agents
SET 
tags = '{{ tags }}'
WHERE 
jobAgentName = '{{ jobAgentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>job_agents</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.job_agents
WHERE jobAgentName = '{{ jobAgentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
