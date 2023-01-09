---
title: accountstatuses
hide_title: false
hide_table_of_contents: false
keywords:
  - accountstatuses
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
<tr><td><b>Name</b></td><td><code>accountstatuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.accountstatuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accountManagement` | `string` | How the account is managed. Acceptable values are: - "`manual`" - "`automatic`"  |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#accountStatus`" |
| `products` | `array` | List of product-related data by channel, destination, and country. Data in this field may be delayed by up to 30 minutes. |
| `websiteClaimed` | `boolean` | Whether the account's website is claimed or not. |
| `accountId` | `string` | The ID of the account for which the status is reported. |
| `accountLevelIssues` | `array` | A list of account level issues. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, merchantId` | Retrieves the status of a Merchant Center account. No itemLevelIssues are returned for multi-client accounts. |
| `list` | `SELECT` | `merchantId` | Lists the statuses of the sub-accounts in your Merchant Center account. |
| `custombatch` | `EXEC` |  | Retrieves multiple Merchant Center account statuses in a single request. |
