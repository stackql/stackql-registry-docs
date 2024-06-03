---
title: phrase_matchers
hide_title: false
hide_table_of_contents: false
keywords:
  - phrase_matchers
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
<tr><td><b>Name</b></td><td><code>phrase_matchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenterinsights.phrase_matchers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the phrase matcher. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/phraseMatchers/&#123;phrase_matcher&#125; |
| <CopyableCode code="activationUpdateTime" /> | `string` | Output only. The most recent time at which the activation status was updated. |
| <CopyableCode code="active" /> | `boolean` | Applies the phrase matcher only when it is active. |
| <CopyableCode code="displayName" /> | `string` | The human-readable name of the phrase matcher. |
| <CopyableCode code="phraseMatchRuleGroups" /> | `array` | A list of phase match rule groups that are included in this matcher. |
| <CopyableCode code="revisionCreateTime" /> | `string` | Output only. The timestamp of when the revision was created. It is also the create time when a new matcher is added. |
| <CopyableCode code="revisionId" /> | `string` | Output only. Immutable. The revision ID of the phrase matcher. A new revision is committed whenever the matcher is changed, except when it is activated or deactivated. A server generated random ID will be used. Example: locations/global/phraseMatchers/my-first-matcher@1234567 |
| <CopyableCode code="roleMatch" /> | `string` | The role whose utterances the phrase matcher should be matched against. If the role is ROLE_UNSPECIFIED it will be matched against any utterances in the transcript. |
| <CopyableCode code="type" /> | `string` | Required. The type of this phrase matcher. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The most recent time at which the phrase matcher was updated. |
| <CopyableCode code="versionTag" /> | `string` | The customized version tag to use for the phrase matcher. If not specified, it will default to `revision_id`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, phraseMatchersId, projectsId" /> | Gets a phrase matcher. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists phrase matchers. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a phrase matcher. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, phraseMatchersId, projectsId" /> | Deletes a phrase matcher. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, phraseMatchersId, projectsId" /> | Updates a phrase matcher. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists phrase matchers. |
