---
title: api_version_set
hide_title: false
hide_table_of_contents: false
keywords:
  - api_version_set
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
<tr><td><b>Name</b></td><td><code>api_version_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_version_set</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, versionSetId` | Gets the details of the Api Version Set specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of API Version Sets in the specified service instance. |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, versionSetId` | Creates or Updates a Api Version Set. |
| `delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, subscriptionId, versionSetId` | Deletes specific Api Version Set. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of API Version Sets in the specified service instance. |
| `update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId, versionSetId` | Updates the details of the Api VersionSet specified by its identifier. |
