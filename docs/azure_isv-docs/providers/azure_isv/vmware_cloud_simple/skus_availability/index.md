---
title: skus_availability
hide_title: false
hide_table_of_contents: false
keywords:
  - skus_availability
  - vmware_cloud_simple
  - azure_isv    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skus_availability</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.skus_availability" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dedicatedAvailabilityZoneId" /> | `string` | CloudSimple Availability Zone id |
| <CopyableCode code="dedicatedAvailabilityZoneName" /> | `string` | CloudSimple Availability Zone Name |
| <CopyableCode code="dedicatedPlacementGroupId" /> | `string` | CloudSimple Placement Group Id |
| <CopyableCode code="dedicatedPlacementGroupName" /> | `string` | CloudSimple Placement Group name |
| <CopyableCode code="limit" /> | `integer` | indicates how many resources of a given SKU is available in a AZ-&gt;PG |
| <CopyableCode code="resourceType" /> | `string` | resource type e.g. DedicatedCloudNodes |
| <CopyableCode code="skuId" /> | `string` | sku id |
| <CopyableCode code="skuName" /> | `string` | sku name |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, regionId, subscriptionId" /> |
