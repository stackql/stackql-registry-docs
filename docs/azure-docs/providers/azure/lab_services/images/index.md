---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - lab_services
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
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an image resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Gets an image resource. |
| <CopyableCode code="list_by_lab_plan" /> | `SELECT` |  | Gets all images from galleries attached to a lab plan. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="data__properties" /> | Updates an image resource via PUT. Creating new resources via PUT will not function. |
| <CopyableCode code="_list_by_lab_plan" /> | `EXEC` |  | Gets all images from galleries attached to a lab plan. |
| <CopyableCode code="update" /> | `EXEC` |  | Updates an image resource. |
