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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>phrase_matchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.phrase_matchers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the phrase matcher. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/phraseMatchers/&#123;phrase_matcher&#125; |
| `revisionCreateTime` | `string` | Output only. The timestamp of when the revision was created. It is also the create time when a new matcher is added. |
| `updateTime` | `string` | Output only. The most recent time at which the phrase matcher was updated. |
| `activationUpdateTime` | `string` | Output only. The most recent time at which the activation status was updated. |
| `displayName` | `string` | The human-readable name of the phrase matcher. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the phrase matcher. A new revision is committed whenever the matcher is changed, except when it is activated or deactivated. A server generated random ID will be used. Example: locations/global/phraseMatchers/my-first-matcher@1234567 |
| `type` | `string` | Required. The type of this phrase matcher. |
| `phraseMatchRuleGroups` | `array` | A list of phase match rule groups that are included in this matcher. |
| `roleMatch` | `string` | The role whose utterances the phrase matcher should be matched against. If the role is ROLE_UNSPECIFIED it will be matched against any utterances in the transcript. |
| `versionTag` | `string` | The customized version tag to use for the phrase matcher. If not specified, it will default to `revision_id`. |
| `active` | `boolean` | Applies the phrase matcher only when it is active. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, phraseMatchersId, projectsId` | Gets a phrase matcher. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists phrase matchers. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a phrase matcher. |
| `delete` | `DELETE` | `locationsId, phraseMatchersId, projectsId` | Deletes a phrase matcher. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists phrase matchers. |
| `patch` | `EXEC` | `locationsId, phraseMatchersId, projectsId` | Updates a phrase matcher. |
