---
title: web_services
hide_title: false
hide_table_of_contents: false
keywords:
  - web_services
  - machine_learning
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
<tr><td><b>Name</b></td><td><code>web_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning.web_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource ID. |
| `name` | `string` | Specifies the name of the resource. |
| `type` | `string` | Specifies the type of the resource. |
| `location` | `string` | Specifies the location of the resource. |
| `properties` | `object` | The set of properties specific to the Azure ML web service resource. |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WebServices_Get` | `SELECT` | `resourceGroupName, subscriptionId, webServiceName` | Gets the Web Service Definition as specified by a subscription, resource group, and name. Note that the storage credentials and web service keys are not returned by this call. To get the web service access keys, call List Keys. |
| `WebServices_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the web services in the specified resource group. |
| `WebServices_ListBySubscriptionId` | `SELECT` | `subscriptionId` | Gets the web services in the specified subscription. |
| `WebServices_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, webServiceName, data__properties` | Create or update a web service. This call will overwrite an existing web service. Note that there is no warning or confirmation. This is a nonrecoverable operation. If your intent is to create a new web service, call the Get operation first to verify that it does not exist. |
| `WebServices_CreateRegionalProperties` | `EXEC` | `region, resourceGroupName, subscriptionId, webServiceName` | Creates an encrypted credentials parameter blob for the specified region. To get the web service from a region other than the region in which it has been created, you must first call Create Regional Web Services Properties to create a copy of the encrypted credential parameter blob in that region. You only need to do this before the first time that you get the web service in the new region. |
| `WebServices_ListKeys` | `EXEC` | `resourceGroupName, subscriptionId, webServiceName` | Gets the access keys for the specified web service. |
| `WebServices_Patch` | `EXEC` | `resourceGroupName, subscriptionId, webServiceName` | Modifies an existing web service resource. The PATCH API call is an asynchronous operation. To determine whether it has completed successfully, you must perform a Get operation. |
| `WebServices_Remove` | `EXEC` | `resourceGroupName, subscriptionId, webServiceName` | Deletes the specified web service. |
