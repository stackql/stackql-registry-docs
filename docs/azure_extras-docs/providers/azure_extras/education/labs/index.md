---
title: labs
hide_title: false
hide_table_of_contents: false
keywords:
  - labs
  - education
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
<tr><td><b>Name</b></td><td><code>labs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.education.labs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Lab detail result properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Labs_List` | `SELECT` | `billingAccountName, billingProfileName, invoiceSectionName` | Get the details for a specific lab associated with the provided billing account name, billing profile name, and invoice section name. |
| `Labs_ListAll` | `SELECT` | `billingAccountName, billingProfileName` | Get a list of labs associated with the provided billing account name and billing profile name. |
| `Labs_CreateOrUpdate` | `INSERT` | `billingAccountName, billingProfileName, invoiceSectionName` | Create a new lab or update a previously created lab. |
| `Labs_Delete` | `DELETE` | `billingAccountName, billingProfileName, invoiceSectionName` | Delete a specific lab associated with the provided billing account name, billing profile name, and invoice section name. Note all students must be removed from the lab in order to delete the lab. |
| `Labs_GenerateInviteCode` | `EXEC` | `billingAccountName, billingProfileName, invoiceSectionName` | Generate invite code for a lab |
| `Labs_Get` | `EXEC` | `billingAccountName, billingProfileName, invoiceSectionName` | Get the details for a specific lab associated with the provided billing account name, billing profile name, and invoice section name. |
