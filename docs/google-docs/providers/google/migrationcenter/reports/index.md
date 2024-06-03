---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - migrationcenter
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
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of resource. |
| <CopyableCode code="description" /> | `string` | Free-text description. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation timestamp. |
| <CopyableCode code="displayName" /> | `string` | User-friendly display name. Maximum length is 63 characters. |
| <CopyableCode code="state" /> | `string` | Report creation state. |
| <CopyableCode code="summary" /> | `object` | Describes the Summary view of a Report, which contains aggregated values for all the groups and preference sets included in this Report. |
| <CopyableCode code="type" /> | `string` | Report type. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reportConfigsId, reportsId" /> | Gets details of a single Report. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reportConfigsId" /> | Lists Reports in a given ReportConfig. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, reportConfigsId" /> | Creates a report. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, reportConfigsId, reportsId" /> | Deletes a Report. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, reportConfigsId" /> | Lists Reports in a given ReportConfig. |
