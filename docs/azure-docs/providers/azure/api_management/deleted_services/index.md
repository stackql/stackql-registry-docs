---
title: deleted_services
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_services
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
<tr><td><b>Name</b></td><td><code>deleted_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.deleted_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | API Management Service Master Location. |
| `properties` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all soft-deleted services available for undelete for the given subscription. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all soft-deleted services available for undelete for the given subscription. |
| `get_by_name` | `EXEC` | `location, serviceName, subscriptionId` | Get soft-deleted Api Management Service by name. |
| `purge` | `EXEC` | `location, serviceName, subscriptionId` | Purges Api Management Service (deletes it with no option to undelete). |
