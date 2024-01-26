---
title: local_rulestacks_advanced_security_objects
hide_title: false
hide_table_of_contents: false
keywords:
  - local_rulestacks_advanced_security_objects
  - paloaltonetworks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>local_rulestacks_advanced_security_objects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.paloaltonetworks.local_rulestacks_advanced_security_objects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | next link |
| `value` | `object` | List of custom and predefined url category |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `localRulestackName, resourceGroupName, subscriptionId, type` |
