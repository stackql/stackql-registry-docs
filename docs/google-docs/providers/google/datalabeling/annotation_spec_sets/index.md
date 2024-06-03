---
title: annotation_spec_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - annotation_spec_sets
  - datalabeling
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
<tr><td><b>Name</b></td><td><code>annotation_spec_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalabeling.annotation_spec_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The AnnotationSpecSet resource name in the following format: "projects/&#123;project_id&#125;/annotationSpecSets/&#123;annotation_spec_set_id&#125;" |
| <CopyableCode code="description" /> | `string` | Optional. User-provided description of the annotation specification set. The description can be up to 10,000 characters long. |
| <CopyableCode code="annotationSpecs" /> | `array` | Required. The array of AnnotationSpecs that you define when you create the AnnotationSpecSet. These are the possible labels for the labeling task. |
| <CopyableCode code="blockingResources" /> | `array` | Output only. The names of any related resources that are blocking changes to the annotation spec set. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name for AnnotationSpecSet that you define when you create it. Maximum of 64 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_annotation_spec_sets_get" /> | `SELECT` | <CopyableCode code="annotationSpecSetsId, projectsId" /> | Gets an annotation spec set by resource name. |
| <CopyableCode code="projects_annotation_spec_sets_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists annotation spec sets for a project. Pagination is supported. |
| <CopyableCode code="projects_annotation_spec_sets_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an annotation spec set by providing a set of labels. |
| <CopyableCode code="projects_annotation_spec_sets_delete" /> | `DELETE` | <CopyableCode code="annotationSpecSetsId, projectsId" /> | Deletes an annotation spec set by resource name. |
| <CopyableCode code="_projects_annotation_spec_sets_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists annotation spec sets for a project. Pagination is supported. |
