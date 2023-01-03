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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Required. Name of the schema. Format is `projects/{project}/schemas/{schema}`. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the schema. |
| `type` | `string` | The type of the schema definition. |
| `definition` | `string` | The definition of the schema. This should contain a string representing the full definition of the schema that is a valid schema definition of the type specified in `type`. |
| `revisionCreateTime` | `string` | Output only. The timestamp that the revision was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_schemas_get` | `SELECT` | `projectsId, schemasId` | Gets a schema. |
| `projects_schemas_list` | `SELECT` | `projectsId` | Lists schemas in a project. |
| `projects_schemas_create` | `INSERT` | `projectsId` | Creates a schema. |
| `projects_schemas_delete` | `DELETE` | `projectsId, schemasId` | Deletes a schema. |
| `projects_schemas_validate` | `EXEC` | `projectsId` | Validates a schema. |
| `projects_schemas_validateMessage` | `EXEC` | `projectsId` | Validates a message against a schema. |
