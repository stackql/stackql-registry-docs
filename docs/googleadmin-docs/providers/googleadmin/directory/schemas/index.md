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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="displayName" /> | `string` | Display name for the schema. |
| <CopyableCode code="etag" /> | `string` | The ETag of the resource. |
| <CopyableCode code="fields" /> | `array` | A list of fields in the schema. |
| <CopyableCode code="kind" /> | `string` | Kind of resource this is. |
| <CopyableCode code="schemaId" /> | `string` | The unique identifier of the schema (Read-only) |
| <CopyableCode code="schemaName" /> | `string` | The schema's name. Each `schema_name` must be unique within a customer. Reusing a name results in a `409: Entity already exists` error. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customerId, schemaKey" /> | Retrieves a schema. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customerId" /> | Retrieves all schemas for a customer. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="customerId" /> | Creates a schema. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customerId, schemaKey" /> | Deletes a schema. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customerId" /> | Retrieves all schemas for a customer. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="customerId, schemaKey" /> | Patches a schema. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="customerId, schemaKey" /> | Updates a schema. |
