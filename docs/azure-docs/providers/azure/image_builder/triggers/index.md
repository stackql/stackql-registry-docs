---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
  - image_builder
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
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.image_builder.triggers" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId, triggerName" /> | Get the specified trigger for the specified image template resource |
| <CopyableCode code="list_by_image_template" /> | `SELECT` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | List all triggers for the specified Image Template resource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId, triggerName" /> | Create or update a trigger for the specified virtual machine image template |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId, triggerName" /> | Delete a trigger for the specified virtual machine image template |
