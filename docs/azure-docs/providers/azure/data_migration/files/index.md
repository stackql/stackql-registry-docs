---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - data_migration
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
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_migration.files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Base class for file properties. |
| `systemData` | `object` |  |
| `type` | `string` | Resource type. |
| `etag` | `string` | HTTP strong entity tag value. This is ignored if submitted. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Files_Get` | `SELECT` |  | The files resource is a nested, proxy-only resource representing a file stored under the project resource. This method retrieves information about a file. |
| `Files_List` | `SELECT` | `api-version, groupName, projectName, serviceName, subscriptionId` | The project resource is a nested resource representing a stored migration project. This method returns a list of files owned by a project resource. |
| `Files_CreateOrUpdate` | `INSERT` |  | The PUT method creates a new file or updates an existing one. |
| `Files_Delete` | `DELETE` |  | This method deletes a file. |
| `Files_Read` | `EXEC` | `api-version, fileName, groupName, projectName, serviceName, subscriptionId` | This method is used for requesting storage information using which contents of the file can be downloaded. |
| `Files_ReadWrite` | `EXEC` | `api-version, fileName, groupName, projectName, serviceName, subscriptionId` | This method is used for requesting information for reading and writing the file content. |
| `Files_Update` | `EXEC` |  | This method updates an existing file. |
