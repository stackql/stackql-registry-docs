---
title: apicategories
hide_title: false
hide_table_of_contents: false
keywords:
  - apicategories
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
<tr><td><b>Name</b></td><td><code>apicategories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.apicategories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` | the Api category resource. |
| <CopyableCode code="errorCode" /> | `string` | ID that can be used to find errors in the log files. |
| <CopyableCode code="message" /> | `string` | Description of the operation. |
| <CopyableCode code="requestId" /> | `string` | ID that can be used to find request details in the log files. |
| <CopyableCode code="status" /> | `string` | Status of the operation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_sites_apicategories_get" /> | `SELECT` | <CopyableCode code="apicategoriesId, organizationsId, sitesId" /> | Gets a category on the portal. |
| <CopyableCode code="organizations_sites_apicategories_list" /> | `SELECT` | <CopyableCode code="organizationsId, sitesId" /> | Lists the categories on the portal. |
| <CopyableCode code="organizations_sites_apicategories_create" /> | `INSERT` | <CopyableCode code="organizationsId, sitesId" /> | Creates a new category on the portal. |
| <CopyableCode code="organizations_sites_apicategories_delete" /> | `DELETE` | <CopyableCode code="apicategoriesId, organizationsId, sitesId" /> | Deletes a category from the portal. |
| <CopyableCode code="organizations_sites_apicategories_patch" /> | `EXEC` | <CopyableCode code="apicategoriesId, organizationsId, sitesId" /> | Updates a category on the portal. |
