---
title: load_balancer_probes
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_probes
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

Creates, updates, deletes, gets or lists a <code>load_balancer_probes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer_probes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_probes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_balancer_probes', value: 'view', },
        { label: 'load_balancer_probes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within the set of probes used by the load balancer. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="interval_in_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="loadBalancerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancing_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="no_healthy_backends_behavior" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_probes" /> | `text` | field from the `properties` object |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="probeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="probe_threshold" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within the set of probes used by the load balancer. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Load balancer probe resource. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="loadBalancerName, probeName, resourceGroupName, subscriptionId" /> | Gets load balancer probe. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Gets all the load balancer probes. |

## `SELECT` examples

Gets all the load balancer probes.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_balancer_probes', value: 'view', },
        { label: 'load_balancer_probes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
interval_in_seconds,
loadBalancerName,
load_balancing_rules,
no_healthy_backends_behavior,
number_of_probes,
port,
probeName,
probe_threshold,
protocol,
provisioning_state,
request_path,
resourceGroupName,
subscriptionId,
type
FROM azure.network.vw_load_balancer_probes
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
FROM azure.network.load_balancer_probes
WHERE loadBalancerName = '{{ loadBalancerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

