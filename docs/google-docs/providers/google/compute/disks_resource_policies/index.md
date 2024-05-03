---
title: disks_resource_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - disks_resource_policies
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
<tr><td><b>Name</b></td><td><code>disks_resource_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.disks_resource_policies" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_resource_policies" /> | `EXEC` | <CopyableCode code="disk, project, zone" /> | Adds existing resource policies to a disk. You can only add one policy which will be applied to this disk for scheduling snapshot creation. |
| <CopyableCode code="remove_resource_policies" /> | `EXEC` | <CopyableCode code="disk, project, zone" /> | Removes resource policies from a disk. |
