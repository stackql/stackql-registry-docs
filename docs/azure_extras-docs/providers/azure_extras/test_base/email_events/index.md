---
title: email_events
hide_title: false
hide_table_of_contents: false
keywords:
  - email_events
  - test_base
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
<tr><td><b>Name</b></td><td><code>email_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.email_events</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `emailEventResourceName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets a email event of a Test Base Account. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the email events of a Test Base Account. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the email events of a Test Base Account. |
