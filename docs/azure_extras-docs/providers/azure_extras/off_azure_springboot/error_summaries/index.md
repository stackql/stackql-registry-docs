---
title: error_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - error_summaries
  - off_azure_springboot
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
<tr><td><b>Name</b></td><td><code>error_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.off_azure_springboot.error_summaries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Error summary properties |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `errorSummaryName, resourceGroupName, siteName, subscriptionId` | Gets the ErrorSummaries resource. |
| `list_by_site` | `SELECT` | `resourceGroupName, siteName, subscriptionId` | Lists the ErrorSummaries resource in springbootsites. |
| `_list_by_site` | `EXEC` | `resourceGroupName, siteName, subscriptionId` | Lists the ErrorSummaries resource in springbootsites. |
