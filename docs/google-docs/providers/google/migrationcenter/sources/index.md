---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
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
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="migrationcenter.sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full name of the source. |
| <CopyableCode code="description" /> | `string` | Free-text description. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the source was created. |
| <CopyableCode code="displayName" /> | `string` | User-friendly display name. |
| <CopyableCode code="errorFrameCount" /> | `integer` | Output only. The number of frames that were reported by the source and contained errors. |
| <CopyableCode code="managed" /> | `boolean` | If `true`, the source is managed by other service(s). |
| <CopyableCode code="pendingFrameCount" /> | `integer` | Output only. Number of frames that are still being processed. |
| <CopyableCode code="priority" /> | `integer` | The information confidence of the source. The higher the value, the higher the confidence. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the source. |
| <CopyableCode code="type" /> | `string` | Data source type. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the source was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Gets the details of a source. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the sources in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new source in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Deletes a source. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all the sources in a given project and location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Updates the parameters of a source. |
