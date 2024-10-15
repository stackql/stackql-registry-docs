---
title: sites_packet_cores
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_packet_cores
  - mobile_network
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

Creates, updates, deletes, gets or lists a <code>sites_packet_cores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites_packet_cores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.sites_packet_cores" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mobileNetworkName, resourceGroupName, siteName, subscriptionId" /> | Deletes a packet core under the specified mobile network site. |

## `DELETE` example

Deletes the specified <code>sites_packet_cores</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.sites_packet_cores
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
