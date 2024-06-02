---
title: issues
hide_title: false
hide_table_of_contents: false
keywords:
  - issues
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
<tr><td><b>Name</b></td><td><code>issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="contactcenterinsights.issues" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the issue. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/issueModels/&#123;issue_model&#125;/issues/&#123;issue&#125; |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this issue was created. |
| <CopyableCode code="displayName" /> | `string` | The representative name for the issue. |
| <CopyableCode code="sampleUtterances" /> | `array` | Output only. Resource names of the sample representative utterances that match to this issue. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The most recent time that this issue was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="issueModelsId, issuesId, locationsId, projectsId" /> | Gets an issue. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="issueModelsId, locationsId, projectsId" /> | Lists issues. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="issueModelsId, issuesId, locationsId, projectsId" /> | Deletes an issue. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="issueModelsId, issuesId, locationsId, projectsId" /> | Updates an issue. |
