---
title: product_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - product_packages
  - deployment_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>product_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.deployment_admin.product_packages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties for Product package. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packageId, subscriptionId" /> | Retrieves the specific product package details. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns an array of product packages. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="packageId, subscriptionId" /> | Creates a new product package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="packageId, subscriptionId" /> | Deletes a product package. |
