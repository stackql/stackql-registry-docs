---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Location identifier. |
| <CopyableCode code="name" /> | `string` | Location name. |
| <CopyableCode code="displayName" /> | `string` | Display name of the location. |
| <CopyableCode code="latitude" /> | `string` | Latitude of the location. |
| <CopyableCode code="longitude" /> | `string` | Longitude of the location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get the specified location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of all AzureStack location. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="location, subscriptionId" /> | Updates the specified location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get a list of all AzureStack location. |
