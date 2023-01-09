---
title: liasettings
hide_title: false
hide_table_of_contents: false
keywords:
  - liasettings
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
<tr><td><b>Name</b></td><td><code>liasettings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.liasettings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `countrySettings` | `array` | The LIA settings for each country. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#liaSettings`" |
| `accountId` | `string` | The ID of the account to which these LIA settings belong. Ignored upon update, always present in get request responses. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, merchantId` | Retrieves the LIA settings of the account. |
| `list` | `SELECT` | `merchantId` | Lists the LIA settings of the sub-accounts in your Merchant Center account. |
| `custombatch` | `EXEC` |  | Retrieves and/or updates the LIA settings of multiple accounts in a single request. |
| `requestgmbaccess` | `EXEC` | `accountId, gmbEmail, merchantId` | Requests access to a specified Business Profile. |
| `requestinventoryverification` | `EXEC` | `accountId, country, merchantId` | Requests inventory validation for the specified country. |
| `setinventoryverificationcontact` | `EXEC` | `accountId, contactEmail, contactName, country, language, merchantId` | Sets the inventory verification contract for the specified country. |
| `setposdataprovider` | `EXEC` | `accountId, country, merchantId` | Sets the POS data provider for the specified country. |
| `update` | `EXEC` | `accountId, merchantId` | Updates the LIA settings of the account. Any fields that are not provided are deleted from the resource. |
