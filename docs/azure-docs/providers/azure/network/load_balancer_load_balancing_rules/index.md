---
title: load_balancer_load_balancing_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_load_balancing_rules
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

Creates, updates, deletes, gets or lists a <code>load_balancer_load_balancing_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer_load_balancing_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_load_balancing_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_balancer_load_balancing_rules', value: 'view', },
        { label: 'load_balancer_load_balancing_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within the set of load balancing rules used by the load balancer. This name can be used to access the resource. |
| <CopyableCode code="backend_address_pool" /> | `text` | field from the `properties` object |
| <CopyableCode code="backend_address_pools" /> | `text` | field from the `properties` object |
| <CopyableCode code="backend_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_outbound_snat" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_floating_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_tcp_reset" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="frontend_ip_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="frontend_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="idle_timeout_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="loadBalancerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="loadBalancingRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_distribution" /> | `text` | field from the `properties` object |
| <CopyableCode code="probe" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within the set of load balancing rules used by the load balancer. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the load balancer. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="loadBalancerName, loadBalancingRuleName, resourceGroupName, subscriptionId" /> | Gets the specified load balancer load balancing rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Gets all the load balancing rules in a load balancer. |

## `SELECT` examples

Gets all the load balancing rules in a load balancer.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_balancer_load_balancing_rules', value: 'view', },
        { label: 'load_balancer_load_balancing_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backend_address_pool,
backend_address_pools,
backend_port,
disable_outbound_snat,
enable_floating_ip,
enable_tcp_reset,
etag,
frontend_ip_configuration,
frontend_port,
idle_timeout_in_minutes,
loadBalancerName,
loadBalancingRuleName,
load_distribution,
probe,
protocol,
provisioning_state,
resourceGroupName,
subscriptionId,
type
FROM azure.network.vw_load_balancer_load_balancing_rules
WHERE loadBalancerName = '{{ loadBalancerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.network.load_balancer_load_balancing_rules
WHERE loadBalancerName = '{{ loadBalancerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

