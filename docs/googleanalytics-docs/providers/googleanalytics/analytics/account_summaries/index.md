---
title: account_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - account_summaries
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
<tr><td><b>Name</b></td><td><code>account_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.account_summaries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Account ID. |
| `name` | `string` | Account name. |
| `starred` | `boolean` | Indicates whether this account is starred or not. |
| `webProperties` | `array` | List of web properties under this account. |
| `kind` | `string` | Resource type for Analytics AccountSummary. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `management_accountSummaries_list` | `SELECT` |  |
