---
title: route_filter_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - route_filter_rules
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

Creates, updates, deletes, gets or lists a <code>route_filter_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_filter_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.route_filter_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_route_filter_rules', value: 'view', },
        { label: 'route_filter_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="access" /> | `text` | field from the `properties` object |
| <CopyableCode code="communities" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routeFilterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="route_filter_rule_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Route Filter Rule Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeFilterName, ruleName, subscriptionId" /> | Gets the specified rule from a route filter. |
| <CopyableCode code="list_by_route_filter" /> | `SELECT` | <CopyableCode code="resourceGroupName, routeFilterName, subscriptionId" /> | Gets all RouteFilterRules in a route filter. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, routeFilterName, ruleName, subscriptionId" /> | Creates or updates a route in the specified route filter. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routeFilterName, ruleName, subscriptionId" /> | Deletes the specified rule from a route filter. |

## `SELECT` examples

Gets all RouteFilterRules in a route filter.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_route_filter_rules', value: 'view', },
        { label: 'route_filter_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
access,
communities,
etag,
location,
provisioning_state,
resourceGroupName,
routeFilterName,
route_filter_rule_type,
ruleName,
subscriptionId
FROM azure.network.vw_route_filter_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routeFilterName = '{{ routeFilterName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties
FROM azure.network.route_filter_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routeFilterName = '{{ routeFilterName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>route_filter_rules</code> resource.

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
INSERT INTO azure.network.route_filter_rules (
resourceGroupName,
routeFilterName,
ruleName,
subscriptionId,
properties,
name,
location,
id
)
SELECT 
'{{ resourceGroupName }}',
'{{ routeFilterName }}',
'{{ ruleName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ name }}',
'{{ location }}',
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
        - name: access
          value: []
        - name: routeFilterRuleType
          value: string
        - name: communities
          value:
            - string
        - name: provisioningState
          value: []
    - name: name
      value: string
    - name: location
      value: string
    - name: etag
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>route_filter_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.route_filter_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND routeFilterName = '{{ routeFilterName }}'
AND ruleName = '{{ ruleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
