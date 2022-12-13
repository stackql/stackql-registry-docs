---
title: log_files
hide_title: false
hide_table_of_contents: false
keywords:
  - log_files
  - mysql
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
<tr><td><b>Name</b></td><td><code>log_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.log_files</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the log file. |
| `properties` | `object` | The properties of a log file. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `LogFiles_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` |
