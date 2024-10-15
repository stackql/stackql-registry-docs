---
title: network_device_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - network_device_skus
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

Creates, updates, deletes, gets or lists a <code>network_device_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_device_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_device_skus" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_device_skus', value: 'view', },
        { label: 'network_device_skus', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="interfaces" /> | `text` | field from the `properties` object |
| <CopyableCode code="manufacturer" /> | `text` | field from the `properties` object |
| <CopyableCode code="model" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkDeviceSkuName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_role_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_versions" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Network Device SKU Properties defines the properties of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkDeviceSkuName, subscriptionId" /> | Get a Network Device SKU details. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Network Device SKUs for the given subscription. |

## `SELECT` examples

List Network Device SKUs for the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_device_skus', value: 'view', },
        { label: 'network_device_skus', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
interfaces,
manufacturer,
model,
networkDeviceSkuName,
provisioning_state,
subscriptionId,
supported_role_types,
supported_versions
FROM azure.managed_network_fabric.vw_network_device_skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.managed_network_fabric.network_device_skus
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

