---
title: region_instance_group_managers_errors
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instance_group_managers_errors
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
<tr><td><b>Name</b></td><td><code>region_instance_group_managers_errors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_instance_group_managers_errors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="error" /> | `object` |  |
| <CopyableCode code="instanceActionDetails" /> | `object` |  |
| <CopyableCode code="timestamp" /> | `string` | [Output Only] The time that this error occurred. This value is in RFC3339 text format. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_errors" /> | `SELECT` | <CopyableCode code="instanceGroupManager, project, region" /> |
