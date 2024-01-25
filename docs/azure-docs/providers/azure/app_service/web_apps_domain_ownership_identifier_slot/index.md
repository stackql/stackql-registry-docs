---
title: web_apps_domain_ownership_identifier_slot
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_domain_ownership_identifier_slot
  - app_service
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
<tr><td><b>Name</b></td><td><code>web_apps_domain_ownership_identifier_slot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_domain_ownership_identifier_slot</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | Identifier resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domainOwnershipIdentifierName, name, resourceGroupName, slot, subscriptionId` | Description for Get domain ownership identifier for web app. |
| `create_or_update` | `INSERT` | `domainOwnershipIdentifierName, name, resourceGroupName, slot, subscriptionId` | Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier. |
| `delete` | `DELETE` | `domainOwnershipIdentifierName, name, resourceGroupName, slot, subscriptionId` | Description for Deletes a domain ownership identifier for a web app. |
| `update` | `EXEC` | `domainOwnershipIdentifierName, name, resourceGroupName, slot, subscriptionId` | Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier. |
