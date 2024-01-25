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
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | The log profile properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| `type` | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `logProfileName, subscriptionId` | Gets the log profile. |
| `list` | `SELECT` | `subscriptionId` | List the log profiles. |
| `create_or_update` | `INSERT` | `logProfileName, subscriptionId, data__properties` | Create or update a log profile in Azure Monitoring REST API. |
| `delete` | `DELETE` | `logProfileName, subscriptionId` | Deletes the log profile. |
| `_list` | `EXEC` | `subscriptionId` | List the log profiles. |
| `update` | `EXEC` | `logProfileName, subscriptionId` | Updates an existing LogProfilesResource. To update other fields use the CreateOrUpdate method. |
