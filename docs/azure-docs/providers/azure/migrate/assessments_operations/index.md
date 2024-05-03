---
title: assessments_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments_operations
  - migrate
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
<tr><td><b>Name</b></td><td><code>assessments_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.assessments_operations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assessmentName, groupName, projectName, resourceGroupName, subscriptionId" /> | Get a Assessment |
| <CopyableCode code="list_by_group" /> | `SELECT` | <CopyableCode code="groupName, projectName, resourceGroupName, subscriptionId" /> | List Assessment resources by Group |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="assessmentName, groupName, projectName, resourceGroupName, subscriptionId" /> | Create a Assessment |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assessmentName, groupName, projectName, resourceGroupName, subscriptionId" /> | Delete a Assessment |
| <CopyableCode code="_list_by_group" /> | `EXEC` | <CopyableCode code="groupName, projectName, resourceGroupName, subscriptionId" /> | List Assessment resources by Group |
| <CopyableCode code="download_url" /> | `EXEC` | <CopyableCode code="assessmentName, groupName, projectName, resourceGroupName, subscriptionId" /> | Get the URL for downloading the assessment in a report format. |
