---
title: virtual_hub_bgp_connections_advertised_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hub_bgp_connections_advertised_routes
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

Creates, updates, deletes, gets or lists a <code>virtual_hub_bgp_connections_advertised_routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_hub_bgp_connections_advertised_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_hub_bgp_connections_advertised_routes" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionName, hubName, resourceGroupName, subscriptionId" /> | Retrieves a list of routes the virtual hub bgp connection is advertising to the specified peer. |

## `SELECT` examples

Retrieves a list of routes the virtual hub bgp connection is advertising to the specified peer.


```sql
SELECT

FROM azure.network.virtual_hub_bgp_connections_advertised_routes
WHERE connectionName = '{{ connectionName }}'
AND hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```