---
title: alert_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_configurations
  - authorization
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
<tr><td><b>Name</b></td><td><code>alert_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.alert_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The alert configuration ID. |
| <CopyableCode code="name" /> | `string` | The alert configuration name. |
| <CopyableCode code="properties" /> | `object` | Alert configuration properties. |
| <CopyableCode code="type" /> | `string` | The alert configuration type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertId, scope" /> | Get the specified alert configuration. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="alertId, scope" /> | Update an alert configuration. |
