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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>printer_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.printer_models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="displayName" /> | `string` | Display name. eq. "Brother MFC-8840D" |
| <CopyableCode code="makeAndModel" /> | `string` | Make and model as represented in "make_and_model" field in Printer object. eq. "brother mfc-8840d" |
| <CopyableCode code="manufacturer" /> | `string` | Manufacturer. eq. "Brother" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customersId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customersId" /> |
