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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conversion_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datamigration.conversion_workspaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Full name of the workspace resource, in the form of: projects/&#123;project&#125;/locations/&#123;location&#125;/conversionWorkspaces/&#123;conversion_workspace&#125;. |
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
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists conversion workspaces in a given project and location. |
| <CopyableCode code="apply" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Applies draft tree onto a specific destination database. |
| <CopyableCode code="commit" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Marks all the data in the conversion workspace as committed. |
| <CopyableCode code="convert" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Creates a draft tree schema for the destination database. |
| <CopyableCode code="describe_conversion_workspace_revisions" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Retrieves a list of committed revisions of a specific conversion workspace. |
| <CopyableCode code="describe_database_entities" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Describes the database entities tree for a specific conversion workspace and a specific tree type. Database entities are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are simple data objects describing the structure of the client database. |
| <CopyableCode code="rollback" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Rolls back a conversion workspace to the last committed snapshot. |
| <CopyableCode code="search_background_jobs" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Searches/lists the background jobs for a specific conversion workspace. The background jobs are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are a way to expose the data plane jobs log. |
| <CopyableCode code="seed" /> | `EXEC` | <CopyableCode code="conversionWorkspacesId, locationsId, projectsId" /> | Imports a snapshot of the source database into the conversion workspace. |
