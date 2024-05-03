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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>print_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.print_servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Immutable. ID of the print server. Leave empty when creating. |
| <CopyableCode code="name" /> | `string` | Immutable. Resource name of the print server. Leave empty when creating. Format: `customers/&#123;customer.id&#125;/printServers/&#123;print_server.id&#125;` |
| <CopyableCode code="description" /> | `string` | Editable. Description of the print server (as shown in the Admin console). |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the print server was created. |
| <CopyableCode code="displayName" /> | `string` | Editable. Display name of the print server (as shown in the Admin console). |
| <CopyableCode code="orgUnitId" /> | `string` | ID of the organization unit (OU) that owns this print server. This value can only be set when the print server is initially created. If it's not populated, the print server is placed under the root OU. The `org_unit_id` can be retrieved using the [Directory API](/admin-sdk/directory/reference/rest/v1/orgunits). |
| <CopyableCode code="uri" /> | `string` | Editable. Print server URI. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customersId, printServersId" /> | Returns a print server's configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customersId" /> | Lists print server configurations. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="customersId" /> | Creates a print server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customersId, printServersId" /> | Deletes a print server. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customersId" /> | Lists print server configurations. |
| <CopyableCode code="batchCreatePrintServers" /> | `EXEC` | <CopyableCode code="customersId" /> | Creates multiple print servers. |
| <CopyableCode code="batchDeletePrintServers" /> | `EXEC` | <CopyableCode code="customersId" /> | Deletes multiple print servers. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="customersId, printServersId" /> | Updates a print server's configuration. |
