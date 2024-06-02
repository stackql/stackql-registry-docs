---
title: stats
hide_title: false
hide_table_of_contents: false
keywords:
  - stats
  - apigee
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
<tr><td><b>Name</b></td><td><code>stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.stats" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="environments" /> | `array` | List of query results on the environment level. |
| <CopyableCode code="hosts" /> | `array` | List of query results grouped by host. |
| <CopyableCode code="metaData" /> | `object` | Encapsulates additional information about query execution. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="organizations_environments_stats_get" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, statsId" /> |
