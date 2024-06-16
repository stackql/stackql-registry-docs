---
title: log_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - log_profiles
  - monitor
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
<tr><td><b>Name</b></td><td><code>log_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.log_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The log profile properties. |
| <CopyableCode code="tags" /> | `` | Resource tags |
| <CopyableCode code="type" /> | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="logProfileName, subscriptionId" /> | Gets the log profile. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List the log profiles. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="logProfileName, subscriptionId, data__properties" /> | Create or update a log profile in Azure Monitoring REST API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="logProfileName, subscriptionId" /> | Deletes the log profile. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="logProfileName, subscriptionId" /> | Updates an existing LogProfilesResource. To update other fields use the CreateOrUpdate method. |
