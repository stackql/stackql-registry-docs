---
title: sensitivity_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - sensitivity_settings
  - security
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sensitivity_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.sensitivity_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the sensitivity settings |
| <CopyableCode code="name" /> | `string` | The name of the sensitivity settings |
| <CopyableCode code="properties" /> | `object` | The sensitivity settings properties |
| <CopyableCode code="type" /> | `string` | The type of the sensitivity settings |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version" /> | Gets data sensitivity settings for sensitive data discovery |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version" /> | Gets a list with a single sensitivity settings resource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, data__sensitiveInfoTypesIds" /> | Create or update data sensitivity settings for sensitive data discovery |
