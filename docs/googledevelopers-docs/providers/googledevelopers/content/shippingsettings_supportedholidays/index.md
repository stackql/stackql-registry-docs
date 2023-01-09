---
title: shippingsettings_supportedholidays
hide_title: false
hide_table_of_contents: false
keywords:
  - shippingsettings_supportedholidays
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
<tr><td><b>Name</b></td><td><code>shippingsettings_supportedholidays</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.shippingsettings_supportedholidays</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `holidays` | `array` | A list of holidays applicable for delivery guarantees. May be empty. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#shippingsettingsGetSupportedHolidaysResponse`". |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `shippingsettings_getsupportedholidays` | `SELECT` | `merchantId` |
