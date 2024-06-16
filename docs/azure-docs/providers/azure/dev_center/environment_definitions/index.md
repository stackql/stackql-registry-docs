---
title: environment_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_definitions
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
<tr><td><b>Name</b></td><td><code>environment_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.environment_definitions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Gets an environment definition from the catalog. |
| <CopyableCode code="list_by_catalog" /> | `SELECT` | <CopyableCode code="catalogName, devCenterName, resourceGroupName, subscriptionId" /> | List environment definitions in the catalog. |
| <CopyableCode code="list_by_project_catalog" /> | `SELECT` | <CopyableCode code="catalogName, projectName, resourceGroupName, subscriptionId" /> | Lists the environment definitions in this project catalog. |
| <CopyableCode code="get_by_project_catalog" /> | `EXEC` |  | Gets an environment definition from the catalog. |
