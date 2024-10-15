---
title: managed_clusters_outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters_outbound_network_dependencies_endpoints
  - aks
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

Creates, updates, deletes, gets or lists a <code>managed_clusters_outbound_network_dependencies_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_clusters_outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.managed_clusters_outbound_network_dependencies_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="category" /> | `string` | The category of endpoints accessed by the AKS agent node, e.g. azure-resource-management, apiserver, etc. |
| <CopyableCode code="endpoints" /> | `array` | The endpoints that AKS agent nodes connect to |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets a list of egress endpoints (network endpoints of all outbound dependencies) in the specified managed cluster. The operation returns properties of each egress endpoint. |

## `SELECT` examples

Gets a list of egress endpoints (network endpoints of all outbound dependencies) in the specified managed cluster. The operation returns properties of each egress endpoint.


```sql
SELECT
category,
endpoints
FROM azure.aks.managed_clusters_outbound_network_dependencies_endpoints
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```