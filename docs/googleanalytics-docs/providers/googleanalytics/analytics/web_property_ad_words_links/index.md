---
title: web_property_ad_words_links
hide_title: false
hide_table_of_contents: false
keywords:
  - web_property_ad_words_links
  - analytics
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
<tr><td><b>Name</b></td><td><code>web_property_ad_words_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.web_property_ad_words_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Entity Google Ads link ID |
| `name` | `string` | Name of the link. This field is required when creating a Google Ads link. |
| `profileIds` | `array` | IDs of linked Views (Profiles) represented as strings. |
| `selfLink` | `string` | URL link for this Google Analytics - Google Ads link. |
| `adWordsAccounts` | `array` | A list of Google Ads client accounts. These cannot be MCC accounts. This field is required when creating a Google Ads link. It cannot be empty. |
| `entity` | `object` | Web property being linked. |
| `kind` | `string` | Resource type for entity Google Ads link. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_webPropertyAdWordsLinks_get` | `SELECT` | `accountId, webPropertyAdWordsLinkId, webPropertyId` | Returns a web property-Google Ads link to which the user has access. |
| `management_webPropertyAdWordsLinks_list` | `SELECT` | `accountId, webPropertyId` | Lists webProperty-Google Ads links for a given web property. |
| `management_webPropertyAdWordsLinks_delete` | `DELETE` | `accountId, webPropertyAdWordsLinkId, webPropertyId` | Deletes a web property-Google Ads link. |
| `management_webPropertyAdWordsLinks_insert` | `EXEC` | `accountId, webPropertyId` | Creates a webProperty-Google Ads link. |
| `management_webPropertyAdWordsLinks_patch` | `EXEC` | `accountId, webPropertyAdWordsLinkId, webPropertyId` | Updates an existing webProperty-Google Ads link. This method supports patch semantics. |
| `management_webPropertyAdWordsLinks_update` | `EXEC` | `accountId, webPropertyAdWordsLinkId, webPropertyId` | Updates an existing webProperty-Google Ads link. |
