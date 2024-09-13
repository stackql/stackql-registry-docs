
---
title: networks_peering_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - networks_peering_routes
  - compute
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

Creates, updates, deletes or gets an <code>networks_peering_route</code> resource or lists <code>networks_peering_routes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks_peering_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.networks_peering_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="destRange" /> | `string` | The destination range of the route. |
| <CopyableCode code="imported" /> | `boolean` | True if the peering route has been imported from a peer. The actual import happens if the field networkPeering.importCustomRoutes is true for this network, and networkPeering.exportCustomRoutes is true for the peer network, and the import does not result in a route conflict. |
| <CopyableCode code="nextHopRegion" /> | `string` | The region of peering route next hop, only applies to dynamic routes. |
| <CopyableCode code="priority" /> | `integer` | The priority of the peering route. |
| <CopyableCode code="type" /> | `string` | The type of the peering route. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_peering_routes" /> | `SELECT` | <CopyableCode code="network, project" /> | Lists the peering routes exchanged over peering connection. |

## `SELECT` examples

Lists the peering routes exchanged over peering connection.

```sql
SELECT
destRange,
imported,
nextHopRegion,
priority,
type
FROM google.compute.networks_peering_routes
WHERE network = '{{ network }}'
AND project = '{{ project }}'; 
```
