---
title: settlementreports
hide_title: false
hide_table_of_contents: false
keywords:
  - settlementreports
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
<tr><td><b>Name</b></td><td><code>settlementreports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.settlementreports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `transferDate` | `string` | Date on which transfer for this payment was initiated by Google, in ISO 8601 format. |
| `transferIds` | `array` | The list of bank identifiers used for the transfer. For example, Trace ID for Federal Automated Clearing House (ACH). This may also be known as the Wire ID. |
| `endDate` | `string` | The end date on which all transactions are included in the report, in ISO 8601 format. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#settlementReport`" |
| `previousBalance` | `object` |  |
| `settlementId` | `string` | The ID of the settlement report. |
| `startDate` | `string` | The start date on which all transactions are included in the report, in ISO 8601 format. |
| `transferAmount` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `merchantId, settlementId` | Retrieves a settlement report from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Retrieves a list of settlement reports from your Merchant Center account. |
