---
title: express_route_circuits_routes_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuits_routes_tables
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

Creates, updates, deletes, gets or lists a <code>express_route_circuits_routes_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_circuits_routes_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuits_routes_tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="locPrf" /> | `string` | Local preference value as set with the set local-preference route-map configuration command. |
| <CopyableCode code="network" /> | `string` | IP address of a network entity. |
| <CopyableCode code="nextHop" /> | `string` | NextHop address. |
| <CopyableCode code="path" /> | `string` | Autonomous system paths to the destination network. |
| <CopyableCode code="weight" /> | `integer` | Route Weight. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="circuitName, devicePath, peeringName, resourceGroupName, subscriptionId" /> | Gets the currently advertised routes table associated with the express route circuit in a resource group. |

## `SELECT` examples

Gets the currently advertised routes table associated with the express route circuit in a resource group.


```sql
SELECT
locPrf,
network,
nextHop,
path,
weight
FROM azure.network.express_route_circuits_routes_tables
WHERE circuitName = '{{ circuitName }}'
AND devicePath = '{{ devicePath }}'
AND peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```