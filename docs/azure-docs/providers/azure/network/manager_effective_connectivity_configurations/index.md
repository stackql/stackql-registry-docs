---
title: manager_effective_connectivity_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - manager_effective_connectivity_configurations
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

Creates, updates, deletes, gets or lists a <code>manager_effective_connectivity_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>manager_effective_connectivity_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.manager_effective_connectivity_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Connectivity configuration ID. |
| <CopyableCode code="configurationGroups" /> | `array` | Effective configuration groups. |
| <CopyableCode code="properties" /> | `object` | Properties of network manager connectivity configuration |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | List all effective connectivity configurations applied on a virtual network. |

## `SELECT` examples

List all effective connectivity configurations applied on a virtual network.


```sql
SELECT
id,
configurationGroups,
properties
FROM azure.network.manager_effective_connectivity_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}';
```