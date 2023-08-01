---
title: node_count_information
hide_title: false
hide_table_of_contents: false
keywords:
  - node_count_information
  - automation
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>node_count_information</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.node_count_information</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `totalCount` | `integer` | Gets the total number of records matching countType criteria. |
| `value` | `array` | Gets an array of counts |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `NodeCountInformation_Get` | `SELECT` | `automationAccountName, countType, resourceGroupName, subscriptionId` |
