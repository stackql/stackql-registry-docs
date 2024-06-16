---
title: apps_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - apps_templates
  - iot_central
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
<tr><td><b>Name</b></td><td><code>apps_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_central.apps_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the template. |
| <CopyableCode code="description" /> | `string` | The description of the template. |
| <CopyableCode code="industry" /> | `string` | The industry of the template. |
| <CopyableCode code="locations" /> | `array` | A list of locations that support the template. |
| <CopyableCode code="manifestId" /> | `string` | The ID of the template. |
| <CopyableCode code="manifestVersion" /> | `string` | The version of the template. |
| <CopyableCode code="order" /> | `number` | The order of the template in the templates list. |
| <CopyableCode code="title" /> | `string` | The title of the template. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> |
