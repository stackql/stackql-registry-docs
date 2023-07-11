---
title: print_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - print_servers
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
<tr><td><b>Name</b></td><td><code>print_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.print_servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Immutable. ID of the print server. Leave empty when creating. |
| `name` | `string` | Immutable. Resource name of the print server. Leave empty when creating. Format: `customers/&#123;customer.id&#125;/printServers/&#123;print_server.id&#125;` |
| `description` | `string` | Editable. Description of the print server (as shown in the Admin console). |
| `orgUnitId` | `string` | ID of the organization unit (OU) that owns this print server. This value can only be set when the print server is initially created. If it's not populated, the print server is placed under the root OU. The `org_unit_id` can be retrieved using the [Directory API](/admin-sdk/directory/reference/rest/v1/orgunits). |
| `uri` | `string` | Editable. Print server URI. |
| `createTime` | `string` | Output only. Time when the print server was created. |
| `displayName` | `string` | Editable. Display name of the print server (as shown in the Admin console). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customersId, printServersId` | Returns a print server's configuration. |
| `list` | `SELECT` | `customersId` | Lists print server configurations. |
| `insert` | `INSERT` | `customersId` | Creates a print server. |
| `delete` | `DELETE` | `customersId, printServersId` | Deletes a print server. |
| `_list` | `EXEC` | `customersId` | Lists print server configurations. |
| `batchCreatePrintServers` | `EXEC` | `customersId` | Creates multiple print servers. |
| `batchDeletePrintServers` | `EXEC` | `customersId` | Deletes multiple print servers. |
| `patch` | `EXEC` | `customersId, printServersId` | Updates a print server's configuration. |
