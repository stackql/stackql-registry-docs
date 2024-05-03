---
title: resourcefiles
hide_title: false
hide_table_of_contents: false
keywords:
  - resourcefiles
  - apigee
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
<tr><td><b>Name</b></td><td><code>resourcefiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.resourcefiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentType" /> | `string` | The HTTP Content-Type header value specifying the content type of the body. |
| <CopyableCode code="data" /> | `string` | The HTTP request/response body as raw binary. |
| <CopyableCode code="extensions" /> | `array` | Application specific response metadata. Must be set in the first response for streaming APIs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_resourcefiles_get" /> | `SELECT` | <CopyableCode code="environmentsId, name, organizationsId, type" /> | Gets the contents of a resource file. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files). |
| <CopyableCode code="organizations_environments_resourcefiles_list" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Lists all resource files, optionally filtering by type. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files). |
| <CopyableCode code="organizations_environments_resourcefiles_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Creates a resource file. Specify the `Content-Type` as `application/octet-stream` or `multipart/form-data`. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files). |
| <CopyableCode code="organizations_environments_resourcefiles_delete" /> | `DELETE` | <CopyableCode code="environmentsId, name, organizationsId, type" /> | Deletes a resource file. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files). |
| <CopyableCode code="organizations_environments_resourcefiles_update" /> | `EXEC` | <CopyableCode code="environmentsId, name, organizationsId, type" /> | Updates a resource file. Specify the `Content-Type` as `application/octet-stream` or `multipart/form-data`. For more information about resource files, see [Resource files](https://cloud.google.com/apigee/docs/api-platform/develop/resource-files). |
