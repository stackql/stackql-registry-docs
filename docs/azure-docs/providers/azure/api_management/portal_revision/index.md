---
title: portal_revision
hide_title: false
hide_table_of_contents: false
keywords:
  - portal_revision
  - api_management
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
<tr><td><b>Name</b></td><td><code>portal_revision</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.portal_revision</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` |  |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PortalRevision_Get` | `SELECT` | `portalRevisionId, resourceGroupName, serviceName, subscriptionId` | Gets the developer portal's revision specified by its identifier. |
| `PortalRevision_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists developer portal's revisions. |
| `PortalRevision_CreateOrUpdate` | `INSERT` | `portalRevisionId, resourceGroupName, serviceName, subscriptionId` | Creates a new developer portal's revision by running the portal's publishing. The `isCurrent` property indicates if the revision is publicly accessible. |
| `PortalRevision_GetEntityTag` | `EXEC` | `portalRevisionId, resourceGroupName, serviceName, subscriptionId` | Gets the developer portal revision specified by its identifier. |
| `PortalRevision_Update` | `EXEC` | `If-Match, portalRevisionId, resourceGroupName, serviceName, subscriptionId` | Updates the description of specified portal revision or makes it current. |
