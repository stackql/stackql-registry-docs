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
| `unreachable` | `array` | Locations that could not be reached. |
| `conversionWorkspaces` | `array` | The list of conversion workspace objects. |
| `nextPageToken` | `string` | A token which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `conversionWorkspacesId, locationsId, projectsId` | Gets details of a single conversion workspace. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists conversion workspaces in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new conversion workspace in a given project and location. |
| `delete` | `DELETE` | `conversionWorkspacesId, locationsId, projectsId` | Deletes a single conversion workspace. |
| `apply` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Applies draft tree onto a specific destination database. |
| `commit` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Marks all the data in the conversion workspace as committed. |
| `convert` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Creates a draft tree schema for the destination database. |
| `describe_conversion_workspace_revisions` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Retrieves a list of committed revisions of a specific conversion workspace. |
| `describe_database_entities` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Describes the database entities tree for a specific conversion workspace and a specific tree type. Database entities are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are simple data objects describing the structure of the client database. |
| `patch` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Updates the parameters of a single conversion workspace. |
| `rollback` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Rolls back a conversion workspace to the last committed snapshot. |
| `search_background_jobs` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Searches/lists the background jobs for a specific conversion workspace. The background jobs are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are a way to expose the data plane jobs log. |
| `seed` | `EXEC` | `conversionWorkspacesId, locationsId, projectsId` | Imports a snapshot of the source database into the conversion workspace. |
