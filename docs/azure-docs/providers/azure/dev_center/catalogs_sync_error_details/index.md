---
title: catalogs_sync_error_details
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs_sync_error_details
  - dev_center
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
<tr><td><b>Name</b></td><td><code>catalogs_sync_error_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_center.catalogs_sync_error_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `conflicts` | `array` | Catalog items that have conflicting names. |
| `errors` | `array` | Errors that occured during synchronization. |
| `operationError` | `object` | Catalog error details |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` |  |
