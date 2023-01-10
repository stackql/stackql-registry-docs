---
title: cloud_appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_appliances
  - stor_simple_8000_series
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
<tr><td><b>Name</b></td><td><code>cloud_appliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.cloud_appliances</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CloudAppliances_ListSupportedConfigurations` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Lists supported cloud appliance models and supported configurations. |
| `CloudAppliances_Provision` | `EXEC` | `managerName, resourceGroupName, subscriptionId, data__name, data__vnetRegion` | Provisions cloud appliance. |
