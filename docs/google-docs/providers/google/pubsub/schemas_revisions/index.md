---
title: schemas_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas_revisions
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
<tr><td><b>Name</b></td><td><code>schemas_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsub.schemas_revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the schema. Format is `projects/&#123;project&#125;/schemas/&#123;schema&#125;`. |
| `definition` | `string` | The definition of the schema. This should contain a string representing the full definition of the schema that is a valid schema definition of the type specified in `type`. |
| `revisionCreateTime` | `string` | Output only. The timestamp that the revision was created. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the schema. |
| `type` | `string` | The type of the schema definition. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_schemas_list_revisions` | `SELECT` | `projectsId, schemasId` |
| `_projects_schemas_list_revisions` | `EXEC` | `projectsId, schemasId` |
