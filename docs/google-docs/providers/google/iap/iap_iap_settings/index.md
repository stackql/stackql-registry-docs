---
title: iap_iap_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - iap_iap_settings
  - iap
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iap_iap_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iap.iap_iap_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the IAP protected resource. |
| `accessSettings` | `object` | Access related settings for IAP protected apps. |
| `applicationSettings` | `object` | Wrapper over application specific settings for IAP. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_iap_settings` | `SELECT` | `v1Id` | Gets the IAP settings on a particular IAP protected resource. |
| `update_iap_settings` | `EXEC` | `v1Id` | Updates the IAP settings on a particular IAP protected resource. It replaces all fields unless the `update_mask` is set. |
