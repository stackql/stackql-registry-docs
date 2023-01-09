---
title: operating_system_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - operating_system_versions
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
<tr><td><b>Name</b></td><td><code>operating_system_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.operating_system_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this operating system version. |
| `name` | `string` | Name of this operating system version. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#operatingSystemVersion". |
| `majorVersion` | `string` | Major version (leftmost number) of this operating system version. |
| `minorVersion` | `string` | Minor version (number after the first dot) of this operating system version. |
| `operatingSystem` | `object` | Contains information about an operating system that can be targeted by ads. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `operatingSystemVersions_get` | `SELECT` | `id, profileId` | Gets one operating system version by ID. |
| `operatingSystemVersions_list` | `SELECT` | `profileId` | Retrieves a list of operating system versions. |
