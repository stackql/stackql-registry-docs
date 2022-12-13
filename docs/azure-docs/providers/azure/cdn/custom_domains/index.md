---
title: custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_domains
  - cdn
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
<tr><td><b>Name</b></td><td><code>custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.custom_domains</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CustomDomains_Get` | `SELECT` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Gets an existing custom domain within an endpoint. |
| `CustomDomains_ListByEndpoint` | `SELECT` | `endpointName, profileName, resourceGroupName, subscriptionId` | Lists all of the existing custom domains within an endpoint. |
| `CustomDomains_Create` | `INSERT` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Creates a new custom domain within an endpoint. |
| `CustomDomains_Delete` | `DELETE` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Deletes an existing custom domain within an endpoint. |
| `CustomDomains_DisableCustomHttps` | `EXEC` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Disable https delivery of the custom domain. |
| `CustomDomains_EnableCustomHttps` | `EXEC` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, data__certificateSource, data__protocolType` | Enable https delivery of the custom domain. |
