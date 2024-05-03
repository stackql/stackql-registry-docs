---
title: budgets
hide_title: false
hide_table_of_contents: false
keywords:
  - budgets
  - billingbudgets
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>budgets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.billingbudgets.budgets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the budget. The resource name implies the scope of a budget. Values are of the form `billingAccounts/&#123;billingAccountId&#125;/budgets/&#123;budgetId&#125;`. |
| <CopyableCode code="amount" /> | `object` | The budgeted amount for each usage period. |
| <CopyableCode code="budgetFilter" /> | `object` | A filter for a budget, limiting the scope of the cost to calculate. |
| <CopyableCode code="displayName" /> | `string` | User data for display name in UI. The name must be less than or equal to 60 characters. |
| <CopyableCode code="etag" /> | `string` | Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag causes an update to overwrite other changes. |
| <CopyableCode code="notificationsRule" /> | `object` | NotificationsRule defines notifications that are sent based on budget spend and thresholds. |
| <CopyableCode code="thresholdRules" /> | `array` | Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget. Optional for `pubsubTopic` notifications. Required if using email notifications. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountsId, budgetsId" /> | Returns a budget. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. When reading from the API, you will not see these fields in the return value, though they may have been set in the Cloud Console. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountsId" /> | Returns a list of budgets for a billing account. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. When reading from the API, you will not see these fields in the return value, though they may have been set in the Cloud Console. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="billingAccountsId" /> | Creates a new budget. See [Quotas and limits](https://cloud.google.com/billing/quotas) for more information on the limits of the number of budgets you can create. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="billingAccountsId, budgetsId" /> | Deletes a budget. Returns successfully if already deleted. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="billingAccountsId" /> | Returns a list of budgets for a billing account. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. When reading from the API, you will not see these fields in the return value, though they may have been set in the Cloud Console. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="billingAccountsId, budgetsId" /> | Updates a budget and returns the updated budget. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. Budget fields that are not exposed in this API will not be changed by this method. |
