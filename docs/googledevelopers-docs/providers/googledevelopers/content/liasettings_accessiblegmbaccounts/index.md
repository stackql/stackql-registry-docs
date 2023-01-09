---
title: liasettings_accessiblegmbaccounts
hide_title: false
hide_table_of_contents: false
keywords:
  - liasettings_accessiblegmbaccounts
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
<tr><td><b>Name</b></td><td><code>liasettings_accessiblegmbaccounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.liasettings_accessiblegmbaccounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `gmbAccounts` | `array` | A list of Business Profiles which are available to the merchant. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#liasettingsGetAccessibleGmbAccountsResponse`". |
| `accountId` | `string` | The ID of the Merchant Center account. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `liasettings_getaccessiblegmbaccounts` | `SELECT` | `accountId, merchantId` |
