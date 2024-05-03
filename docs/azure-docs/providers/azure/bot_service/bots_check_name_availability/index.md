---
title: bots_check_name_availability
hide_title: false
hide_table_of_contents: false
keywords:
  - bots_check_name_availability
  - bot_service
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
<tr><td><b>Name</b></td><td><code>bots_check_name_availability</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.bots_check_name_availability" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="absCode" /> | `string` | response code from ABS |
| <CopyableCode code="message" /> | `string` | additional message from the bot management api showing why a bot name is not available |
| <CopyableCode code="valid" /> | `boolean` | indicates if the bot name is valid. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` |  |
