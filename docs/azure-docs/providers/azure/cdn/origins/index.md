---
title: origins
hide_title: false
hide_table_of_contents: false
keywords:
  - origins
  - cdn
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

Creates, updates, deletes, gets or lists a <code>origins</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.origins" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_origins', value: 'view', },
        { label: 'origins', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="http_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="https_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="originName" /> | `text` | field from the `properties` object |
| <CopyableCode code="origin_host_header" /> | `text` | field from the `properties` object |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_alias" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_approval_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="weight" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties of the origin. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, originName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing origin within an endpoint. |
| <CopyableCode code="list_by_endpoint" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origins within an endpoint. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="endpointName, originName, profileName, resourceGroupName, subscriptionId" /> | Creates a new origin within the specified endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, originName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing origin within an endpoint. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="endpointName, originName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing origin within an endpoint. |

## `SELECT` examples

Lists all of the existing origins within an endpoint.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_origins', value: 'view', },
        { label: 'origins', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
enabled,
endpointName,
host_name,
http_port,
https_port,
originName,
origin_host_header,
priority,
private_endpoint_status,
private_link_alias,
private_link_approval_message,
private_link_location,
private_link_resource_id,
profileName,
provisioning_state,
resourceGroupName,
resource_state,
subscriptionId,
weight
FROM azure.cdn.vw_origins
WHERE endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cdn.origins
WHERE endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>origins</code> resource.

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
INSERT INTO azure.cdn.origins (
endpointName,
originName,
profileName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ endpointName }}',
'{{ originName }}',
'{{ profileName }}',
'{{ resourceGroupName }}',
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
        - name: hostName
          value: string
        - name: httpPort
          value: integer
        - name: httpsPort
          value: integer
        - name: originHostHeader
          value: string
        - name: priority
          value: integer
        - name: weight
          value: integer
        - name: enabled
          value: boolean
        - name: privateLinkAlias
          value: string
        - name: privateLinkResourceId
          value: string
        - name: privateLinkLocation
          value: string
        - name: privateLinkApprovalMessage
          value: string
        - name: resourceState
          value: string
        - name: provisioningState
          value: string
        - name: privateEndpointStatus
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>origins</code> resource.

```sql
/*+ update */
UPDATE azure.cdn.origins
SET 
properties = '{{ properties }}'
WHERE 
endpointName = '{{ endpointName }}'
AND originName = '{{ originName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>origins</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.origins
WHERE endpointName = '{{ endpointName }}'
AND originName = '{{ originName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
