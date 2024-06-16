---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - compute_admin
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
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.compute_admin.quotas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties for a Compute Quota |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, quotaName, subscriptionId" /> | Get an existing Compute Quota. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get a list of existing Compute quotas. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="location, quotaName, subscriptionId" /> | Creates or Updates a Compute Quota with the provided quota parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="location, quotaName, subscriptionId" /> | Delete an existing Compute quota. |
