---
title: connector_dryrun
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_dryrun
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
<tr><td><b>Name</b></td><td><code>connector_dryrun</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_connector.connector_dryrun</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dryrunName, location, resourceGroupName, subscriptionId` | get a dryrun job |
| `list` | `SELECT` | `location, resourceGroupName, subscriptionId` | list dryrun jobs |
| `create` | `INSERT` | `dryrunName, location, resourceGroupName, subscriptionId` | create a dryrun job to do necessary check before actual creation |
| `delete` | `DELETE` | `dryrunName, location, resourceGroupName, subscriptionId` | delete a dryrun job |
| `_list` | `EXEC` | `location, resourceGroupName, subscriptionId` | list dryrun jobs |
| `update` | `EXEC` | `dryrunName, location, resourceGroupName, subscriptionId` | update a dryrun job to do necessary check before actual creation |
