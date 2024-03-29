---
title: tag_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_resource
  - api_management
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
<tr><td><b>Name</b></td><td><code>tag_resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.tag_resource</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `api` | `object` | API contract properties for the Tag Resources. |
| `operation` | `object` | Operation Entity contract Properties. |
| `product` | `object` | Product profile. |
| `tag` | `object` | Contract defining the Tag property in the Tag Resource Contract |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` |
