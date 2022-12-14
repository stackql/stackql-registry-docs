---
title: location
hide_title: false
hide_table_of_contents: false
keywords:
  - location
  - container_instance
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
<tr><td><b>Name</b></td><td><code>location</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_instance.location</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Location_ListCachedImages` | `EXEC` | `location, subscriptionId` | Get the list of cached images on specific OS type for a subscription in a region. |
| `Location_ListCapabilities` | `EXEC` | `location, subscriptionId` | Get the list of CPU/memory/GPU capabilities of a region. |
| `Location_ListUsage` | `EXEC` | `location, subscriptionId` | Get the usage for a subscription |
