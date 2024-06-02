---
title: answers
hide_title: false
hide_table_of_contents: false
keywords:
  - answers
  - discoveryengine
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
<tr><td><b>Name</b></td><td><code>answers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="discoveryengine.answers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Fully qualified name `projects/&#123;project&#125;/locations/global/collections/&#123;collection&#125;/engines/&#123;engine&#125;/sessions/*/answers/*` |
| <CopyableCode code="answerSkippedReasons" /> | `array` | Additional answer-skipped reasons. This provides the reason for ignored cases. If nothing is skipped, this field is not set. |
| <CopyableCode code="answerText" /> | `string` | The textual answer. |
| <CopyableCode code="citations" /> | `array` | Citations. |
| <CopyableCode code="completeTime" /> | `string` | Output only. Answer completed timestamp. |
| <CopyableCode code="createTime" /> | `string` | Output only. Answer creation timestamp. |
| <CopyableCode code="queryUnderstandingInfo" /> | `object` | Query understanding information. |
| <CopyableCode code="references" /> | `array` | References. |
| <CopyableCode code="relatedQuestions" /> | `array` | Suggested related questions. |
| <CopyableCode code="state" /> | `string` | The state of the answer generation. |
| <CopyableCode code="steps" /> | `array` | Answer generation steps. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_collections_data_stores_sessions_answers_get" /> | `SELECT` | <CopyableCode code="answersId, collectionsId, dataStoresId, locationsId, projectsId, sessionsId" /> |
| <CopyableCode code="projects_locations_collections_engines_sessions_answers_get" /> | `SELECT` | <CopyableCode code="answersId, collectionsId, enginesId, locationsId, projectsId, sessionsId" /> |
| <CopyableCode code="projects_locations_data_stores_sessions_answers_get" /> | `SELECT` | <CopyableCode code="answersId, dataStoresId, locationsId, projectsId, sessionsId" /> |
