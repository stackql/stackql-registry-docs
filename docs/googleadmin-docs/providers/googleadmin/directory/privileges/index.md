---
title: privileges
hide_title: false
hide_table_of_contents: false
keywords:
  - privileges
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>privileges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.privileges</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `isOuScopable` | `boolean` | If the privilege can be restricted to an organization unit. |
| `kind` | `string` | The type of the API resource. This is always `admin#directory#privilege`. |
| `privilegeName` | `string` | The name of the privilege. |
| `serviceId` | `string` | The obfuscated ID of the service this privilege is for. This value is returned with [`Privileges.list()`](/admin-sdk/directory/v1/reference/privileges/list). |
| `serviceName` | `string` | The name of the service this privilege is for. |
| `childPrivileges` | `array` | A list of child privileges. Privileges for a service form a tree. Each privilege can have a list of child privileges; this list is empty for a leaf privilege. |
| `etag` | `string` | ETag of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `customer` |
