---
title: log_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - log_profiles
  - monitor
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
<tr><td><b>Name</b></td><td><code>log_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.log_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | The log profile properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LogProfiles_Get` | `SELECT` | `logProfileName, subscriptionId` | Gets the log profile. |
| `LogProfiles_List` | `SELECT` | `subscriptionId` | List the log profiles. |
| `LogProfiles_CreateOrUpdate` | `INSERT` | `logProfileName, subscriptionId, data__properties` | Create or update a log profile in Azure Monitoring REST API. |
| `LogProfiles_Delete` | `DELETE` | `logProfileName, subscriptionId` | Deletes the log profile. |
| `LogProfiles_Update` | `EXEC` | `logProfileName, subscriptionId` | Updates an existing LogProfilesResource. To update other fields use the CreateOrUpdate method. |
