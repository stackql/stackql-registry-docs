---
title: feature_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_groups
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
<tr><td><b>Name</b></td><td><code>feature_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.feature_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the FeatureGroup. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/featureGroups/&#123;featureGroup&#125;` |
| <CopyableCode code="description" /> | `string` | Optional. Description of the FeatureGroup. |
| <CopyableCode code="bigQuery" /> | `object` | Input source type for BigQuery Tables and Views. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this FeatureGroup was created. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize your FeatureGroup. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureGroup(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this FeatureGroup was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureGroupsId, locationsId, projectsId" /> | Gets details of a single FeatureGroup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists FeatureGroups in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new FeatureGroup in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="featureGroupsId, locationsId, projectsId" /> | Deletes a single FeatureGroup. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="featureGroupsId, locationsId, projectsId" /> | Updates the parameters of a single FeatureGroup. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists FeatureGroups in a given project and location. |
