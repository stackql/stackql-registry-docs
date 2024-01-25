---
title: watchers_troubleshooting
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_troubleshooting
  - network
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
<tr><td><b>Name</b></td><td><code>watchers_troubleshooting</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.watchers_troubleshooting</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `code` | `string` | The result code of the troubleshooting. |
| `endTime` | `string` | The end time of the troubleshooting. |
| `results` | `array` | Information from troubleshooting. |
| `startTime` | `string` | The start time of the troubleshooting. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `networkWatcherName, resourceGroupName, subscriptionId, data__properties, data__targetResourceId` |
