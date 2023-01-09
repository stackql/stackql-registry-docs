---
title: campaign_creative_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - campaign_creative_associations
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
<tr><td><b>Name</b></td><td><code>campaign_creative_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.campaign_creative_associations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#campaignCreativeAssociationsListResponse". |
| `nextPageToken` | `string` | Pagination token to be used for the next list operation. |
| `campaignCreativeAssociations` | `array` | Campaign creative association collection |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `campaignCreativeAssociations_list` | `SELECT` | `campaignId, profileId` | Retrieves the list of creative IDs associated with the specified campaign. This method supports paging. |
| `campaignCreativeAssociations_insert` | `EXEC` | `campaignId, profileId` | Associates a creative with the specified campaign. This method creates a default ad with dimensions matching the creative in the campaign if such a default ad does not exist already. |
