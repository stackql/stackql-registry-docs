---
title: kusto_pools_skus_by_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pools_skus_by_resources
  - synapse
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

Creates, updates, deletes, gets or lists a <code>kusto_pools_skus_by_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kusto_pools_skus_by_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pools_skus_by_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capacity" /> | `object` | Azure capacity definition. |
| <CopyableCode code="resourceType" /> | `string` | Resource Namespace and Type. |
| <CopyableCode code="sku" /> | `object` | Azure SKU definition. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns the SKUs available for the provided resource. |

## `SELECT` examples

Returns the SKUs available for the provided resource.


```sql
SELECT
capacity,
resourceType,
sku
FROM azure.synapse.kusto_pools_skus_by_resources
WHERE kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```