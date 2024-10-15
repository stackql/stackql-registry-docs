---
title: managed_unsupported_vm_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_unsupported_vm_sizes
  - service_fabric_managed_clusters
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

Creates, updates, deletes, gets or lists a <code>managed_unsupported_vm_sizes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_unsupported_vm_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.managed_unsupported_vm_sizes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_unsupported_vm_sizes', value: 'view', },
        { label: 'managed_unsupported_vm_sizes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | VM Size id. |
| <CopyableCode code="name" /> | `text` | VM Size name. |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="size" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | VM Size type. |
| <CopyableCode code="vmSize" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | VM Size id. |
| <CopyableCode code="name" /> | `string` | VM Size name. |
| <CopyableCode code="properties" /> | `object` | VM Sizes properties. |
| <CopyableCode code="type" /> | `string` | VM Size type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId, vmSize" /> | Get unsupported vm size for Service Fabric Managed Clusters. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get the lists of unsupported vm sizes for Service Fabric Managed Clusters. |

## `SELECT` examples

Get the lists of unsupported vm sizes for Service Fabric Managed Clusters.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_unsupported_vm_sizes', value: 'view', },
        { label: 'managed_unsupported_vm_sizes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
location,
size,
subscriptionId,
type,
vmSize
FROM azure.service_fabric_managed_clusters.vw_managed_unsupported_vm_sizes
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.service_fabric_managed_clusters.managed_unsupported_vm_sizes
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

