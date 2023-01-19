---
title: datasources_schema
hide_title: false
hide_table_of_contents: false
keywords:
  - datasources_schema
  - cloudsearch
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
<tr><td><b>Name</b></td><td><code>datasources_schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudsearch.datasources_schema</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `objectDefinitions` | `array` | The list of top-level objects for the data source. The maximum number of elements is 10. |
| `operationIds` | `array` | IDs of the Long Running Operations (LROs) currently running for this schema. After modifying the schema, wait for operations to complete before indexing additional content. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `indexing_datasources_getSchema` | `SELECT` | `datasourcesId` | Gets the schema of a data source. **Note:** This API requires an admin or service account to execute. |
| `indexing_datasources_deleteSchema` | `DELETE` | `datasourcesId` | Deletes the schema of a data source. **Note:** This API requires an admin or service account to execute. |
