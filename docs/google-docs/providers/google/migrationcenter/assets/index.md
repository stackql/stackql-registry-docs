---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
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
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="migrationcenter.assets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full name of the asset. |
| <CopyableCode code="assignedGroups" /> | `array` | Output only. The list of groups that the asset is assigned to. |
| <CopyableCode code="attributes" /> | `object` | Generic asset attributes. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the asset was created. |
| <CopyableCode code="insightList" /> | `object` | Message containing insights list. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs. |
| <CopyableCode code="machineDetails" /> | `object` | Details of a machine. |
| <CopyableCode code="performanceData" /> | `object` | Performance data for an asset. |
| <CopyableCode code="sources" /> | `array` | Output only. The list of sources contributing to the asset. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the asset was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assetsId, locationsId, projectsId" /> | Gets the details of an asset. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the assets in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assetsId, locationsId, projectsId" /> | Deletes an asset. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all the assets in a given project and location. |
| <CopyableCode code="aggregate_values" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Aggregates the requested fields based on provided function. |
| <CopyableCode code="batch_delete" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Deletes list of Assets. |
| <CopyableCode code="batch_update" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Updates the parameters of a list of assets. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="assetsId, locationsId, projectsId" /> | Updates the parameters of an asset. |
| <CopyableCode code="report_asset_frames" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Reports a set of frames. |
