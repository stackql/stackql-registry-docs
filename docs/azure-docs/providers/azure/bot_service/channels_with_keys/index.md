---
title: channels_with_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - channels_with_keys
  - bot_service
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
<tr><td><b>Name</b></td><td><code>channels_with_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.bot_service.channels_with_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `changedTime` | `string` | Changed time of the resource |
| `entityTag` | `string` | Entity tag of the resource |
| `properties` | `object` | Channel definition |
| `provisioningState` | `string` | Provisioning state of the resource |
| `resource` | `object` | Channel definition |
| `setting` | `object` | Channel settings definition |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `channelName, resourceGroupName, resourceName, subscriptionId` |
