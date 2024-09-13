---
title: conversion_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - conversion_workspaces
  - datamigration
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

Creates, updates, deletes, gets or lists a <code>conversion_workspaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conversion_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datamigration.conversion_workspaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Full name of the workspace resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the workspace resource was created. |
| <CopyableCode code="destination" /> | `object` | The type and version of a source or destination database. |
| <CopyableCode code="displayName" /> | `string` | Optional. The display name for the workspace. |
| <CopyableCode code="globalSettings" /> | `object` | Optional. A generic list of settings for the workspace. The settings are database pair dependant and can indicate default behavior for the mapping rules engine or turn on or off specific features. Such examples can be: convert_foreign_key_to_interleave=true, skip_triggers=false, ignore_non_table_synonyms=true |
| <CopyableCode code="hasUncommittedChanges" /> | `boolean` | Output only. Whether the workspace has uncommitted changes (changes which were made after the workspace was committed). |
| <CopyableCode code="latestCommitId" /> | `string` | Output only. The latest commit ID. |
| <CopyableCode code="latestCommitTime" /> | `string` | Output only. The timestamp when the workspace was committed. |
| <CopyableCode code="source" /> | `object` | The type and version of a source or destination database. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the workspace resource was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Gets details of a single conversion workspace. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists conversion workspaces in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new conversion workspace in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Deletes a single conversion workspace. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Updates the parameters of a single conversion workspace. |
| <CopyableCode code="apply" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Applies draft tree onto a specific destination database. |
| <CopyableCode code="commit" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Marks all the data in the conversion workspace as committed. |
| <CopyableCode code="convert" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Creates a draft tree schema for the destination database. |
| <CopyableCode code="describe_conversion_workspace_revisions" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Retrieves a list of committed revisions of a specific conversion workspace. |
| <CopyableCode code="describe_database_entities" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Describes the database entities tree for a specific conversion workspace and a specific tree type. Database entities are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are simple data objects describing the structure of the client database. |
| <CopyableCode code="rollback" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Rolls back a conversion workspace to the last committed snapshot. |
| <CopyableCode code="search_background_jobs" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Searches/lists the background jobs for a specific conversion workspace. The background jobs are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are a way to expose the data plane jobs log. |
| <CopyableCode code="seed" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Imports a snapshot of the source database into the conversion workspace. |

## `SELECT` examples

Lists conversion workspaces in a given project and location.

```sql
SELECT
name,
createTime,
destination,
displayName,
globalSettings,
hasUncommittedChanges,
latestCommitId,
latestCommitTime,
source,
updateTime
FROM google.datamigration.conversion_workspaces
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>conversion_workspaces</code> resource.

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
INSERT INTO google.datamigration.conversion_workspaces (
locationsId,
projectsId,
name,
source,
destination,
globalSettings,
hasUncommittedChanges,
latestCommitId,
latestCommitTime,
createTime,
updateTime,
displayName
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ source }}',
'{{ destination }}',
'{{ globalSettings }}',
true|false,
'{{ latestCommitId }}',
'{{ latestCommitTime }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ displayName }}'
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
      - name: source
        value: '{{ source }}'
      - name: destination
        value: '{{ destination }}'
      - name: globalSettings
        value: '{{ globalSettings }}'
      - name: hasUncommittedChanges
        value: '{{ hasUncommittedChanges }}'
      - name: latestCommitId
        value: '{{ latestCommitId }}'
      - name: latestCommitTime
        value: '{{ latestCommitTime }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: displayName
        value: '{{ displayName }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>conversion_workspaces</code> resource.

```sql
/*+ update */
UPDATE google.datamigration.conversion_workspaces
SET 
name = '{{ name }}',
source = '{{ source }}',
destination = '{{ destination }}',
globalSettings = '{{ globalSettings }}',
hasUncommittedChanges = true|false,
latestCommitId = '{{ latestCommitId }}',
latestCommitTime = '{{ latestCommitTime }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
displayName = '{{ displayName }}'
WHERE 
conversionWorkspacesId = '{{ conversionWorkspacesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>conversion_workspaces</code> resource.

```sql
/*+ delete */
DELETE FROM google.datamigration.conversion_workspaces
WHERE conversionWorkspacesId = '{{ conversionWorkspacesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
