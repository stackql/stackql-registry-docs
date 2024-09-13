---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
  - networkconnectivity
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

Creates, updates, deletes or gets an <code>route</code> resource or lists <code>routes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of the route. Route names must be unique. Route names use the following form: `projects/{project_number}/locations/global/hubs/{hub}/routeTables/{route_table_id}/routes/{route_id}` |
| <CopyableCode code="description" /> | `string` | An optional description of the route. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the route was created. |
| <CopyableCode code="ipCidrRange" /> | `string` | The destination IP address range. |
| <CopyableCode code="labels" /> | `object` | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| <CopyableCode code="location" /> | `string` | Output only. The origin location of the route. Uses the following form: "projects/{project}/locations/{location}" Example: projects/1234/locations/us-central1 |
| <CopyableCode code="nextHopInterconnectAttachment" /> | `object` | A route next hop that leads to an interconnect attachment resource. |
| <CopyableCode code="nextHopRouterApplianceInstance" /> | `object` | A route next hop that leads to a Router appliance instance. |
| <CopyableCode code="nextHopVpcNetwork" /> | `object` |  |
| <CopyableCode code="nextHopVpnTunnel" /> | `object` | A route next hop that leads to a VPN tunnel resource. |
| <CopyableCode code="priority" /> | `string` | Output only. The priority of this route. Priority is used to break ties in cases where a destination matches more than one route. In these cases the route with the lowest-numbered priority value wins. |
| <CopyableCode code="spoke" /> | `string` | Immutable. The spoke that this route leads to. Example: projects/12345/locations/global/spokes/SPOKE |
| <CopyableCode code="state" /> | `string` | Output only. The current lifecycle state of the route. |
| <CopyableCode code="type" /> | `string` | Output only. The route's type. Its type is determined by the properties of its IP address range. |
| <CopyableCode code="uid" /> | `string` | Output only. The Google-generated UUID for the route. This value is unique across all Network Connectivity Center route resources. If a route is deleted and another with the same name is created, the new route is assigned a different `uid`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the route was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubsId, projectsId, routeTablesId, routesId" /> | Gets details about the specified route. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="hubsId, projectsId, routeTablesId" /> | Lists routes in a given route table. |

## `SELECT` examples

Lists routes in a given route table.

```sql
SELECT
name,
description,
createTime,
ipCidrRange,
labels,
location,
nextHopInterconnectAttachment,
nextHopRouterApplianceInstance,
nextHopVpcNetwork,
nextHopVpnTunnel,
priority,
spoke,
state,
type,
uid,
updateTime
FROM google.networkconnectivity.routes
WHERE hubsId = '{{ hubsId }}'
AND projectsId = '{{ projectsId }}'
AND routeTablesId = '{{ routeTablesId }}'; 
```
