---
title: printer_models
hide_title: false
hide_table_of_contents: false
keywords:
  - printer_models
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>printer_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.printer_models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `makeAndModel` | `string` | Make and model as represented in "make_and_model" field in Printer object. eq. "brother mfc-8840d" |
| `manufacturer` | `string` | Manufacturer. eq. "Brother" |
| `displayName` | `string` | Display name. eq. "Brother MFC-8840D" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `customersId` |
| `_list` | `EXEC` | `customersId` |
