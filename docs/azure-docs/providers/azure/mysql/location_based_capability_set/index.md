---
title: location_based_capability_set
hide_title: false
hide_table_of_contents: false
keywords:
  - location_based_capability_set
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
<tr><td><b>Name</b></td><td><code>location_based_capability_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mysql.location_based_capability_set</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `capabilitySetName, locationName, subscriptionId` |
| `list` | `SELECT` | `locationName, subscriptionId` |
| `_list` | `EXEC` | `locationName, subscriptionId` |
