---
title: deal_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - deal_associations
  - adexchangebuyer2
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
<tr><td><b>Name</b></td><td><code>deal_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.deal_associations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token to retrieve the next page of results. Pass this value in the ListDealAssociationsRequest.page_token field in the subsequent call to 'ListDealAssociation' method to retrieve the next page of results. |
| `associations` | `array` | The list of associations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_creatives_dealAssociations_list` | `SELECT` | `accountId, creativeId` | List all creative-deal associations. |
| `accounts_creatives_dealAssociations_add` | `EXEC` | `accountId, creativeId` | Associate an existing deal with a creative. |
| `accounts_creatives_dealAssociations_remove` | `EXEC` | `accountId, creativeId` | Remove the association between a deal and a creative. |
