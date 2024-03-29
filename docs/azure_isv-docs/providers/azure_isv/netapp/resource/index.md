---
title: resource
hide_title: false
hide_table_of_contents: false
keywords:
  - resource
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
<tr><td><b>Name</b></td><td><code>resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.resource</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `check_file_path_availability` | `EXEC` | `location, subscriptionId, data__name, data__subnetId` | Check if a file path is available. |
| `check_name_availability` | `EXEC` | `location, subscriptionId, data__name, data__resourceGroup, data__type` | Check if a resource name is available. |
| `check_quota_availability` | `EXEC` | `location, subscriptionId, data__name, data__resourceGroup, data__type` | Check if a quota is available. |
