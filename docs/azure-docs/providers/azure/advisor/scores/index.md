---
title: scores
hide_title: false
hide_table_of_contents: false
keywords:
  - scores
  - advisor
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
<tr><td><b>Name</b></td><td><code>scores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.advisor.scores</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, subscriptionId` | Gets the advisor score. |
| `list` | `SELECT` | `subscriptionId` | Gets the list of advisor scores. |
| `_list` | `EXEC` | `subscriptionId` | Gets the list of advisor scores. |
