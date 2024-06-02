---
title: analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - analyses
  - contactcenterinsights
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
<tr><td><b>Name</b></td><td><code>analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="contactcenterinsights.analyses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the analysis. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/conversations/&#123;conversation&#125;/analyses/&#123;analysis&#125; |
| <CopyableCode code="analysisResult" /> | `object` | The result of an analysis. |
| <CopyableCode code="annotatorSelector" /> | `object` | Selector of all available annotators and phrase matchers to run. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the analysis was created, which occurs when the long-running operation completes. |
| <CopyableCode code="requestTime" /> | `string` | Output only. The time at which the analysis was requested. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="analysesId, conversationsId, locationsId, projectsId" /> | Gets an analysis. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Lists analyses. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Creates an analysis. The long running operation is done when the analysis has completed. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="analysesId, conversationsId, locationsId, projectsId" /> | Deletes an analysis. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Lists analyses. |
