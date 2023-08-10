---
title: data_items
hide_title: false
hide_table_of_contents: false
keywords:
  - data_items
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>data_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.data_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the DataItem. |
| `etag` | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| `labels` | `object` | Optional. The labels with user-defined metadata to organize your DataItems. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one DataItem(System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| `payload` | `any` | Required. The data that the DataItem represents (for example, an image or a text snippet). The schema of the payload is stored in the parent Dataset's metadata schema's dataItemSchemaUri field. |
| `updateTime` | `string` | Output only. Timestamp when this DataItem was last updated. |
| `createTime` | `string` | Output only. Timestamp when this DataItem was created. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `datasetsId, locationsId, projectsId` |
| `_list` | `EXEC` | `datasetsId, locationsId, projectsId` |
