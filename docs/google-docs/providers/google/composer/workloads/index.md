---
title: workloads
hide_title: false
hide_table_of_contents: false
keywords:
  - workloads
  - composer
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
<tr><td><b>Name</b></td><td><code>workloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="composer.workloads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of a workload. |
| <CopyableCode code="status" /> | `object` | Workload status. |
| <CopyableCode code="type" /> | `string` | Type of a workload. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentsId, locationsId, projectsId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> |
