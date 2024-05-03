---
title: studies
hide_title: false
hide_table_of_contents: false
keywords:
  - studies
  - ml
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.ml.studies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of a study. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the study was created. |
| <CopyableCode code="inactiveReason" /> | `string` | Output only. A human readable reason why the Study is inactive. This should be empty if a study is ACTIVE or COMPLETED. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of a study. |
| <CopyableCode code="studyConfig" /> | `object` | Represents configuration of a study. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_studies_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Gets a study. |
| <CopyableCode code="projects_locations_studies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the studies in a region for an associated project. |
| <CopyableCode code="projects_locations_studies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a study. |
| <CopyableCode code="projects_locations_studies_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, studiesId" /> | Deletes a study. |
