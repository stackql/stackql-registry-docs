---
title: studies
hide_title: false
hide_table_of_contents: false
keywords:
  - studies
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
<tr><td><b>Name</b></td><td><code>studies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.studies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of a study. The study's globally unique identifier. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/studies/&#123;study&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the study was created. |
| <CopyableCode code="displayName" /> | `string` | Required. Describes the Study, default value is empty string. |
| <CopyableCode code="inactiveReason" /> | `string` | Output only. A human readable reason why the Study is inactive. This should be empty if a study is ACTIVE or COMPLETED. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of a Study. |
| <CopyableCode code="studySpec" /> | `object` | Represents specification of a Study. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Gets a Study by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the studies in a region for an associated project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Study. A resource name will be generated after creation of the Study. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Deletes a Study. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all the studies in a region for an associated project. |
| <CopyableCode code="lookup" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Looks a study up using the user-defined display_name field instead of the fully qualified resource name. |
