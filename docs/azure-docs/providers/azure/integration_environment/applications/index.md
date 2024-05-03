---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - integration_environment
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.integration_environment.applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of application. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId" /> | Get a Application |
| <CopyableCode code="list_by_space" /> | `SELECT` | <CopyableCode code="resourceGroupName, spaceName, subscriptionId" /> | List Application resources by Space |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId" /> | Create a Application |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId" /> | Delete a Application |
| <CopyableCode code="_list_by_space" /> | `EXEC` | <CopyableCode code="resourceGroupName, spaceName, subscriptionId" /> | List Application resources by Space |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId" /> | Update a Application |
| <CopyableCode code="save_business_process_development_artifact" /> | `EXEC` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId, data__name" /> | The save business process development artifact action. |
| <CopyableCode code="validate_business_process_development_artifact" /> | `EXEC` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId, data__name" /> | The validate business process development artifact action. |
