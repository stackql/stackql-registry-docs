---
title: kusto_pools_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pools_skus
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

Creates, updates, deletes, gets or lists a <code>kusto_pools_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kusto_pools_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pools_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the SKU |
| <CopyableCode code="locationInfo" /> | `array` | Locations and zones |
| <CopyableCode code="locations" /> | `array` | The set of locations that the SKU is available |
| <CopyableCode code="resourceType" /> | `string` | The resource type |
| <CopyableCode code="restrictions" /> | `array` | The restrictions because of which SKU cannot be used |
| <CopyableCode code="size" /> | `string` | The size of the SKU |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists eligible SKUs for Kusto Pool resource. |

## `SELECT` examples

Lists eligible SKUs for Kusto Pool resource.


```sql
SELECT
name,
locationInfo,
locations,
resourceType,
restrictions,
size
FROM azure.synapse.kusto_pools_skus
WHERE subscriptionId = '{{ subscriptionId }}';
```