---
title: applications_business_process_development_artifact
hide_title: false
hide_table_of_contents: false
keywords:
  - applications_business_process_development_artifact
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
<tr><td><b>Name</b></td><td><code>applications_business_process_development_artifact</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.integration_environment.applications_business_process_development_artifact" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the business process development artifact. |
| <CopyableCode code="properties" /> | `object` | The properties of business process development artifact. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId, data__name" /> | The get business process development artifact action. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId, data__name" /> | The delete business process development artifact action. |
