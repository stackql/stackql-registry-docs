---
title: google_ads_links
hide_title: false
hide_table_of_contents: false
keywords:
  - google_ads_links
  - analyticsadmin
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>google_ads_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsadmin.google_ads_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `googleAdsLinks` | `array` | List of GoogleAdsLinks. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `properties_googleAdsLinks_list` | `SELECT` | `propertiesId` | Lists GoogleAdsLinks on a property. |
| `properties_googleAdsLinks_create` | `INSERT` | `propertiesId` | Creates a GoogleAdsLink. |
| `properties_googleAdsLinks_delete` | `DELETE` | `googleAdsLinksId, propertiesId` | Deletes a GoogleAdsLink on a property |
| `properties_googleAdsLinks_patch` | `EXEC` | `googleAdsLinksId, propertiesId` | Updates a GoogleAdsLink on a property |
