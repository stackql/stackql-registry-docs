---
title: printers
hide_title: false
hide_table_of_contents: false
keywords:
  - printers
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
<tr><td><b>Name</b></td><td><code>printers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.printers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the printer. (During printer creation leave empty) |
| `name` | `string` | The resource name of the Printer object, in the format customers/&#123;customer-id&#125;/printers/&#123;printer-id&#125; (During printer creation leave empty) |
| `description` | `string` | Editable. Description of printer. |
| `displayName` | `string` | Editable. Name of printer. |
| `createTime` | `string` | Output only. Time when printer was created. |
| `orgUnitId` | `string` | Organization Unit that owns this printer (Only can be set during Printer creation) |
| `makeAndModel` | `string` | Editable. Make and model of printer. e.g. Lexmark MS610de Value must be in format as seen in ListPrinterModels response. |
| `auxiliaryMessages` | `array` | Output only. Auxiliary messages about issues with the printer configuration if any. |
| `uri` | `string` | Editable. Printer URI. |
| `useDriverlessConfig` | `boolean` | Editable. flag to use driverless configuration or not. If it's set to be true, make_and_model can be ignored |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customersId, printersId` | Returns a `Printer` resource (printer's config). |
| `list` | `SELECT` | `customersId` | List printers configs. |
| `insert` | `INSERT` | `customersId` | Creates a printer under given Organization Unit. |
| `delete` | `DELETE` | `customersId, printersId` | Deletes a `Printer`. |
| `_list` | `EXEC` | `customersId` | List printers configs. |
| `batchCreatePrinters` | `EXEC` | `customersId` | Creates printers under given Organization Unit. |
| `batchDeletePrinters` | `EXEC` | `customersId` | Deletes printers in batch. |
| `patch` | `EXEC` | `customersId, printersId` | Updates a `Printer` resource. |
