---
title: services_supported_server_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - services_supported_server_versions
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>services_supported_server_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.services_supported_server_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `server` | `string` | The server name. |
| `value` | `string` | The raw server version value which could be passed to deployment CRUD operations. |
| `version` | `string` | The Server version. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` |
