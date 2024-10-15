---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
  - storage_cache
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

Creates, updates, deletes, gets or lists a <code>skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of this SKU. |
| <CopyableCode code="capabilities" /> | `array` | A list of capabilities of this SKU, such as throughput or ops/sec. |
| <CopyableCode code="locationInfo" /> | `array` | The set of locations where the SKU is available. |
| <CopyableCode code="locations" /> | `array` | The set of locations where the SKU is available. This is the supported and registered Azure Geo Regions (e.g., West US, East US, Southeast Asia, etc.). |
| <CopyableCode code="resourceType" /> | `string` | The type of resource the SKU applies to. |
| <CopyableCode code="restrictions" /> | `array` | The restrictions preventing this SKU from being used. This is empty if there are no restrictions. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the list of StorageCache.Cache SKUs available to this subscription. |

## `SELECT` examples

Get the list of StorageCache.Cache SKUs available to this subscription.


```sql
SELECT
name,
capabilities,
locationInfo,
locations,
resourceType,
restrictions
FROM azure.storage_cache.skus
WHERE subscriptionId = '{{ subscriptionId }}';
```