---
title: webfonts
hide_title: false
hide_table_of_contents: false
keywords:
  - webfonts
  - webfonts
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
<tr><td><b>Name</b></td><td><code>webfonts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.webfonts.webfonts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `variants` | `array` | The available variants for the font. |
| `version` | `string` | The font version. |
| `category` | `string` | The category of the font. |
| `family` | `string` | The name of the font. |
| `files` | `object` | The font files (with all supported scripts) for each one of the available variants, as a key : value map. |
| `kind` | `string` | This kind represents a webfont object in the webfonts service. |
| `lastModified` | `string` | The date (format "yyyy-MM-dd") the font was modified for the last time. |
| `subsets` | `array` | The scripts supported by the font. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
