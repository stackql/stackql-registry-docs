---
title: disk_pool_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_pool_zones
  - storage_pool
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

Creates, updates, deletes, gets or lists a <code>disk_pool_zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_pool_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_pool.disk_pool_zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="additionalCapabilities" /> | `array` | List of additional capabilities for Disk Pool. |
| <CopyableCode code="availabilityZones" /> | `array` | Logical zone for Disk Pool resource; example: ["1"]. |
| <CopyableCode code="sku" /> | `object` | Sku for ARM resource |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Lists available Disk Pool Skus in an Azure location. |

## `SELECT` examples

Lists available Disk Pool Skus in an Azure location.


```sql
SELECT
additionalCapabilities,
availabilityZones,
sku
FROM azure.storage_pool.disk_pool_zones
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```