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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>printers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.printers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the printer. (During printer creation leave empty) |
| <CopyableCode code="name" /> | `string` | The resource name of the Printer object, in the format customers/&#123;customer-id&#125;/printers/&#123;printer-id&#125; (During printer creation leave empty) |
| <CopyableCode code="description" /> | `string` | Editable. Description of printer. |
| <CopyableCode code="auxiliaryMessages" /> | `array` | Output only. Auxiliary messages about issues with the printer configuration if any. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when printer was created. |
| <CopyableCode code="displayName" /> | `string` | Editable. Name of printer. |
| <CopyableCode code="makeAndModel" /> | `string` | Editable. Make and model of printer. e.g. Lexmark MS610de Value must be in format as seen in ListPrinterModels response. |
| <CopyableCode code="orgUnitId" /> | `string` | Organization Unit that owns this printer (Only can be set during Printer creation) |
| <CopyableCode code="uri" /> | `string` | Editable. Printer URI. |
| <CopyableCode code="useDriverlessConfig" /> | `boolean` | Editable. flag to use driverless configuration or not. If it's set to be true, make_and_model can be ignored |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customersId, printersId" /> | Returns a `Printer` resource (printer's config). |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customersId" /> | List printers configs. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="customersId" /> | Creates a printer under given Organization Unit. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customersId, printersId" /> | Deletes a `Printer`. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customersId" /> | List printers configs. |
| <CopyableCode code="batchCreatePrinters" /> | `EXEC` | <CopyableCode code="customersId" /> | Creates printers under given Organization Unit. |
| <CopyableCode code="batchDeletePrinters" /> | `EXEC` | <CopyableCode code="customersId" /> | Deletes printers in batch. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="customersId, printersId" /> | Updates a `Printer` resource. |
