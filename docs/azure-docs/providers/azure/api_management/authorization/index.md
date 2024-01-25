---
title: authorization
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization
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
<tr><td><b>Name</b></td><td><code>authorization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.authorization</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the authorization specified by its identifier. |
| `list_by_authorization_provider` | `SELECT` | `authorizationProviderId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of authorization providers defined within a authorization provider. |
| `create_or_update` | `INSERT` | `authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId` | Creates or updates authorization. |
| `delete` | `DELETE` | `If-Match, authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId` | Deletes specific Authorization from the Authorization provider. |
| `_list_by_authorization_provider` | `EXEC` | `authorizationProviderId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of authorization providers defined within a authorization provider. |
| `confirm_consent_code` | `EXEC` | `authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId` | Confirm valid consent code to suppress Authorizations anti-phishing page. |
