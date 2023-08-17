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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conversion_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datamigration.conversion_workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Full name of the workspace resource, in the form of: projects/&#123;project&#125;/locations/&#123;location&#125;/conversionWorkspaces/&#123;conversion_workspace&#125;. |
| `hasUncommittedChanges` | `boolean` | Output only. Whether the workspace has uncommitted changes (changes which were made after the workspace was committed). |
| `createTime` | `string` | Output only. The timestamp when the workspace resource was created. |
| `displayName` | `string` | Optional. The display name for the workspace. |
| `updateTime` | `string` | Output only. The timestamp when the workspace resource was last updated. |
| `source` | `object` | The type and version of a source or destination database. |
| `destination` | `object` | The type and version of a source or destination database. |
| `latestCommitTime` | `string` | Output only. The timestamp when the workspace was committed. |
| `latestCommitId` | `string` | Output only. The latest commit ID. |
| `globalSettings` | `object` | Optional. A generic list of settings for the workspace. The settings are database pair dependant and can indicate default behavior for the mapping rules engine or turn on or off specific features. Such examples can be: convert_foreign_key_to_interleave=true, skip_triggers=false, ignore_non_table_synonyms=true |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `conversionWorkspacesId, locationsId, projectsId` | Gets details of a single conversion workspace. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists conversion workspaces in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new conversion workspace in a given project and location. |
| `delete` | `DELETE` | `conversionWorkspacesId, locationsId, projectsId` | Deletes a single conversion workspace. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists conversion workspaces in a given project and location. |
| `apply` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Applies draft tree onto a specific destination database. |
| `commit` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Marks all the data in the conversion workspace as committed. |
| `convert` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Creates a draft tree schema for the destination database. |
| `describe_conversion_workspace_revisions` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Retrieves a list of committed revisions of a specific conversion workspace. |
| `describe_database_entities` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Describes the database entities tree for a specific conversion workspace and a specific tree type. Database entities are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are simple data objects describing the structure of the client database. |
| `patch` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Updates the parameters of a single conversion workspace. |
| `rollback` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Rolls back a conversion workspace to the last committed snapshot. |
| `search_background_jobs` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Searches/lists the background jobs for a specific conversion workspace. The background jobs are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are a way to expose the data plane jobs log. |
| `seed` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Imports a snapshot of the source database into the conversion workspace. |
