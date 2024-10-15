---
title: private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoints
  - stream_analytics
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

Creates, updates, deletes, gets or lists a <code>private_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.private_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_endpoints', value: 'view', },
        { label: 'private_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Unique opaque string (generally a GUID) that represents the metadata state of the resource (private endpoint) and changes whenever the resource is updated. Required on PUT (CreateOrUpdate) requests. |
| <CopyableCode code="manual_private_link_service_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="privateEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Unique opaque string (generally a GUID) that represents the metadata state of the resource (private endpoint) and changes whenever the resource is updated. Required on PUT (CreateOrUpdate) requests. |
| <CopyableCode code="properties" /> | `object` | The properties associated with a private endpoint. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, privateEndpointName, resourceGroupName, subscriptionId" /> | Gets information about the specified Private Endpoint. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Lists the private endpoints in the cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, privateEndpointName, resourceGroupName, subscriptionId" /> | Creates a Stream Analytics Private Endpoint or replaces an already existing Private Endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, privateEndpointName, resourceGroupName, subscriptionId" /> | Delete the specified private endpoint. |

## `SELECT` examples

Lists the private endpoints in the cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_endpoints', value: 'view', },
        { label: 'private_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterName,
created_date,
etag,
manual_private_link_service_connections,
privateEndpointName,
resourceGroupName,
subscriptionId
FROM azure.stream_analytics.vw_private_endpoints
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.stream_analytics.private_endpoints
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_endpoints</code> resource.

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
INSERT INTO azure.stream_analytics.private_endpoints (
clusterName,
privateEndpointName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ clusterName }}',
'{{ privateEndpointName }}',
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
        - name: createdDate
          value: string
        - name: manualPrivateLinkServiceConnections
          value:
            - - name: properties
                value:
                  - name: privateLinkServiceId
                    value: string
                  - name: groupIds
                    value:
                      - string
                  - name: requestMessage
                    value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: string
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>private_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.stream_analytics.private_endpoints
WHERE clusterName = '{{ clusterName }}'
AND privateEndpointName = '{{ privateEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
