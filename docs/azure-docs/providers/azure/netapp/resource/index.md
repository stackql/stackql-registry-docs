---
title: resource
hide_title: false
hide_table_of_contents: false
keywords:
  - resource
  - netapp
  - azure    
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
<tr><td><b>Name</b></td><td><code>resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.resource</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetAppResource_CheckFilePathAvailability` | `EXEC` | `location, subscriptionId, data__name, data__subnetId` | Check if a file path is available. |
| `NetAppResource_CheckNameAvailability` | `EXEC` | `location, subscriptionId, data__name, data__resourceGroup, data__type` | Check if a resource name is available. |
| `NetAppResource_CheckQuotaAvailability` | `EXEC` | `location, subscriptionId, data__name, data__resourceGroup, data__type` | Check if a quota is available. |
| `NetAppResource_QueryRegionInfo` | `EXEC` | `location, subscriptionId` | Provides storage to network proximity and logical zone mapping information. |
