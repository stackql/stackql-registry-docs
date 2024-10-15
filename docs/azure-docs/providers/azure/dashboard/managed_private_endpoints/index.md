---
title: managed_private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_private_endpoints
  - dashboard
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

Creates, updates, deletes, gets or lists a <code>managed_private_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dashboard.managed_private_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_private_endpoints', value: 'view', },
        { label: 'managed_private_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managedPrivateEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_resource_region" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_private_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_service_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties specific to the managed private endpoint. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="refresh" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_private_endpoints', value: 'view', },
        { label: 'managed_private_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
connection_state,
group_ids,
location,
managedPrivateEndpointName,
private_link_resource_id,
private_link_resource_region,
private_link_service_private_ip,
private_link_service_url,
provisioning_state,
request_message,
resourceGroupName,
subscriptionId,
tags,
workspaceName
FROM azure.dashboard.vw_managed_private_endpoints
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.dashboard.managed_private_endpoints
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_private_endpoints</code> resource.

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
INSERT INTO azure.dashboard.managed_private_endpoints (
managedPrivateEndpointName,
resourceGroupName,
subscriptionId,
workspaceName,
tags,
location,
properties
)
SELECT 
'{{ managedPrivateEndpointName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: privateLinkResourceId
          value: string
        - name: privateLinkResourceRegion
          value: string
        - name: groupIds
          value:
            - string
        - name: requestMessage
          value: string
        - name: connectionState
          value:
            - name: status
              value: []
            - name: description
              value: string
        - name: privateLinkServiceUrl
          value: string
        - name: privateLinkServicePrivateIP
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>managed_private_endpoints</code> resource.

```sql
/*+ update */
UPDATE azure.dashboard.managed_private_endpoints
SET 
tags = '{{ tags }}'
WHERE 
managedPrivateEndpointName = '{{ managedPrivateEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>managed_private_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dashboard.managed_private_endpoints
WHERE managedPrivateEndpointName = '{{ managedPrivateEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
