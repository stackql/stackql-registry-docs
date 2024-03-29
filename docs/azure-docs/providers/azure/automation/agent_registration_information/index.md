---
title: agent_registration_information
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_registration_information
  - automation
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
<tr><td><b>Name</b></td><td><code>agent_registration_information</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.agent_registration_information</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the id. |
| `dscMetaConfiguration` | `string` | Gets or sets the dsc meta configuration. |
| `endpoint` | `string` | Gets or sets the dsc server endpoint. |
| `keys` | `object` | Definition of the agent registration keys. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve the automation agent registration information. |
| `regenerate_key` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId, data__keyName` | Regenerate a primary or secondary agent registration key |
