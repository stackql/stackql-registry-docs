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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `returnType` | `object` | The data type of a variable such as a function argument. Examples include: * INT64: `&#123;"typeKind": "INT64"&#125;` * ARRAY: &#123; "typeKind": "ARRAY", "arrayElementType": &#123;"typeKind": "STRING"&#125; &#125; * STRUCT&gt;: &#123; "typeKind": "STRUCT", "structType": &#123; "fields": [ &#123; "name": "x", "type": &#123;"typeKind": "STRING"&#125; &#125;, &#123; "name": "y", "type": &#123; "typeKind": "ARRAY", "arrayElementType": &#123;"typeKind": "DATE"&#125; &#125; &#125; ] &#125; &#125; |
| `importedLibraries` | `array` | Optional. If language = "JAVASCRIPT", this field stores the path of the imported JAVASCRIPT libraries. |
| `language` | `string` | Optional. Defaults to "SQL" if remote_function_options field is absent, not set otherwise. |
| `strictMode` | `boolean` | Optional. Can be set for procedures only. If true (default), the definition body will be validated in the creation and the updates of the procedure. For procedures with an argument of ANY TYPE, the definition body validtion is not supported at creation/update time, and thus this field must be set to false explicitly. |
| `returnTableType` | `object` | A table type |
| `routineType` | `string` | Required. The type of routine. |
| `definitionBody` | `string` | Required. The body of the routine. For functions, this is the expression in the AS clause. If language=SQL, it is the substring inside (but excluding) the parentheses. For example, for the function created with the following statement: `CREATE FUNCTION JoinLines(x string, y string) as (concat(x, "\n", y))` The definition_body is `concat(x, "\n", y)` (\n is not replaced with linebreak). If language=JAVASCRIPT, it is the evaluated string in the AS clause. For example, for the function created with the following statement: `CREATE FUNCTION f() RETURNS STRING LANGUAGE js AS 'return "\n";\n'` The definition_body is `return "\n";\n` Note that both \n are replaced with linebreaks. |
| `lastModifiedTime` | `string` | Output only. The time when this routine was last modified, in milliseconds since the epoch. |
| `creationTime` | `string` | Output only. The time when this routine was created, in milliseconds since the epoch. |
| `routineReference` | `object` |  |
| `sparkOptions` | `object` | Options for a user-defined Spark routine. |
| `determinismLevel` | `string` | Optional. The determinism level of the JavaScript UDF, if defined. |
| `etag` | `string` | Output only. A hash of this resource. |
| `arguments` | `array` | Optional. |
| `remoteFunctionOptions` | `object` | Options for a remote user-defined function. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `+datasetId, +routineId, projectId` | Gets the specified routine resource by routine ID. |
| `list` | `SELECT` | `+datasetId, projectId` | Lists all routines in the specified dataset. Requires the READER dataset role. |
| `insert` | `INSERT` | `+datasetId, projectId` | Creates a new routine in the dataset. |
| `delete` | `DELETE` | `+datasetId, +routineId, projectId` | Deletes the routine specified by routineId from the dataset. |
| `_list` | `EXEC` | `+datasetId, projectId` | Lists all routines in the specified dataset. Requires the READER dataset role. |
| `update` | `EXEC` | `+datasetId, +routineId, projectId` | Updates information in an existing routine. The update method replaces the entire Routine resource. |
