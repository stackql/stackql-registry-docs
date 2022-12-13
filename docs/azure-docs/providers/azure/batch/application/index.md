---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - batch
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
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.batch.application</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | The properties associated with the Application. |
| `type` | `string` | The type of the resource. |
| `etag` | `string` | The ETag of the resource, used for concurrency statements. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Application_Get` | `SELECT` | `accountName, applicationName, resourceGroupName, subscriptionId` | Gets information about the specified application. |
| `Application_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all of the applications in the specified account. |
| `Application_Create` | `INSERT` | `accountName, applicationName, resourceGroupName, subscriptionId` | Adds an application to the specified Batch account. |
| `Application_Delete` | `DELETE` | `accountName, applicationName, resourceGroupName, subscriptionId` | Deletes an application. |
| `Application_Update` | `EXEC` | `accountName, applicationName, resourceGroupName, subscriptionId` | Updates settings for the specified application. |
