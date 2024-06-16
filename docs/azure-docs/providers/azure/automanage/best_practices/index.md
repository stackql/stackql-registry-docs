---
title: best_practices
hide_title: false
hide_table_of_contents: false
keywords:
  - best_practices
  - automanage
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
<tr><td><b>Name</b></td><td><code>best_practices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.best_practices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID for the best practice.  For example, /providers/Microsoft.Automanage/bestPractices/azureBestPracticesProduction |
| <CopyableCode code="name" /> | `string` | The name of the best practice. For example, azureBestPracticesProduction |
| <CopyableCode code="properties" /> | `object` | Automanage configuration profile properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource.  For example, Microsoft.Automanage/bestPractices |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bestPracticeName" /> | Get information about a Automanage best practice |
| <CopyableCode code="list_by_tenant" /> | `SELECT` |  | Retrieve a list of Automanage best practices |
