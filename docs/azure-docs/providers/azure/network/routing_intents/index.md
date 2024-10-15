---
title: routing_intents
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_intents
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

Creates, updates, deletes, gets or lists a <code>routing_intents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routing_intents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.routing_intents" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_routing_intents', value: 'view', },
        { label: 'routing_intents', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routingIntentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_policies" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | The properties of a RoutingIntent resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routingIntentName, subscriptionId, virtualHubName" /> | Retrieves the details of a RoutingIntent. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all RoutingIntent child resources of the VirtualHub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, routingIntentName, subscriptionId, virtualHubName" /> | Creates a RoutingIntent resource if it doesn't exist else updates the existing RoutingIntent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routingIntentName, subscriptionId, virtualHubName" /> | Deletes a RoutingIntent. |

## `SELECT` examples

Retrieves the details of all RoutingIntent child resources of the VirtualHub.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_routing_intents', value: 'view', },
        { label: 'routing_intents', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
provisioning_state,
resourceGroupName,
routingIntentName,
routing_policies,
subscriptionId,
type,
virtualHubName
FROM azure.network.vw_routing_intents
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
FROM azure.network.routing_intents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>routing_intents</code> resource.

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
INSERT INTO azure.network.routing_intents (
resourceGroupName,
routingIntentName,
subscriptionId,
virtualHubName,
properties,
name,
id
)
SELECT 
'{{ resourceGroupName }}',
'{{ routingIntentName }}',
'{{ subscriptionId }}',
'{{ virtualHubName }}',
'{{ properties }}',
'{{ name }}',
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
        - name: routingPolicies
          value:
            - - name: name
                value: string
              - name: destinations
                value:
                  - string
              - name: nextHop
                value: string
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

Deletes the specified <code>routing_intents</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.routing_intents
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routingIntentName = '{{ routingIntentName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```
