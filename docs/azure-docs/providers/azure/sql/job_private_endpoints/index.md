---
title: job_private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - job_private_endpoints
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

Creates, updates, deletes, gets or lists a <code>job_private_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.job_private_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_private_endpoints', value: 'view', },
        { label: 'job_private_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="jobAgentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_server_azure_resource_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of job agent private endpoint. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobAgentName, privateEndpointName, resourceGroupName, serverName, subscriptionId" /> | Gets a private endpoint. |
| <CopyableCode code="list_by_agent" /> | `SELECT` | <CopyableCode code="jobAgentName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of job agent private endpoints. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobAgentName, privateEndpointName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a private endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobAgentName, privateEndpointName, resourceGroupName, serverName, subscriptionId" /> | Deletes a private endpoint. |

## `SELECT` examples

Gets a list of job agent private endpoints.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_private_endpoints', value: 'view', },
        { label: 'job_private_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
jobAgentName,
privateEndpointName,
private_endpoint_id,
resourceGroupName,
serverName,
subscriptionId,
target_server_azure_resource_id
FROM azure.sql.vw_job_private_endpoints
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
FROM azure.sql.job_private_endpoints
WHERE jobAgentName = '{{ jobAgentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_private_endpoints</code> resource.

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
INSERT INTO azure.sql.job_private_endpoints (
jobAgentName,
privateEndpointName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ jobAgentName }}',
'{{ privateEndpointName }}',
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
        - name: targetServerAzureResourceId
          value: string
        - name: privateEndpointId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>job_private_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.job_private_endpoints
WHERE jobAgentName = '{{ jobAgentName }}'
AND privateEndpointName = '{{ privateEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
