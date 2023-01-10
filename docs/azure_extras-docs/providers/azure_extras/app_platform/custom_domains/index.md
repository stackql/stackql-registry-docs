---
title: custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_domains
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
<tr><td><b>Name</b></td><td><code>custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.custom_domains</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CustomDomains_Get` | `SELECT` | `appName, domainName, resourceGroupName, serviceName, subscriptionId` | Get the custom domain of one lifecycle application. |
| `CustomDomains_List` | `SELECT` | `appName, resourceGroupName, serviceName, subscriptionId` | List the custom domains of one lifecycle application. |
| `CustomDomains_CreateOrUpdate` | `INSERT` | `appName, domainName, resourceGroupName, serviceName, subscriptionId` | Create or update custom domain of one lifecycle application. |
| `CustomDomains_Delete` | `DELETE` | `appName, domainName, resourceGroupName, serviceName, subscriptionId` | Delete the custom domain of one lifecycle application. |
| `CustomDomains_Update` | `EXEC` | `appName, domainName, resourceGroupName, serviceName, subscriptionId` | Update custom domain of one lifecycle application. |
