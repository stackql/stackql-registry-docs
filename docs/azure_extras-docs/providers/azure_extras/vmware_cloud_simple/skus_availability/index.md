---
title: skus_availability
hide_title: false
hide_table_of_contents: false
keywords:
  - skus_availability
  - vmware_cloud_simple
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>skus_availability</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.vmware_cloud_simple.skus_availability</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `skuName` | `string` | sku name |
| `dedicatedAvailabilityZoneId` | `string` | CloudSimple Availability Zone id |
| `dedicatedAvailabilityZoneName` | `string` | CloudSimple Availability Zone Name |
| `dedicatedPlacementGroupId` | `string` | CloudSimple Placement Group Id |
| `dedicatedPlacementGroupName` | `string` | CloudSimple Placement Group name |
| `limit` | `integer` | indicates how many resources of a given SKU is available in a AZ-&gt;PG |
| `resourceType` | `string` | resource type e.g. DedicatedCloudNodes |
| `skuId` | `string` | sku id |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SkusAvailability_List` | `SELECT` | `api-version, regionId, subscriptionId` |
