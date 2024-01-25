---
title: linkers_dryrun
hide_title: false
hide_table_of_contents: false
keywords:
  - linkers_dryrun
  - service_connector
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
<tr><td><b>Name</b></td><td><code>linkers_dryrun</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_connector.linkers_dryrun</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dryrunName, resourceUri` | get a dryrun job |
| `list` | `SELECT` | `resourceUri` | list dryrun jobs |
| `create` | `INSERT` | `dryrunName, resourceUri` | create a dryrun job to do necessary check before actual creation |
| `delete` | `DELETE` | `dryrunName, resourceUri` | delete a dryrun job |
| `_list` | `EXEC` | `resourceUri` | list dryrun jobs |
| `update` | `EXEC` | `dryrunName, resourceUri` | add a dryrun job to do necessary check before actual creation |
