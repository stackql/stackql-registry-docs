---
title: routines
hide_title: false
hide_table_of_contents: false
keywords:
  - routines
  - bigquery
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
<tr><td><b>Name</b></td><td><code>routines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.routines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | Optional. The description of the routine, if defined. |
| `returnType` | `object` | The data type of a variable such as a function argument. Examples include: * INT64: `{"typeKind": "INT64"}` * ARRAY: { "typeKind": "ARRAY", "arrayElementType": {"typeKind": "STRING"} } * STRUCT&gt;: { "typeKind": "STRUCT", "structType": { "fields": [ { "name": "x", "type": {"typeKind: "STRING"} }, { "name": "y", "type": { "typeKind": "ARRAY", "arrayElementType": {"typekind": "DATE"} } } ] } } |
| `etag` | `string` | Output only. A hash of this resource. |
| `definitionBody` | `string` | Required. The body of the routine. For functions, this is the expression in the AS clause. If language=SQL, it is the substring inside (but excluding) the parentheses. For example, for the function created with the following statement: `CREATE FUNCTION JoinLines(x string, y string) as (concat(x, "\n", y))` The definition_body is `concat(x, "\n", y)` (\n is not replaced with linebreak). If language=JAVASCRIPT, it is the evaluated string in the AS clause. For example, for the function created with the following statement: `CREATE FUNCTION f() RETURNS STRING LANGUAGE js AS 'return "\n";\n'` The definition_body is `return "\n";\n` Note that both \n are replaced with linebreaks. |
| `creationTime` | `string` | Output only. The time when this routine was created, in milliseconds since the epoch. |
| `arguments` | `array` | Optional. |
| `lastModifiedTime` | `string` | Output only. The time when this routine was last modified, in milliseconds since the epoch. |
| `importedLibraries` | `array` | Optional. If language = "JAVASCRIPT", this field stores the path of the imported JAVASCRIPT libraries. |
| `remoteFunctionOptions` | `object` | Options for a remote user-defined function. |
| `language` | `string` | Optional. Defaults to "SQL". |
| `determinismLevel` | `string` | Optional. The determinism level of the JavaScript UDF, if defined. |
| `routineReference` | `object` |  |
| `strictMode` | `boolean` | Optional. Can be set for procedures only. If true (default), the definition body will be validated in the creation and the updates of the procedure. For procedures with an argument of ANY TYPE, the definition body validtion is not supported at creation/update time, and thus this field must be set to false explicitly. |
| `returnTableType` | `object` | A table type |
| `routineType` | `string` | Required. The type of routine. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datasetId, projectId, routineId` | Gets the specified routine resource by routine ID. |
| `list` | `SELECT` | `datasetId, projectId` | Lists all routines in the specified dataset. Requires the READER dataset role. |
| `insert` | `INSERT` | `datasetId, projectId` | Creates a new routine in the dataset. |
| `delete` | `DELETE` | `datasetId, projectId, routineId` | Deletes the routine specified by routineId from the dataset. |
| `update` | `EXEC` | `datasetId, projectId, routineId` | Updates information in an existing routine. The update method replaces the entire Routine resource. |
