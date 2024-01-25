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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `portalRevisionId, resourceGroupName, serviceName, subscriptionId` | Gets the developer portal's revision specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists developer portal's revisions. |
| `create_or_update` | `INSERT` | `portalRevisionId, resourceGroupName, serviceName, subscriptionId` | Creates a new developer portal's revision by running the portal's publishing. The `isCurrent` property indicates if the revision is publicly accessible. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists developer portal's revisions. |
| `update` | `EXEC` | `If-Match, portalRevisionId, resourceGroupName, serviceName, subscriptionId` | Updates the description of specified portal revision or makes it current. |
