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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pubsub.schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the schema. Format is `projects/&#123;project&#125;/schemas/&#123;schema&#125;`. |
| <CopyableCode code="definition" /> | `string` | The definition of the schema. This should contain a string representing the full definition of the schema that is a valid schema definition of the type specified in `type`. |
| <CopyableCode code="revisionCreateTime" /> | `string` | Output only. The timestamp that the revision was created. |
| <CopyableCode code="revisionId" /> | `string` | Output only. Immutable. The revision ID of the schema. |
| <CopyableCode code="type" /> | `string` | The type of the schema definition. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_schemas_get" /> | `SELECT` | <CopyableCode code="projectsId, schemasId" /> | Gets a schema. |
| <CopyableCode code="projects_schemas_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists schemas in a project. |
| <CopyableCode code="projects_schemas_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a schema. |
| <CopyableCode code="projects_schemas_delete" /> | `DELETE` | <CopyableCode code="projectsId, schemasId" /> | Deletes a schema. |
| <CopyableCode code="_projects_schemas_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists schemas in a project. |
| <CopyableCode code="projects_schemas_commit" /> | `EXEC` | <CopyableCode code="projectsId, schemasId" /> | Commits a new schema revision to an existing schema. |
| <CopyableCode code="projects_schemas_rollback" /> | `EXEC` | <CopyableCode code="projectsId, schemasId" /> | Creates a new schema revision that is a copy of the provided revision_id. |
| <CopyableCode code="projects_schemas_validate" /> | `EXEC` | <CopyableCode code="projectsId" /> | Validates a schema. |
| <CopyableCode code="projects_schemas_validate_message" /> | `EXEC` | <CopyableCode code="projectsId" /> | Validates a message against a schema. |
