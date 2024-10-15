---
title: mobile_networks_sim_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - mobile_networks_sim_groups
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

Creates, updates, deletes, gets or lists a <code>mobile_networks_sim_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mobile_networks_sim_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.mobile_networks_sim_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (User assigned identity) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | SIM group properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Gets all the SIM groups assigned to a mobile network. |

## `SELECT` examples

Gets all the SIM groups assigned to a mobile network.


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.mobile_network.mobile_networks_sim_groups
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```