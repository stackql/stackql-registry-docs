---
title: load_balancer_frontend_ip_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_frontend_ip_configurations
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

Creates, updates, deletes, gets or lists a <code>load_balancer_frontend_ip_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer_frontend_ip_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_frontend_ip_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_balancer_frontend_ip_configurations', value: 'view', },
        { label: 'load_balancer_frontend_ip_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within the set of frontend IP configurations used by the load balancer. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="frontendIPConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_load_balancer" /> | `text` | field from the `properties` object |
| <CopyableCode code="inbound_nat_pools" /> | `text` | field from the `properties` object |
| <CopyableCode code="inbound_nat_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="loadBalancerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancing_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="outbound_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_ip_address_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_ip_allocation_method" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource. |
| <CopyableCode code="zones" /> | `text` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within the set of frontend IP configurations used by the load balancer. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of Frontend IP Configuration of the load balancer. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="frontendIPConfigurationName, loadBalancerName, resourceGroupName, subscriptionId" /> | Gets load balancer frontend IP configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Gets all the load balancer frontend IP configurations. |

## `SELECT` examples

Gets all the load balancer frontend IP configurations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_balancer_frontend_ip_configurations', value: 'view', },
        { label: 'load_balancer_frontend_ip_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
frontendIPConfigurationName,
gateway_load_balancer,
inbound_nat_pools,
inbound_nat_rules,
loadBalancerName,
load_balancing_rules,
outbound_rules,
private_ip_address,
private_ip_address_version,
private_ip_allocation_method,
provisioning_state,
public_ip_address,
public_ip_prefix,
resourceGroupName,
subnet,
subscriptionId,
type,
zones
FROM azure.network.vw_load_balancer_frontend_ip_configurations
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
type,
zones
FROM azure.network.load_balancer_frontend_ip_configurations
WHERE loadBalancerName = '{{ loadBalancerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

