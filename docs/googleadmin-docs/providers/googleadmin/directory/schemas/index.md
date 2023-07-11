---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `displayName` | `string` | Display name for the schema. |
| `etag` | `string` | The ETag of the resource. |
| `fields` | `array` | A list of fields in the schema. |
| `kind` | `string` | Kind of resource this is. |
| `schemaId` | `string` | The unique identifier of the schema (Read-only) |
| `schemaName` | `string` | The schema's name. Each `schema_name` must be unique within a customer. Reusing a name results in a `409: Entity already exists` error. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customerId, schemaKey` | Retrieves a schema. |
| `list` | `SELECT` | `customerId` | Retrieves all schemas for a customer. |
| `insert` | `INSERT` | `customerId` | Creates a schema. |
| `delete` | `DELETE` | `customerId, schemaKey` | Deletes a schema. |
| `_list` | `EXEC` | `customerId` | Retrieves all schemas for a customer. |
| `patch` | `EXEC` | `customerId, schemaKey` | Patches a schema. |
| `update` | `EXEC` | `customerId, schemaKey` | Updates a schema. |
