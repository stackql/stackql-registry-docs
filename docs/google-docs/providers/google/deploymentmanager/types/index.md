---
title: types
hide_title: false
hide_table_of_contents: false
keywords:
  - types
  - deploymentmanager
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
<tr><td><b>Name</b></td><td><code>types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.deploymentmanager.types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | Name of the type. |
| <CopyableCode code="insertTime" /> | `string` | Output only. Creation timestamp in RFC3339 text format. |
| <CopyableCode code="operation" /> | `object` | Represents an Operation resource. Google Compute Engine has three Operation resources: * [Global](/compute/docs/reference/rest/&#123;$api_version&#125;/globalOperations) * [Regional](/compute/docs/reference/rest/&#123;$api_version&#125;/regionOperations) * [Zonal](/compute/docs/reference/rest/&#123;$api_version&#125;/zoneOperations) You can use an operation resource to manage asynchronous API requests. For more information, read Handling API responses. Operations can be global, regional or zonal. - For global operations, use the `globalOperations` resource. - For regional operations, use the `regionOperations` resource. - For zonal operations, use the `zoneOperations` resource. For more information, read Global, Regional, and Zonal Resources. |
| <CopyableCode code="selfLink" /> | `string` | Output only. Server defined URL for the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="project" /> |
