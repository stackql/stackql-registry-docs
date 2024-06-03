---
title: storage_pools_disks
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_pools_disks
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
<tr><td><b>Name</b></td><td><code>storage_pools_disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.storage_pools_disks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | [Output Only] The name of the disk. |
| <CopyableCode code="attachedInstances" /> | `array` | [Output Only] Instances this disk is attached to. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="disk" /> | `string` | [Output Only] The URL of the disk. |
| <CopyableCode code="provisionedIops" /> | `string` | [Output Only] The number of IOPS provisioned for the disk. |
| <CopyableCode code="provisionedThroughput" /> | `string` | [Output Only] The throughput provisioned for the disk. |
| <CopyableCode code="resourcePolicies" /> | `array` | [Output Only] Resource policies applied to disk for automatic snapshot creations. |
| <CopyableCode code="sizeGb" /> | `string` | [Output Only] The disk size, in GB. |
| <CopyableCode code="status" /> | `string` | [Output Only] The disk status. |
| <CopyableCode code="type" /> | `string` | [Output Only] The disk type. |
| <CopyableCode code="usedBytes" /> | `string` | [Output Only] Amount of disk space used. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_disks" /> | `SELECT` | <CopyableCode code="project, storagePool, zone" /> |
