---
title: express_route_cross_connections_arp_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_cross_connections_arp_tables
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

Creates, updates, deletes, gets or lists a <code>express_route_cross_connections_arp_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_cross_connections_arp_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_cross_connections_arp_tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="age" /> | `integer` | Entry age in minutes. |
| <CopyableCode code="interface" /> | `string` | Interface address. |
| <CopyableCode code="ipAddress" /> | `string` | The IP address. |
| <CopyableCode code="macAddress" /> | `string` | The MAC address. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="crossConnectionName, devicePath, peeringName, resourceGroupName, subscriptionId" /> | Gets the currently advertised ARP table associated with the express route cross connection in a resource group. |

## `SELECT` examples

Gets the currently advertised ARP table associated with the express route cross connection in a resource group.


```sql
SELECT
age,
interface,
ipAddress,
macAddress
FROM azure.network.express_route_cross_connections_arp_tables
WHERE crossConnectionName = '{{ crossConnectionName }}'
AND devicePath = '{{ devicePath }}'
AND peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```