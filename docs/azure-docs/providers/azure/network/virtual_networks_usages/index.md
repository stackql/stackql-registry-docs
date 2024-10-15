---
title: virtual_networks_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks_usages
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

Creates, updates, deletes, gets or lists a <code>virtual_networks_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_networks_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_networks_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Subnet identifier. |
| <CopyableCode code="name" /> | `object` | Usage strings container. |
| <CopyableCode code="currentValue" /> | `number` | Indicates number of IPs used from the Subnet. |
| <CopyableCode code="limit" /> | `number` | Indicates the size of the subnet. |
| <CopyableCode code="unit" /> | `string` | Usage units. Returns 'Count'. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Lists usage stats. |

## `SELECT` examples

Lists usage stats.


```sql
SELECT
id,
name,
currentValue,
limit,
unit
FROM azure.network.virtual_networks_usages
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}';
```