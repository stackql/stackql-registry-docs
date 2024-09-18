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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>phrase_matchers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>phrase_matchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenterinsights.phrase_matchers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the phrase matcher. Format: projects/{project}/locations/{location}/phraseMatchers/{phrase_matcher} |
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

## `SELECT` examples

Lists phrase matchers.

```sql
SELECT
name,
activationUpdateTime,
active,
displayName,
phraseMatchRuleGroups,
revisionCreateTime,
revisionId,
roleMatch,
type,
updateTime,
versionTag
FROM google.contactcenterinsights.phrase_matchers
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>phrase_matchers</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.contactcenterinsights.phrase_matchers (
locationsId,
projectsId,
name,
displayName,
roleMatch,
phraseMatchRuleGroups,
active,
type,
versionTag
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ roleMatch }}',
'{{ phraseMatchRuleGroups }}',
true|false,
'{{ type }}',
'{{ versionTag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
activationUpdateTime: string
name: string
displayName: string
revisionCreateTime: string
roleMatch: string
updateTime: string
phraseMatchRuleGroups:
  - type: string
    phraseMatchRules:
      - query: string
        negated: boolean
        config:
          exactMatchConfig:
            caseSensitive: boolean
revisionId: string
active: boolean
type: string
versionTag: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>phrase_matchers</code> resource.

```sql
/*+ update */
UPDATE google.contactcenterinsights.phrase_matchers
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
roleMatch = '{{ roleMatch }}',
phraseMatchRuleGroups = '{{ phraseMatchRuleGroups }}',
active = true|false,
type = '{{ type }}',
versionTag = '{{ versionTag }}'
WHERE 
locationsId = '{{ locationsId }}'
AND phraseMatchersId = '{{ phraseMatchersId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>phrase_matchers</code> resource.

```sql
/*+ delete */
DELETE FROM google.contactcenterinsights.phrase_matchers
WHERE locationsId = '{{ locationsId }}'
AND phraseMatchersId = '{{ phraseMatchersId }}'
AND projectsId = '{{ projectsId }}';
```
