---
title: release_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - release_configs
  - dataform
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

Creates, updates, deletes, gets or lists a <code>release_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>release_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.release_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The release config's name. |
| <CopyableCode code="codeCompilationConfig" /> | `object` | Configures various aspects of Dataform code compilation. |
| <CopyableCode code="cronSchedule" /> | `string` | Optional. Optional schedule (in cron format) for automatic creation of compilation results. |
| <CopyableCode code="disabled" /> | `boolean` | Optional. Disables automatic creation of compilation results. |
| <CopyableCode code="gitCommitish" /> | `string` | Required. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples: - a commit SHA: `12ade345` - a tag: `tag1` - a branch name: `branch1` |
| <CopyableCode code="recentScheduledReleaseRecords" /> | `array` | Output only. Records of the 10 most recent scheduled release attempts, ordered in in descending order of `release_time`. Updated whenever automatic creation of a compilation result is triggered by cron_schedule. |
| <CopyableCode code="releaseCompilationResult" /> | `string` | Optional. The name of the currently released compilation result for this release config. This value is updated when a compilation result is automatically created from this release config (using cron_schedule), or when this resource is updated by API call (perhaps to roll back to an earlier release). The compilation result must have been created using this release config. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`. |
| <CopyableCode code="timeZone" /> | `string` | Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, releaseConfigsId, repositoriesId" /> | Fetches a single ReleaseConfig. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Lists ReleaseConfigs in a given Repository. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Creates a new ReleaseConfig in a given Repository. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, releaseConfigsId, repositoriesId" /> | Deletes a single ReleaseConfig. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, releaseConfigsId, repositoriesId" /> | Updates a single ReleaseConfig. |

## `SELECT` examples

Lists ReleaseConfigs in a given Repository.

```sql
SELECT
name,
codeCompilationConfig,
cronSchedule,
disabled,
gitCommitish,
recentScheduledReleaseRecords,
releaseCompilationResult,
timeZone
FROM google.dataform.release_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>release_configs</code> resource.

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
INSERT INTO google.dataform.release_configs (
locationsId,
projectsId,
repositoriesId,
name,
gitCommitish,
codeCompilationConfig,
cronSchedule,
timeZone,
recentScheduledReleaseRecords,
releaseCompilationResult,
disabled
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ repositoriesId }}',
'{{ name }}',
'{{ gitCommitish }}',
'{{ codeCompilationConfig }}',
'{{ cronSchedule }}',
'{{ timeZone }}',
'{{ recentScheduledReleaseRecords }}',
'{{ releaseCompilationResult }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: gitCommitish
        value: '{{ gitCommitish }}'
      - name: codeCompilationConfig
        value: '{{ codeCompilationConfig }}'
      - name: cronSchedule
        value: '{{ cronSchedule }}'
      - name: timeZone
        value: '{{ timeZone }}'
      - name: recentScheduledReleaseRecords
        value: '{{ recentScheduledReleaseRecords }}'
      - name: releaseCompilationResult
        value: '{{ releaseCompilationResult }}'
      - name: disabled
        value: '{{ disabled }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>release_configs</code> resource.

```sql
/*+ update */
UPDATE google.dataform.release_configs
SET 
name = '{{ name }}',
gitCommitish = '{{ gitCommitish }}',
codeCompilationConfig = '{{ codeCompilationConfig }}',
cronSchedule = '{{ cronSchedule }}',
timeZone = '{{ timeZone }}',
recentScheduledReleaseRecords = '{{ recentScheduledReleaseRecords }}',
releaseCompilationResult = '{{ releaseCompilationResult }}',
disabled = true|false
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND releaseConfigsId = '{{ releaseConfigsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```

## `DELETE` example

Deletes the specified <code>release_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataform.release_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND releaseConfigsId = '{{ releaseConfigsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```
