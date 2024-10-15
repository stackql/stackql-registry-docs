---
title: job_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - job_credentials
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

Creates, updates, deletes, gets or lists a <code>job_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_credentials" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_credentials', value: 'view', },
        { label: 'job_credentials', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="credentialName" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobAgentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="password" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="username" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a job credential. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Gets a jobs credential. |
| <CopyableCode code="list_by_agent" /> | `SELECT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of jobs credentials. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a job credential. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Deletes a job credential. |

## `SELECT` examples

Gets a list of jobs credentials.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_credentials', value: 'view', },
        { label: 'job_credentials', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
credentialName,
jobAgentName,
password,
resourceGroupName,
serverName,
subscriptionId,
username
FROM azure.sql.vw_job_credentials
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
FROM azure.sql.job_credentials
WHERE jobAgentName = '{{ jobAgentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_credentials</code> resource.

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
INSERT INTO azure.sql.job_credentials (
credentialName,
jobAgentName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ credentialName }}',
'{{ jobAgentName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
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
        - name: username
          value: string
        - name: password
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>job_credentials</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.job_credentials
WHERE credentialName = '{{ credentialName }}'
AND jobAgentName = '{{ jobAgentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
