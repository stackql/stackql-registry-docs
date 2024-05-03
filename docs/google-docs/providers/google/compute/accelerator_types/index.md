---
title: accelerator_types
hide_title: false
hide_table_of_contents: false
keywords:
  - accelerator_types
  - compute
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
<tr><td><b>Name</b></td><td><code>accelerator_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.accelerator_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | [Output Only] Name of the resource. |
| <CopyableCode code="description" /> | `string` | [Output Only] An optional textual description of the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="deprecated" /> | `object` | Deprecation status for a public resource. |
| <CopyableCode code="kind" /> | `string` | [Output Only] The type of the resource. Always compute#acceleratorType for accelerator types. |
| <CopyableCode code="maximumCardsPerInstance" /> | `integer` | [Output Only] Maximum number of accelerator cards allowed per instance. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined, fully qualified URL for this resource. |
| <CopyableCode code="zone" /> | `string` | [Output Only] The name of the zone where the accelerator type resides, such as us-central1-a. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of accelerator types. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="acceleratorType, project, zone" /> | Returns the specified accelerator type. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, zone" /> | Retrieves a list of accelerator types that are available to the specified project. |
| <CopyableCode code="_aggregated_list" /> | `EXEC` | <CopyableCode code="project" /> | Retrieves an aggregated list of accelerator types. |
