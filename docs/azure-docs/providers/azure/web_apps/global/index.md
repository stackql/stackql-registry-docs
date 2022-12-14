---
title: global
hide_title: false
hide_table_of_contents: false
keywords:
  - global
  - web_apps
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
<tr><td><b>Name</b></td><td><code>global</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.global</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Global_GetDeletedWebApp` | `EXEC` | `deletedSiteId, subscriptionId` | Description for Get deleted app for a subscription. |
| `Global_GetDeletedWebAppSnapshots` | `EXEC` | `deletedSiteId, subscriptionId` | Description for Get all deleted apps for a subscription. |
| `Global_GetSubscriptionOperationWithAsyncResponse` | `EXEC` | `location, operationId, subscriptionId` | Description for Gets an operation in a subscription and given region |
