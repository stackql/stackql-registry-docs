---
title: configuration_stores_deleted
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_stores_deleted
  - app_configuration
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
<tr><td><b>Name</b></td><td><code>configuration_stores_deleted</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.configuration_stores_deleted" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID for the deleted configuration store. |
| <CopyableCode code="name" /> | `string` | The name of the configuration store. |
| <CopyableCode code="properties" /> | `object` | Properties of the deleted configuration store. |
| <CopyableCode code="type" /> | `string` | The resource type of the configuration store. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configStoreName, location, subscriptionId" /> | Gets a deleted Azure app configuration store. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets information about the deleted configuration stores in a subscription. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets information about the deleted configuration stores in a subscription. |
