---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
  - pubsub
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
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsub.schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the schema. Format is `projects/&#123;project&#125;/schemas/&#123;schema&#125;`. |
| `revisionCreateTime` | `string` | Output only. The timestamp that the revision was created. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the schema. |
| `type` | `string` | The type of the schema definition. |
| `definition` | `string` | The definition of the schema. This should contain a string representing the full definition of the schema that is a valid schema definition of the type specified in `type`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_schemas_get` | `SELECT` | `projectsId, schemasId` | Gets a schema. |
| `projects_schemas_list` | `SELECT` | `projectsId` | Lists schemas in a project. |
| `projects_schemas_create` | `INSERT` | `projectsId` | Creates a schema. |
| `projects_schemas_delete` | `DELETE` | `projectsId, schemasId` | Deletes a schema. |
| `projects_schemas_commit` | `EXEC` | `projectsId, schemasId` | Commits a new schema revision to an existing schema. |
| `projects_schemas_rollback` | `EXEC` | `projectsId, schemasId` | Creates a new schema revision that is a copy of the provided revision_id. |
| `projects_schemas_validate` | `EXEC` | `projectsId` | Validates a schema. |
| `projects_schemas_validate_message` | `EXEC` | `projectsId` | Validates a message against a schema. |
