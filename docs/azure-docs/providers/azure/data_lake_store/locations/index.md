---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - data_lake_store
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
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_lake_store.locations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Locations_GetCapability` | `EXEC` | `location, subscriptionId` | Gets subscription-level properties and limits for Data Lake Store specified by resource location. |
| `Locations_GetUsage` | `EXEC` | `location, subscriptionId` | Gets the current usage count and the limit for the resources of the location under the subscription. |
