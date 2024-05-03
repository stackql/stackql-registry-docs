---
title: communications_no_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - communications_no_subscription
  - support
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
<tr><td><b>Name</b></td><td><code>communications_no_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.communications_no_subscription" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a communication resource. |
| <CopyableCode code="type" /> | `string` | Type of the resource 'Microsoft.Support/communications'. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="communicationName, supportTicketName" /> | Returns communication details for a support ticket. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="communicationName, supportTicketName" /> | Adds a new customer communication to an Azure support ticket. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="supportTicketName, data__name, data__type" /> | Check the availability of a resource name. This API should be used to check the uniqueness of the name for adding a new communication to the support ticket. |
