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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>budgets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.billingbudgets.budgets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `budgets` | `array` | List of the budgets owned by the requested billing account. |
| `nextPageToken` | `string` | If not empty, indicates that there may be more budgets that match the request; this value should be passed in a new `ListBudgetsRequest`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `billingAccountsId, budgetsId` | Returns a budget. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. When reading from the API, you will not see these fields in the return value, though they may have been set in the Cloud Console. |
| `list` | `SELECT` | `billingAccountsId` | Returns a list of budgets for a billing account. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. When reading from the API, you will not see these fields in the return value, though they may have been set in the Cloud Console. |
| `create` | `INSERT` | `billingAccountsId` | Creates a new budget. See [Quotas and limits](https://cloud.google.com/billing/quotas) for more information on the limits of the number of budgets you can create. |
| `delete` | `DELETE` | `billingAccountsId, budgetsId` | Deletes a budget. Returns successfully if already deleted. |
| `patch` | `EXEC` | `billingAccountsId, budgetsId` | Updates a budget and returns the updated budget. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. Budget fields that are not exposed in this API will not be changed by this method. |
