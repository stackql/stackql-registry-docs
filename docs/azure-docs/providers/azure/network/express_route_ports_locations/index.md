---
title: express_route_ports_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_ports_locations
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

Creates, updates, deletes, gets or lists a <code>express_route_ports_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_ports_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_ports_locations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_ports_locations', value: 'view', },
        { label: 'express_route_ports_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="address" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_bandwidths" /> | `text` | field from the `properties` object |
| <CopyableCode code="contact" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="locationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties specific to ExpressRoutePorts peering location resources. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Retrieves a single ExpressRoutePort peering location, including the list of available bandwidths available at said peering location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves all ExpressRoutePort peering locations. Does not return available bandwidths for each location. Available bandwidths can only be obtained when retrieving a specific peering location. |

## `SELECT` examples

Retrieves all ExpressRoutePort peering locations. Does not return available bandwidths for each location. Available bandwidths can only be obtained when retrieving a specific peering location.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_express_route_ports_locations', value: 'view', },
        { label: 'express_route_ports_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
address,
available_bandwidths,
contact,
location,
locationName,
provisioning_state,
subscriptionId,
tags,
type
FROM azure.network.vw_express_route_ports_locations
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
FROM azure.network.express_route_ports_locations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

