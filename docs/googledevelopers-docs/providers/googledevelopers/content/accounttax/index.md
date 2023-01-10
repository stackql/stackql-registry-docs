---
title: accounttax
hide_title: false
hide_table_of_contents: false
keywords:
  - accounttax
  - content
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounttax</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.accounttax</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#accountTax`". |
| `rules` | `array` | Tax rules. Updating the tax rules will enable "US" taxes (not reversible). Defining no rules is equivalent to not charging tax at all. |
| `accountId` | `string` | Required. The ID of the account to which these account tax settings belong. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, merchantId` | Retrieves the tax settings of the account. |
| `list` | `SELECT` | `merchantId` | Lists the tax settings of the sub-accounts in your Merchant Center account. |
| `custombatch` | `EXEC` |  | Retrieves and updates tax settings of multiple accounts in a single request. |
| `update` | `EXEC` | `accountId, merchantId` | Updates the tax settings of the account. Any fields that are not provided are deleted from the resource. |
