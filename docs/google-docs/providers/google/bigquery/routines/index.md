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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="bigquery.routines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | Optional. The description of the routine, if defined. |
| <CopyableCode code="arguments" /> | `array` | Optional. |
| <CopyableCode code="creationTime" /> | `string` | Output only. The time when this routine was created, in milliseconds since the epoch. |
| <CopyableCode code="dataGovernanceType" /> | `string` | Optional. If set to `DATA_MASKING`, the function is validated and made available as a masking function. For more information, see [Create custom masking routines](https://cloud.google.com/bigquery/docs/user-defined-functions#custom-mask). |
| <CopyableCode code="definitionBody" /> | `string` | Required. The body of the routine. For functions, this is the expression in the AS clause. If language=SQL, it is the substring inside (but excluding) the parentheses. For example, for the function created with the following statement: `CREATE FUNCTION JoinLines(x string, y string) as (concat(x, "\n", y))` The definition_body is `concat(x, "\n", y)` (\n is not replaced with linebreak). If language=JAVASCRIPT, it is the evaluated string in the AS clause. For example, for the function created with the following statement: `CREATE FUNCTION f() RETURNS STRING LANGUAGE js AS 'return "\n";\n'` The definition_body is `return "\n";\n` Note that both \n are replaced with linebreaks. |
| <CopyableCode code="determinismLevel" /> | `string` | Optional. The determinism level of the JavaScript UDF, if defined. |
| <CopyableCode code="etag" /> | `string` | Output only. A hash of this resource. |
| <CopyableCode code="importedLibraries" /> | `array` | Optional. If language = "JAVASCRIPT", this field stores the path of the imported JAVASCRIPT libraries. |
| <CopyableCode code="language" /> | `string` | Optional. Defaults to "SQL" if remote_function_options field is absent, not set otherwise. |
| <CopyableCode code="lastModifiedTime" /> | `string` | Output only. The time when this routine was last modified, in milliseconds since the epoch. |
| <CopyableCode code="remoteFunctionOptions" /> | `object` | Options for a remote user-defined function. |
| <CopyableCode code="returnTableType" /> | `object` | A table type |
| <CopyableCode code="returnType" /> | `object` | The data type of a variable such as a function argument. Examples include: * INT64: `&#123;"typeKind": "INT64"&#125;` * ARRAY: &#123; "typeKind": "ARRAY", "arrayElementType": &#123;"typeKind": "STRING"&#125; &#125; * STRUCT&gt;: &#123; "typeKind": "STRUCT", "structType": &#123; "fields": [ &#123; "name": "x", "type": &#123;"typeKind": "STRING"&#125; &#125;, &#123; "name": "y", "type": &#123; "typeKind": "ARRAY", "arrayElementType": &#123;"typeKind": "DATE"&#125; &#125; &#125; ] &#125; &#125; |
| <CopyableCode code="routineReference" /> | `object` | Id path of a routine. |
| <CopyableCode code="routineType" /> | `string` | Required. The type of routine. |
| <CopyableCode code="securityMode" /> | `string` | Optional. The security mode of the routine, if defined. If not defined, the security mode is automatically determined from the routine's configuration. |
| <CopyableCode code="sparkOptions" /> | `object` | Options for a user-defined Spark routine. |
| <CopyableCode code="strictMode" /> | `boolean` | Optional. Use this option to catch many common errors. Error checking is not exhaustive, and successfully creating a procedure doesn't guarantee that the procedure will successfully execute at runtime. If `strictMode` is set to `TRUE`, the procedure body is further checked for errors such as non-existent tables or columns. The `CREATE PROCEDURE` statement fails if the body fails any of these checks. If `strictMode` is set to `FALSE`, the procedure body is checked only for syntax. For procedures that invoke themselves recursively, specify `strictMode=FALSE` to avoid non-existent procedure errors during validation. Default value is `TRUE`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="+datasetId, +routineId, projectId" /> | Gets the specified routine resource by routine ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="+datasetId, projectId" /> | Lists all routines in the specified dataset. Requires the READER dataset role. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="+datasetId, projectId" /> | Creates a new routine in the dataset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="+datasetId, +routineId, projectId" /> | Deletes the routine specified by routineId from the dataset. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="+datasetId, projectId" /> | Lists all routines in the specified dataset. Requires the READER dataset role. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="+datasetId, +routineId, projectId" /> | Updates information in an existing routine. The update method replaces the entire Routine resource. |
