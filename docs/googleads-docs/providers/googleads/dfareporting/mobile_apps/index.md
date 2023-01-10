---
title: mobile_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - mobile_apps
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
<tr><td><b>Name</b></td><td><code>mobile_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.mobile_apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this mobile app. |
| `title` | `string` | Title of this mobile app. |
| `directory` | `string` | Mobile app directory. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#mobileApp". |
| `publisherName` | `string` | Publisher name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `mobileApps_get` | `SELECT` | `id, profileId` | Gets one mobile app by ID. |
| `mobileApps_list` | `SELECT` | `profileId` | Retrieves list of available mobile apps. |
