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
| `displayName` | `string` | The display name for the workspace |
| `createTime` | `string` | Output only. The timestamp when the workspace resource was created. |
| `updateTime` | `string` | Output only. The timestamp when the workspace resource was last updated. |
| `source` | `object` | The type and version of a source or destination DB. |
| `globalSettings` | `object` | A generic list of settings for the workspace. The settings are database pair dependant and can indicate default behavior for the mapping rules engine or turn on or off specific features. Such examples can be: convert_foreign_key_to_interleave=true, skip_triggers=false, ignore_non_table_synonyms=true |
| `hasUncommittedChanges` | `boolean` | Output only. Whether the workspace has uncommitted changes (changes which were made after the workspace was committed) |
| `destination` | `object` | The type and version of a source or destination DB. |
| `latestCommitId` | `string` | Output only. The latest commit id |
| `latestCommitTime` | `string` | Output only. The timestamp when the workspace was committed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_conversionWorkspaces_get` | `SELECT` | `conversionWorkspacesId, locationsId, projectsId` | Gets details of a single conversion workspace. |
| `projects_locations_conversionWorkspaces_list` | `SELECT` | `locationsId, projectsId` | Lists conversion workspaces in a given project and location. |
| `projects_locations_conversionWorkspaces_create` | `INSERT` | `locationsId, projectsId` | Creates a new conversion workspace in a given project and location. |
| `projects_locations_conversionWorkspaces_delete` | `DELETE` | `conversionWorkspacesId, locationsId, projectsId` | Deletes a single conversion workspace. |
| `projects_locations_conversionWorkspaces_apply` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Apply draft tree onto a specific destination database |
| `projects_locations_conversionWorkspaces_commit` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Marks all the data in the conversion workspace as committed. |
| `projects_locations_conversionWorkspaces_convert` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Creates a draft tree schema for the destination database. |
| `projects_locations_conversionWorkspaces_describeConversionWorkspaceRevisions` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Retrieves a list of committed revisions of a specific conversion workspace. |
| `projects_locations_conversionWorkspaces_describeDatabaseEntities` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Use this method to describe the database entities tree for a specific conversion workspace and a specific tree type. The DB Entities are not a resource like conversion workspace or mapping rule, and they can not be created, updated or deleted like one. Instead they are simple data objects describing the structure of the client database. |
| `projects_locations_conversionWorkspaces_patch` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Updates the parameters of a single conversion workspace. |
| `projects_locations_conversionWorkspaces_rollback` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Rollbacks a conversion workspace to the last committed spanshot. |
| `projects_locations_conversionWorkspaces_searchBackgroundJobs` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Use this method to search/list the background jobs for a specific conversion workspace. The background jobs are not a resource like conversion workspace or mapping rule, and they can not be created, updated or deleted like one. Instead they are a way to expose the data plane jobs log. |
| `projects_locations_conversionWorkspaces_seed` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Imports a snapshot of the source database into the conversion workspace. |
