---
title: variants
hide_title: false
hide_table_of_contents: false
keywords:
  - variants
  - androidpublisher
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
<tr><td><b>Name</b></td><td><code>variants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.variants</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `deviceSpec` | `object` | The device spec used to generate a system APK. |
| `variantId` | `integer` | Output only. The ID of a previously created system APK variant. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `systemapks_variants_get` | `SELECT` | `packageName, variantId, versionCode` | Returns a previously created system APK variant. |
| `systemapks_variants_list` | `SELECT` | `packageName, versionCode` | Returns the list of previously created system APK variants. |
| `systemapks_variants_create` | `INSERT` | `packageName, versionCode` | Creates an APK which is suitable for inclusion in a system image from an already uploaded Android App Bundle. |
| `systemapks_variants_download` | `EXEC` | `packageName, variantId, versionCode` | Downloads a previously created system APK which is suitable for inclusion in a system image. |
