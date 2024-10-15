---
title: resource_provider_states
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_provider_states
  - network_admin
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

Creates, updates, deletes, gets or lists a <code>resource_provider_states</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_provider_states</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.network_admin.resource_provider_states" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_provider_states', value: 'view', },
        { label: 'resource_provider_states', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="backend_ip_usage" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancer_mux_health" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Region location of resource. |
| <CopyableCode code="mac_address_usage" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_address_usage" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
| <CopyableCode code="virtual_gateway_health" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_network_health" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Region location of resource. |
| <CopyableCode code="properties" /> | `object` | Admin overview properties. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get an overview of the state of the network resource provider. |

## `SELECT` examples

Get an overview of the state of the network resource provider.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_provider_states', value: 'view', },
        { label: 'resource_provider_states', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backend_ip_usage,
load_balancer_mux_health,
location,
mac_address_usage,
provisioning_state,
public_ip_address_usage,
subscriptionId,
tags,
type,
virtual_gateway_health,
virtual_network_health
FROM azure_stack.network_admin.vw_resource_provider_states
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_stack.network_admin.resource_provider_states
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

