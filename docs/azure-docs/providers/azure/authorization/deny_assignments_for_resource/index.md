---
title: deny_assignments_for_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - deny_assignments_for_resource
  - authorization
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
<tr><td><b>Name</b></td><td><code>deny_assignments_for_resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.deny_assignments_for_resource</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The deny assignment ID. |
| `name` | `string` | The deny assignment name. |
| `properties` | `object` | Deny assignment properties. |
| `type` | `string` | The deny assignment type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` |
| `_list` | `EXEC` | `parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` |
