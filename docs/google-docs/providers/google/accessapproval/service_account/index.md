---
title: service_account
hide_title: false
hide_table_of_contents: false
keywords:
  - service_account
  - accessapproval
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
<tr><td><b>Name</b></td><td><code>service_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="accessapproval.service_account" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the Access Approval service account. Format is one of: * "projects/&#123;project&#125;/serviceAccount" * "folders/&#123;folder&#125;/serviceAccount" * "organizations/&#123;organization&#125;/serviceAccount" |
| <CopyableCode code="accountEmail" /> | `string` | Email address of the service account. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="folders_get_service_account" /> | `SELECT` | <CopyableCode code="foldersId" /> |
| <CopyableCode code="organizations_get_service_account" /> | `SELECT` | <CopyableCode code="organizationsId" /> |
| <CopyableCode code="projects_get_service_account" /> | `SELECT` | <CopyableCode code="projectsId" /> |
