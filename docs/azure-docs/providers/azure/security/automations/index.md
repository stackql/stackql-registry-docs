---
title: automations
hide_title: false
hide_table_of_contents: false
keywords:
  - automations
  - security
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
<tr><td><b>Name</b></td><td><code>automations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.automations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | A set of properties that defines the behavior of the automation configuration. To learn more about the supported security events data models schemas - please visit https://aka.ms/ASCAutomationSchemas. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Automations_Get` | `SELECT` | `api-version, automationName, resourceGroupName, subscriptionId` | Retrieves information about the model of a security automation. |
| `Automations_List` | `SELECT` | `api-version, subscriptionId` | Lists all the security automations in the specified subscription. Use the 'nextLink' property in the response to get the next page of security automations for the specified subscription. |
| `Automations_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Lists all the security automations in the specified resource group. Use the 'nextLink' property in the response to get the next page of security automations for the specified resource group. |
| `Automations_CreateOrUpdate` | `INSERT` | `api-version, automationName, resourceGroupName, subscriptionId` | Creates or updates a security automation. If a security automation is already created and a subsequent request is issued for the same automation id, then it will be updated. |
| `Automations_Delete` | `DELETE` | `api-version, automationName, resourceGroupName, subscriptionId` | Deletes a security automation. |
| `Automations_Validate` | `EXEC` | `api-version, automationName, resourceGroupName, subscriptionId` | Validates the security automation model before create or update. Any validation errors are returned to the client. |
