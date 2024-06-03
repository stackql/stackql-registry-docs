---
title: license_codes
hide_title: false
hide_table_of_contents: false
keywords:
  - license_codes
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>license_codes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.license_codes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | [Output Only] Name of the resource. The name is 1-20 characters long and must be a valid 64 bit integer. |
| <CopyableCode code="description" /> | `string` | [Output Only] Description of this License Code. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of resource. Always compute#licenseCode for licenses. |
| <CopyableCode code="licenseAlias" /> | `array` | [Output Only] URL and description aliases of Licenses with the same License Code. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="state" /> | `string` | [Output Only] Current state of this License Code. |
| <CopyableCode code="transferable" /> | `boolean` | [Output Only] If true, the license will remain attached when creating images or snapshots from disks. Otherwise, the license is not transferred. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="licenseCode, project" /> |
