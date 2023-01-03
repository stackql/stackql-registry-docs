---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - datastore
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datastore.projects</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `allocateIds` | `EXEC` | `projectId` | Allocates IDs for the given keys, which is useful for referencing an entity before it is inserted. |
| `beginTransaction` | `EXEC` | `projectId` | Begins a new transaction. |
| `commit` | `EXEC` | `projectId` | Commits a transaction, optionally creating, deleting or modifying some entities. |
| `export` | `EXEC` | `projectId` | Exports a copy of all or a subset of entities from Google Cloud Datastore to another storage system, such as Google Cloud Storage. Recent updates to entities may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage. |
| `import` | `EXEC` | `projectId` | Imports entities into Google Cloud Datastore. Existing entities with the same key are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportEntities operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Datastore. |
| `lookup` | `EXEC` | `projectId` | Looks up entities by key. |
| `reserveIds` | `EXEC` | `projectId` | Prevents the supplied keys' IDs from being auto-allocated by Cloud Datastore. |
| `rollback` | `EXEC` | `projectId` | Rolls back a transaction. |
| `runQuery` | `EXEC` | `projectId` | Queries for entities. |
