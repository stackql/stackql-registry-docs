---
title: notification_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_operations
  - marketplace_notifications
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
<tr><td><b>Name</b></td><td><code>notification_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.marketplace_notifications.notification_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the operation |
| `display` | `object` | Operation display payload |
| `isDataAction` | `boolean` | Indicates whether the operation is a data action |
| `origin` | `string` | operation origin |
| `properties` | `object` | operation properties |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version` |
| `_get` | `EXEC` | `api-version` |
