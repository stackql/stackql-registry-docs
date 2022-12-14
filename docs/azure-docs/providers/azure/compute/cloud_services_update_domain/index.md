---
title: cloud_services_update_domain
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_services_update_domain
  - compute
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
<tr><td><b>Name</b></td><td><code>cloud_services_update_domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.cloud_services_update_domain</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CloudServicesUpdateDomain_GetUpdateDomain` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId, updateDomain` | Gets the specified update domain of a cloud service. Use nextLink property in the response to get the next page of update domains. Do this till nextLink is null to fetch all the update domains. |
| `CloudServicesUpdateDomain_ListUpdateDomains` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId` | Gets a list of all update domains in a cloud service. |
| `CloudServicesUpdateDomain_WalkUpdateDomain` | `EXEC` | `cloudServiceName, resourceGroupName, subscriptionId, updateDomain` | Updates the role instances in the specified update domain. |
