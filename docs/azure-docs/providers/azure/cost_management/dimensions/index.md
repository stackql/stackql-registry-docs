---
title: dimensions
hide_title: false
hide_table_of_contents: false
keywords:
  - dimensions
  - cost_management
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
<tr><td><b>Name</b></td><td><code>dimensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cost_management.dimensions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Dimensions_ByExternalCloudProviderType` | `EXEC` | `externalCloudProviderId, externalCloudProviderType` | Lists the dimensions by the external cloud provider type. |
| `Dimensions_List` | `EXEC` | `scope` | Lists the dimensions by the defined scope. |
