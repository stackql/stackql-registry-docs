---
title: network_fabrics_topologies
hide_title: false
hide_table_of_contents: false
keywords:
  - network_fabrics_topologies
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>network_fabrics_topologies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_fabrics_topologies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_fabrics_topologies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configurationState" /> | `string` | Configuration state for the resource. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="url" /> | `string` | URL for the details of the response. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFabricName, resourceGroupName, subscriptionId" /> | Gets Topology of the underlying resources in the given Network Fabric instance. |

## `SELECT` examples

Gets Topology of the underlying resources in the given Network Fabric instance.


```sql
SELECT
configurationState,
error,
url
FROM azure.managed_network_fabric.network_fabrics_topologies
WHERE networkFabricName = '{{ networkFabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```