---
title: filters
hide_title: false
hide_table_of_contents: false
keywords:
  - filters
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
<tr><td><b>Name</b></td><td><code>filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.filters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Filter ID. |
| `name` | `string` | Name of this filter. |
| `includeDetails` | `object` | JSON template for an Analytics filter expression. |
| `lowercaseDetails` | `object` | Details for the filter of the type LOWER. |
| `searchAndReplaceDetails` | `object` | Details for the filter of the type SEARCH_AND_REPLACE. |
| `selfLink` | `string` | Link for this filter. |
| `created` | `string` | Time this filter was created. |
| `type` | `string` | Type of this filter. Possible values are INCLUDE, EXCLUDE, LOWERCASE, UPPERCASE, SEARCH_AND_REPLACE and ADVANCED. |
| `parentLink` | `object` | Parent link for this filter. Points to the account to which this filter belongs. |
| `excludeDetails` | `object` | JSON template for an Analytics filter expression. |
| `uppercaseDetails` | `object` | Details for the filter of the type UPPER. |
| `accountId` | `string` | Account ID to which this filter belongs. |
| `advancedDetails` | `object` | Details for the filter of the type ADVANCED. |
| `updated` | `string` | Time this filter was last modified. |
| `kind` | `string` | Resource type for Analytics filter. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_filters_get` | `SELECT` | `accountId, filterId` | Returns filters to which the user has access. |
| `management_filters_list` | `SELECT` | `accountId` | Lists all filters for an account |
| `management_filters_delete` | `DELETE` | `accountId, filterId` | Delete a filter. |
| `management_filters_insert` | `EXEC` | `accountId` | Create a new filter. |
| `management_filters_patch` | `EXEC` | `accountId, filterId` | Updates an existing filter. This method supports patch semantics. |
| `management_filters_update` | `EXEC` | `accountId, filterId` | Updates an existing filter. |
