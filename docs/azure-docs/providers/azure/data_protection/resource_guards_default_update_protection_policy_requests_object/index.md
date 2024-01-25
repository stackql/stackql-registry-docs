---
title: resource_guards_default_update_protection_policy_requests_object
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_guards_default_update_protection_policy_requests_object
  - data_protection
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
<tr><td><b>Name</b></td><td><code>resource_guards_default_update_protection_policy_requests_object</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.resource_guards_default_update_protection_policy_requests_object</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `requestName, resourceGroupName, resourceGuardsName, subscriptionId` |
