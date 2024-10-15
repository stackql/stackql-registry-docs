---
title: express_route_links
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_links
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

Creates, updates, deletes, gets or lists a <code>express_route_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_links" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_links', value: 'view', },
        { label: 'express_route_links', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Name of child port resource that is unique among child port resources of the parent. |
| <CopyableCode code="admin_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="colo_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="connector_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="expressRoutePortName" /> | `text` | field from the `properties` object |
| <CopyableCode code="interface_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="linkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="mac_sec_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="patch_panel_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="rack_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="router_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of child port resource that is unique among child port resources of the parent. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties specific to ExpressRouteLink resources. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="expressRoutePortName, linkName, resourceGroupName, subscriptionId" /> | Retrieves the specified ExpressRouteLink resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId" /> | Retrieve the ExpressRouteLink sub-resources of the specified ExpressRoutePort resource. |

## `SELECT` examples

Retrieve the ExpressRouteLink sub-resources of the specified ExpressRoutePort resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_links', value: 'view', },
        { label: 'express_route_links', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
admin_state,
colo_location,
connector_type,
etag,
expressRoutePortName,
interface_name,
linkName,
mac_sec_config,
patch_panel_id,
provisioning_state,
rack_id,
resourceGroupName,
router_name,
subscriptionId
FROM azure.network.vw_express_route_links
WHERE expressRoutePortName = '{{ expressRoutePortName }}'
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
properties
FROM azure.network.express_route_links
WHERE expressRoutePortName = '{{ expressRoutePortName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

