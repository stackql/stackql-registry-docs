---
title: students
hide_title: false
hide_table_of_contents: false
keywords:
  - students
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
<tr><td><b>Name</b></td><td><code>students</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.education.students</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Student detail properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `billingAccountName, billingProfileName, invoiceSectionName, studentAlias` | Get the details for a specific student in the specified lab by student alias |
| `list` | `SELECT` | `billingAccountName, billingProfileName, invoiceSectionName` | Get a list of details about students that are associated with the specified lab. |
| `create_or_update` | `INSERT` | `billingAccountName, billingProfileName, invoiceSectionName, studentAlias` | Create and add a new student to the specified lab or update the details of an existing student in a lab. Note the student must have a valid tenant to accept the lab after they have been added to lab. |
| `delete` | `DELETE` | `billingAccountName, billingProfileName, invoiceSectionName, studentAlias` | Delete the specified student based on the student alias. |
| `_list` | `EXEC` | `billingAccountName, billingProfileName, invoiceSectionName` | Get a list of details about students that are associated with the specified lab. |
