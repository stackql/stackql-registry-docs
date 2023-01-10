---
title: shippingsettings
hide_title: false
hide_table_of_contents: false
keywords:
  - shippingsettings
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
<tr><td><b>Name</b></td><td><code>shippingsettings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.shippingsettings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accountId` | `string` | The ID of the account to which these account shipping settings belong. Ignored upon update, always present in get request responses. |
| `postalCodeGroups` | `array` | A list of postal code groups that can be referred to in `services`. Optional. |
| `services` | `array` | The target account's list of services. Optional. |
| `warehouses` | `array` | Optional. A list of warehouses which can be referred to in `services`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, merchantId` | Retrieves the shipping settings of the account. |
| `list` | `SELECT` | `merchantId` | Lists the shipping settings of the sub-accounts in your Merchant Center account. |
| `custombatch` | `EXEC` |  | Retrieves and updates the shipping settings of multiple accounts in a single request. |
| `update` | `EXEC` | `accountId, merchantId` | Updates the shipping settings of the account. Any fields that are not provided are deleted from the resource. |
