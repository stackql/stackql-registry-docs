---
title: user_classic_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - user_classic_accounts
  - video_indexer
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
<tr><td><b>Name</b></td><td><code>user_classic_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.video_indexer.user_classic_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The account's id |
| `name` | `string` | The account's name |
| `location` | `string` | The account's location |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `UserClassicAccounts_List` | `SELECT` | `location` |
