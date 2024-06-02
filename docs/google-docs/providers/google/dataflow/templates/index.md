---
title: templates
hide_title: false
hide_table_of_contents: false
keywords:
  - templates
  - dataflow
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
<tr><td><b>Name</b></td><td><code>templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dataflow.templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="metadata" /> | `object` | Metadata describing a template. |
| <CopyableCode code="runtimeMetadata" /> | `object` | RuntimeMetadata describing a runtime environment. |
| <CopyableCode code="status" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="templateType" /> | `string` | Template Type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_templates_get" /> | `SELECT` | <CopyableCode code="location, projectId" /> | Get the template associated with a template. |
| <CopyableCode code="projects_templates_get" /> | `SELECT` | <CopyableCode code="projectId" /> | Get the template associated with a template. |
| <CopyableCode code="projects_locations_templates_create" /> | `INSERT` | <CopyableCode code="location, projectId" /> | Creates a Cloud Dataflow job from a template. Do not enter confidential information when you supply string values using the API. |
| <CopyableCode code="projects_templates_create" /> | `INSERT` | <CopyableCode code="projectId" /> | Creates a Cloud Dataflow job from a template. Do not enter confidential information when you supply string values using the API. |
| <CopyableCode code="projects_locations_templates_launch" /> | `EXEC` | <CopyableCode code="location, projectId" /> | Launch a template. |
| <CopyableCode code="projects_templates_launch" /> | `EXEC` | <CopyableCode code="projectId" /> | Launch a template. |
