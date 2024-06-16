---
title: encryption_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_sets
  - dev_center
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
<tr><td><b>Name</b></td><td><code>encryption_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.encryption_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the devcenter encryption set. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devCenterName, encryptionSetName, resourceGroupName, subscriptionId" /> | Gets a devcenter encryption set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Lists all encryption sets in the devcenter. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="devCenterName, encryptionSetName, resourceGroupName, subscriptionId" /> | Creates or updates a devcenter encryption set resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="devCenterName, encryptionSetName, resourceGroupName, subscriptionId" /> | Deletes a devcenter encryption set |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="devCenterName, encryptionSetName, resourceGroupName, subscriptionId" /> | Partially updates a devcenter encryption set. |
