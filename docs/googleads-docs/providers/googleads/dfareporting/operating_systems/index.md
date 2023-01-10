---
title: operating_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - operating_systems
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
<tr><td><b>Name</b></td><td><code>operating_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.operating_systems</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of this operating system. |
| `mobile` | `boolean` | Whether this operating system is for mobile. |
| `dartId` | `string` | DART ID of this operating system. This is the ID used for targeting. |
| `desktop` | `boolean` | Whether this operating system is for desktop. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#operatingSystem". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `operatingSystems_get` | `SELECT` | `dartId, profileId` | Gets one operating system by DART ID. |
| `operatingSystems_list` | `SELECT` | `profileId` | Retrieves a list of operating systems. |
