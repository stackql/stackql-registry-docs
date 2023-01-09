---
title: platform_types
hide_title: false
hide_table_of_contents: false
keywords:
  - platform_types
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>platform_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.platform_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this platform type. |
| `name` | `string` | Name of this platform type. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#platformType". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `platformTypes_get` | `SELECT` | `id, profileId` | Gets one platform type by ID. |
| `platformTypes_list` | `SELECT` | `profileId` | Retrieves a list of platform types. |
