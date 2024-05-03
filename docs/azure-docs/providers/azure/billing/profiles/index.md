---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - billing
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
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The properties of the billing profile. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Gets a billing profile by its ID. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the billing profiles that a user has access to. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Creates or updates a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
| <CopyableCode code="_list_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName" /> | Lists the billing profiles that a user has access to. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement. |
