---
title: skus_availabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - skus_availabilities
  - vmware_cloud_simple
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

Creates, updates, deletes, gets or lists a <code>skus_availabilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skus_availabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.skus_availabilities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dedicatedAvailabilityZoneId" /> | `string` | CloudSimple Availability Zone id |
| <CopyableCode code="dedicatedAvailabilityZoneName" /> | `string` | CloudSimple Availability Zone Name |
| <CopyableCode code="dedicatedPlacementGroupId" /> | `string` | CloudSimple Placement Group Id |
| <CopyableCode code="dedicatedPlacementGroupName" /> | `string` | CloudSimple Placement Group name |
| <CopyableCode code="limit" /> | `integer` | indicates how many resources of a given SKU is available in a AZ->PG |
| <CopyableCode code="resourceType" /> | `string` | resource type e.g. DedicatedCloudNodes |
| <CopyableCode code="skuId" /> | `string` | sku id |
| <CopyableCode code="skuName" /> | `string` | sku name |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="regionId, subscriptionId" /> | Returns list of available resources in region |

## `SELECT` examples

Returns list of available resources in region


```sql
SELECT
dedicatedAvailabilityZoneId,
dedicatedAvailabilityZoneName,
dedicatedPlacementGroupId,
dedicatedPlacementGroupName,
limit,
resourceType,
skuId,
skuName
FROM azure_isv.vmware_cloud_simple.skus_availabilities
WHERE regionId = '{{ regionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```