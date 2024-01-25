---
title: authorization_server_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_server_secrets
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
<tr><td><b>Name</b></td><td><code>authorization_server_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.authorization_server_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `clientSecret` | `string` | oAuth Authorization Server Secrets. |
| `resourceOwnerPassword` | `string` | Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password. |
| `resourceOwnerUsername` | `string` | Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `authsid, resourceGroupName, serviceName, subscriptionId` |
