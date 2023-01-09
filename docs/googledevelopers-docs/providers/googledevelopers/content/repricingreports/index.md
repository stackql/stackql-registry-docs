---
title: repricingreports
hide_title: false
hide_table_of_contents: false
keywords:
  - repricingreports
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
<tr><td><b>Name</b></td><td><code>repricingreports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.repricingreports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token for retrieving the next page. Its absence means there is no subsequent page. |
| `repricingProductReports` | `array` | Periodic reports for the given Repricing product. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `productstatuses_repricingreports_list` | `SELECT` | `merchantId, productId` | Lists the metrics report for a given Repricing product. |
| `repricingrules_repricingreports_list` | `SELECT` | `merchantId, ruleId` | Lists the metrics report for a given Repricing rule. |
