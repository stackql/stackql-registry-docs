---
title: apidocs_documentation
hide_title: false
hide_table_of_contents: false
keywords:
  - apidocs_documentation
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
<tr><td><b>Name</b></td><td><code>apidocs_documentation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.apidocs_documentation" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` | The documentation for a catalog item. |
| <CopyableCode code="errorCode" /> | `string` | Output only. Unique error code for the request, if any. |
| <CopyableCode code="message" /> | `string` | Output only. Description of the operation. |
| <CopyableCode code="requestId" /> | `string` | Output only. Unique ID of the request. |
| <CopyableCode code="status" /> | `string` | Output only. Status of the operation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_sites_apidocs_get_documentation" /> | `SELECT` | <CopyableCode code="apidocsId, organizationsId, sitesId" /> | Gets the documentation for the specified catalog item. |
| <CopyableCode code="organizations_sites_apidocs_update_documentation" /> | `EXEC` | <CopyableCode code="apidocsId, organizationsId, sitesId" /> | Updates the documentation for the specified catalog item. Note that the documentation file contents will not be populated in the return message. |
