---
title: instances_latest_recovery_time
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_latest_recovery_time
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
<tr><td><b>Name</b></td><td><code>instances_latest_recovery_time</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sqladmin.instances_latest_recovery_time" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | This is always `sql#getLatestRecoveryTime`. |
| <CopyableCode code="latestRecoveryTime" /> | `string` | Timestamp, identifies the latest recovery time of the source instance. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_latest_recovery_time" /> | `SELECT` | <CopyableCode code="instance, project" /> |
