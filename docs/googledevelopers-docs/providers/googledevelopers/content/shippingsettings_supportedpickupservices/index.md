---
title: shippingsettings_supportedpickupservices
hide_title: false
hide_table_of_contents: false
keywords:
  - shippingsettings_supportedpickupservices
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
<tr><td><b>Name</b></td><td><code>shippingsettings_supportedpickupservices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.shippingsettings_supportedpickupservices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#shippingsettingsGetSupportedPickupServicesResponse`". |
| `pickupServices` | `array` | A list of supported pickup services. May be empty. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `shippingsettings_getsupportedpickupservices` | `SELECT` | `merchantId` |
