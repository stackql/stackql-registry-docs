---
title: tenant_access_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_access_secrets
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
<tr><td><b>Name</b></td><td><code>tenant_access_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.tenant_access_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Access Information type ('access' or 'gitAccess') |
| `enabled` | `boolean` | Determines whether direct access is enabled. |
| `primaryKey` | `string` | Primary access key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
| `principalId` | `string` | Principal (User) Identifier. |
| `secondaryKey` | `string` | Secondary access key. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accessName, resourceGroupName, serviceName, subscriptionId` |
