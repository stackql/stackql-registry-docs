---
title: iap_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - iap_settings
  - iap
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iap_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iap.iap_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the IAP protected resource. |
| `applicationSettings` | `object` | Wrapper over application specific settings for IAP. |
| `accessSettings` | `object` | Access related settings for IAP protected apps. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getIapSettings` | `SELECT` | `v1Id` |
