---
title: instances_disk_shrink_config
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_disk_shrink_config
  - sqladmin
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
<tr><td><b>Name</b></td><td><code>instances_disk_shrink_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sqladmin.instances_disk_shrink_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | This is always `sql#getDiskShrinkConfig`. |
| <CopyableCode code="message" /> | `string` | Additional message to customers. |
| <CopyableCode code="minimalTargetSizeGb" /> | `string` | The minimum size to which a disk can be shrunk in GigaBytes. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_disk_shrink_config" /> | `SELECT` | <CopyableCode code="instance, project" /> |
