---
title: plans_vnet_from_server_farms
hide_title: false
hide_table_of_contents: false
keywords:
  - plans_vnet_from_server_farms
  - app_service
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

Creates, updates, deletes, gets or lists a <code>plans_vnet_from_server_farms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plans_vnet_from_server_farms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.plans_vnet_from_server_farms" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_plans_vnet_from_server_farms', value: 'view', },
        { label: 'plans_vnet_from_server_farms', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource Name. |
| <CopyableCode code="cert_blob" /> | `text` | field from the `properties` object |
| <CopyableCode code="cert_thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_servers" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_swift" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of resource. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resync_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="routes" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="vnetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_resource_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Virtual Network information contract. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, vnetName" /> | Description for Get a Virtual Network associated with an App Service plan. |

## `SELECT` examples

Description for Get a Virtual Network associated with an App Service plan.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_plans_vnet_from_server_farms', value: 'view', },
        { label: 'plans_vnet_from_server_farms', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cert_blob,
cert_thumbprint,
dns_servers,
is_swift,
kind,
resourceGroupName,
resync_required,
routes,
subscriptionId,
type,
vnetName,
vnet_resource_id
FROM azure.app_service.vw_plans_vnet_from_server_farms
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vnetName = '{{ vnetName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.plans_vnet_from_server_farms
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vnetName = '{{ vnetName }}';
```
</TabItem></Tabs>

