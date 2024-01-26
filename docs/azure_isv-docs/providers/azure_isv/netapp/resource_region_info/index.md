---
title: resource_region_info
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_region_info
  - netapp
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>resource_region_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.resource_region_info</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `availabilityZoneMappings` | `array` | Provides logical availability zone mappings for the subscription for a region. |
| `storageToNetworkProximity` | `string` | Provides storage to network proximity information in the region. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `query_region_info` | `SELECT` | `location, subscriptionId` |
