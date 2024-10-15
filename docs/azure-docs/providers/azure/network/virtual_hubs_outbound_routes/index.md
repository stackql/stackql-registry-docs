---
title: virtual_hubs_outbound_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hubs_outbound_routes
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

Creates, updates, deletes, gets or lists a <code>virtual_hubs_outbound_routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_hubs_outbound_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_hubs_outbound_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="asPath" /> | `string` | The ASPath of this route. |
| <CopyableCode code="bgpCommunities" /> | `string` | BGP communities of the route. |
| <CopyableCode code="prefix" /> | `string` | The address prefix of the route. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Gets the outbound routes configured for the Virtual Hub on a particular connection. |

## `SELECT` examples

Gets the outbound routes configured for the Virtual Hub on a particular connection.


```sql
SELECT
asPath,
bgpCommunities,
prefix
FROM azure.network.virtual_hubs_outbound_routes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualHubName = '{{ virtualHubName }}';
```