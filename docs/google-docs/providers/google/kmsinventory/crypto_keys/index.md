---
title: crypto_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - crypto_keys
  - kmsinventory
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
<tr><td><b>Name</b></td><td><code>crypto_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.kmsinventory.crypto_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `cryptoKeys` | `array` | The list of CryptoKeys. |
| `nextPageToken` | `string` | The page token returned from the previous response if the next page is desired. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_cryptoKeys_list` | `SELECT` | `projectsId` |
