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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Gets an existing custom domain within an endpoint. |
| `list_by_endpoint` | `SELECT` | `endpointName, profileName, resourceGroupName, subscriptionId` | Lists all of the existing custom domains within an endpoint. |
| `create` | `INSERT` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Creates a new custom domain within an endpoint. |
| `delete` | `DELETE` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Deletes an existing custom domain within an endpoint. |
| `_list_by_endpoint` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId` | Lists all of the existing custom domains within an endpoint. |
| `disable_custom_https` | `EXEC` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Disable https delivery of the custom domain. |
| `enable_custom_https` | `EXEC` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, data__certificateSource, data__protocolType` | Enable https delivery of the custom domain. |
