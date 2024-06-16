---
title: community_trainings
hide_title: false
hide_table_of_contents: false
keywords:
  - community_trainings
  - community_training
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>community_trainings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.community_training.community_trainings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of the Community CommunityTraining. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="communityTrainingName, resourceGroupName, subscriptionId" /> | Get a CommunityTraining |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List CommunityTraining resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List CommunityTraining resources by subscription ID |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="communityTrainingName, resourceGroupName, subscriptionId" /> | Create a CommunityTraining |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="communityTrainingName, resourceGroupName, subscriptionId" /> | Delete a CommunityTraining |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="communityTrainingName, resourceGroupName, subscriptionId" /> | Update a CommunityTraining |
