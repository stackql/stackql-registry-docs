---
title: postal_codes
hide_title: false
hide_table_of_contents: false
keywords:
  - postal_codes
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>postal_codes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.postal_codes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this postal code. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#postalCode". |
| `code` | `string` | Postal code. This is equivalent to the id field. |
| `countryCode` | `string` | Country code of the country to which this postal code belongs. |
| `countryDartId` | `string` | DART ID of the country to which this postal code belongs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `postalCodes_get` | `SELECT` | `code, profileId` | Gets one postal code by ID. |
| `postalCodes_list` | `SELECT` | `profileId` | Retrieves a list of postal codes. |
