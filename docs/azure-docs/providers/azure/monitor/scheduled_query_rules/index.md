---
title: scheduled_query_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_query_rules
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
<tr><td><b>Name</b></td><td><code>scheduled_query_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.scheduled_query_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `etag` | `string` | The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.  |
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | Indicates the type of scheduled query rule. The default is LogAlert. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | scheduled query rule Definition |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, ruleName, subscriptionId` | Retrieve an scheduled query rule definition. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve scheduled query rule definitions in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Retrieve a scheduled query rule definitions in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, ruleName, subscriptionId, data__location, data__properties` | Creates or updates a scheduled query rule. |
| `delete` | `DELETE` | `resourceGroupName, ruleName, subscriptionId` | Deletes a scheduled query rule. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieve scheduled query rule definitions in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Retrieve a scheduled query rule definitions in a subscription. |
| `update` | `EXEC` | `resourceGroupName, ruleName, subscriptionId` | Update a scheduled query rule. |
