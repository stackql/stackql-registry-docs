---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - traffic_manager
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

Creates, updates, deletes, gets or lists a <code>endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.traffic_manager.endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_endpoints', value: 'view', },
        { label: 'endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="always_serve" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_headers" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointType" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint_monitor_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="geo_mapping" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_child_endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_child_endpoints_ipv4" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_child_endpoints_ipv6" /> | `text` | field from the `properties` object |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnets" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="weight" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class representing a Traffic Manager endpoint properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, endpointType, profileName, resourceGroupName, subscriptionId" /> | Gets a Traffic Manager endpoint. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="endpointName, endpointType, profileName, resourceGroupName, subscriptionId" /> | Create or update a Traffic Manager endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, endpointType, profileName, resourceGroupName, subscriptionId" /> | Deletes a Traffic Manager endpoint. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="endpointName, endpointType, profileName, resourceGroupName, subscriptionId" /> | Update a Traffic Manager endpoint. |

## `SELECT` examples

Gets a Traffic Manager endpoint.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_endpoints', value: 'view', },
        { label: 'endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
always_serve,
custom_headers,
endpointName,
endpointType,
endpoint_location,
endpoint_monitor_status,
endpoint_status,
geo_mapping,
min_child_endpoints,
min_child_endpoints_ipv4,
min_child_endpoints_ipv6,
priority,
profileName,
resourceGroupName,
subnets,
subscriptionId,
target,
target_resource_id,
weight
FROM azure.traffic_manager.vw_endpoints
WHERE endpointName = '{{ endpointName }}'
AND endpointType = '{{ endpointType }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.traffic_manager.endpoints
WHERE endpointName = '{{ endpointName }}'
AND endpointType = '{{ endpointType }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoints</code> resource.

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
INSERT INTO azure.traffic_manager.endpoints (
endpointName,
endpointType,
profileName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ endpointName }}',
'{{ endpointType }}',
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
        - name: targetResourceId
          value: string
        - name: target
          value: string
        - name: endpointStatus
          value: string
        - name: weight
          value: integer
        - name: priority
          value: integer
        - name: endpointLocation
          value: string
        - name: endpointMonitorStatus
          value: string
        - name: minChildEndpoints
          value: integer
        - name: minChildEndpointsIPv4
          value: integer
        - name: minChildEndpointsIPv6
          value: integer
        - name: geoMapping
          value:
            - string
        - name: subnets
          value:
            - - name: first
                value: string
              - name: last
                value: string
              - name: scope
                value: integer
        - name: customHeaders
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: alwaysServe
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>endpoints</code> resource.

```sql
/*+ update */
UPDATE azure.traffic_manager.endpoints
SET 
properties = '{{ properties }}'
WHERE 
endpointName = '{{ endpointName }}'
AND endpointType = '{{ endpointType }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.traffic_manager.endpoints
WHERE endpointName = '{{ endpointName }}'
AND endpointType = '{{ endpointType }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
