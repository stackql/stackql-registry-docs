---
title: route_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - route_maps
  - network
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

Creates, updates, deletes, gets or lists a <code>route_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.route_maps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_route_maps', value: 'view', },
        { label: 'route_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="associated_inbound_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="associated_outbound_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routeMapName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtualHubName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of RouteMap resource |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeMapName, subscriptionId, virtualHubName" /> | Retrieves the details of a RouteMap. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all RouteMaps. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, routeMapName, subscriptionId, virtualHubName" /> | Creates a RouteMap if it doesn't exist else updates the existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routeMapName, subscriptionId, virtualHubName" /> | Deletes a RouteMap. |

## `SELECT` examples

Retrieves the details of all RouteMaps.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_route_maps', value: 'view', },
        { label: 'route_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
associated_inbound_connections,
associated_outbound_connections,
etag,
provisioning_state,
resourceGroupName,
routeMapName,
rules,
subscriptionId,
type,
virtualHubName
FROM azure.network.vw_route_maps
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.network.route_maps
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>route_maps</code> resource.

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
INSERT INTO azure.network.route_maps (
resourceGroupName,
routeMapName,
subscriptionId,
virtualHubName,
properties,
id
)
SELECT 
'{{ resourceGroupName }}',
'{{ routeMapName }}',
'{{ subscriptionId }}',
'{{ virtualHubName }}',
'{{ properties }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: associatedInboundConnections
          value:
            - string
        - name: associatedOutboundConnections
          value:
            - string
        - name: rules
          value:
            - - name: name
                value: string
              - name: matchCriteria
                value:
                  - - name: routePrefix
                      value:
                        - string
                    - name: community
                      value:
                        - string
                    - name: asPath
                      value:
                        - string
                    - name: matchCondition
                      value: []
              - name: actions
                value:
                  - - name: type
                      value: []
                    - name: parameters
                      value:
                        - - name: routePrefix
                            value:
                              - string
                          - name: community
                            value:
                              - string
                          - name: asPath
                            value:
                              - string
              - name: nextStepIfMatched
                value: []
        - name: provisioningState
          value: []
    - name: name
      value: string
    - name: etag
      value: string
    - name: type
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>route_maps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.route_maps
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routeMapName = '{{ routeMapName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
