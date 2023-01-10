---
title: api_portal_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - api_portal_custom_domains
  - app_platform
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>api_portal_custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.api_portal_custom_domains</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiPortalCustomDomains_Get` | `SELECT` | `apiPortalName, domainName, resourceGroupName, serviceName, subscriptionId` | Get the API portal custom domain. |
| `ApiPortalCustomDomains_List` | `SELECT` | `apiPortalName, resourceGroupName, serviceName, subscriptionId` | Handle requests to list all API portal custom domains. |
| `ApiPortalCustomDomains_CreateOrUpdate` | `INSERT` | `apiPortalName, domainName, resourceGroupName, serviceName, subscriptionId` | Create or update the API portal custom domain. |
| `ApiPortalCustomDomains_Delete` | `DELETE` | `apiPortalName, domainName, resourceGroupName, serviceName, subscriptionId` | Delete the API portal custom domain. |
