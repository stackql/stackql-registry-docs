---
title: network_fabric_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabric_skus
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>network_fabric_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_fabric_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_fabric_skus" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_fabric_skus', value: 'view', },
        { label: 'network_fabric_skus', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_compute_racks" /> | `text` | field from the `properties` object |
| <CopyableCode code="maximum_server_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkFabricSkuName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_versions" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Network Fabric SKU Properties define properties of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFabricSkuName, subscriptionId" /> | Implements Network Fabric SKU GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Implements Network Fabric SKUs list by subscription GET method. |

## `SELECT` examples

Implements Network Fabric SKUs list by subscription GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_fabric_skus', value: 'view', },
        { label: 'network_fabric_skus', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
details,
max_compute_racks,
maximum_server_count,
networkFabricSkuName,
provisioning_state,
subscriptionId,
supported_versions,
type
FROM azure.managed_network_fabric.vw_network_fabric_skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.managed_network_fabric.network_fabric_skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

