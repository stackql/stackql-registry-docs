---
title: peering_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - peering_routes
  - vmwareengine
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

Creates, updates, deletes or gets an <code>peering_route</code> resource or lists <code>peering_routes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>peering_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.peering_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="destRange" /> | `string` | Output only. Destination range of the peering route in CIDR notation. |
| <CopyableCode code="direction" /> | `string` | Output only. Direction of the routes exchanged with the peer network, from the VMware Engine network perspective: * Routes of direction `INCOMING` are imported from the peer network. * Routes of direction `OUTGOING` are exported from the intranet VPC network of the VMware Engine network. |
| <CopyableCode code="imported" /> | `boolean` | Output only. True if the peering route has been imported from a peered VPC network; false otherwise. The import happens if the field `NetworkPeering.importCustomRoutes` is true for this network, `NetworkPeering.exportCustomRoutes` is true for the peer VPC network, and the import does not result in a route conflict. |
| <CopyableCode code="nextHopRegion" /> | `string` | Output only. Region containing the next hop of the peering route. This field only applies to dynamic routes in the peer VPC network. |
| <CopyableCode code="priority" /> | `string` | Output only. The priority of the peering route. |
| <CopyableCode code="type" /> | `string` | Output only. Type of the route in the peer VPC network. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, privateConnectionsId, projectsId" /> | Lists the private connection routes exchanged over a peering connection. |

## `SELECT` examples

Lists the private connection routes exchanged over a peering connection.

```sql
SELECT
destRange,
direction,
imported,
nextHopRegion,
priority,
type
FROM google.vmwareengine.peering_routes
WHERE locationsId = '{{ locationsId }}'
AND privateConnectionsId = '{{ privateConnectionsId }}'
AND projectsId = '{{ projectsId }}'; 
```
