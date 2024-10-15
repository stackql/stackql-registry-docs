---
title: interface_ip_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - interface_ip_configurations
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

Creates, updates, deletes, gets or lists a <code>interface_ip_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>interface_ip_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.interface_ip_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_interface_ip_configurations', value: 'view', },
        { label: 'interface_ip_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="application_gateway_backend_address_pools" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_security_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="gateway_load_balancer" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancer_backend_address_pools" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancer_inbound_nat_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkInterfaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_ip_address_prefix_length" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_ip_address_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_ip_allocation_method" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_connection_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_network_taps" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of IP configuration. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ipConfigurationName, networkInterfaceName, resourceGroupName, subscriptionId" /> | Gets the specified network interface ip configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> | Get all ip configurations in a network interface. |

## `SELECT` examples

Get all ip configurations in a network interface.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_interface_ip_configurations', value: 'view', },
        { label: 'interface_ip_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
application_gateway_backend_address_pools,
application_security_groups,
etag,
gateway_load_balancer,
ipConfigurationName,
load_balancer_backend_address_pools,
load_balancer_inbound_nat_rules,
networkInterfaceName,
primary,
private_ip_address,
private_ip_address_prefix_length,
private_ip_address_version,
private_ip_allocation_method,
private_link_connection_properties,
provisioning_state,
public_ip_address,
resourceGroupName,
subnet,
subscriptionId,
type,
virtual_network_taps
FROM azure.network.vw_interface_ip_configurations
WHERE networkInterfaceName = '{{ networkInterfaceName }}'
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
FROM azure.network.interface_ip_configurations
WHERE networkInterfaceName = '{{ networkInterfaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

