---
title: specialist_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - specialist_pools
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>specialist_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aiplatform.specialist_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the SpecialistPool. |
| <CopyableCode code="displayName" /> | `string` | Required. The user-defined name of the SpecialistPool. The name can be up to 128 characters long and can consist of any UTF-8 characters. This field should be unique on project-level. |
| <CopyableCode code="pendingDataLabelingJobs" /> | `array` | Output only. The resource name of the pending data labeling jobs. |
| <CopyableCode code="specialistManagerEmails" /> | `array` | The email addresses of the managers in the SpecialistPool. |
| <CopyableCode code="specialistManagersCount" /> | `integer` | Output only. The number of managers in this SpecialistPool. |
| <CopyableCode code="specialistWorkerEmails" /> | `array` | The email addresses of workers in the SpecialistPool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, specialistPoolsId" /> | Gets a SpecialistPool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists SpecialistPools in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a SpecialistPool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, specialistPoolsId" /> | Deletes a SpecialistPool as well as all Specialists in the pool. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists SpecialistPools in a Location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, specialistPoolsId" /> | Updates a SpecialistPool. |
