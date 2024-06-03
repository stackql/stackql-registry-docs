---
title: datacollectors
hide_title: false
hide_table_of_contents: false
keywords:
  - datacollectors
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
<tr><td><b>Name</b></td><td><code>datacollectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.datacollectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | ID of the data collector. Must begin with `dc_`. |
| <CopyableCode code="description" /> | `string` | A description of the data collector. |
| <CopyableCode code="createdAt" /> | `string` | Output only. The time at which the data collector was created in milliseconds since the epoch. |
| <CopyableCode code="lastModifiedAt" /> | `string` | Output only. The time at which the Data Collector was last updated in milliseconds since the epoch. |
| <CopyableCode code="type" /> | `string` | Immutable. The type of data this data collector will collect. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_datacollectors_get" /> | `SELECT` | <CopyableCode code="datacollectorsId, organizationsId" /> | Gets a data collector. |
| <CopyableCode code="organizations_datacollectors_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all data collectors. |
| <CopyableCode code="organizations_datacollectors_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a new data collector. |
| <CopyableCode code="organizations_datacollectors_delete" /> | `DELETE` | <CopyableCode code="datacollectorsId, organizationsId" /> | Deletes a data collector. |
| <CopyableCode code="organizations_datacollectors_patch" /> | `UPDATE` | <CopyableCode code="datacollectorsId, organizationsId" /> | Updates a data collector. |
| <CopyableCode code="_organizations_datacollectors_list" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Lists all data collectors. |
