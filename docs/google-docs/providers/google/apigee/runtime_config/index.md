---
title: runtime_config
hide_title: false
hide_table_of_contents: false
keywords:
  - runtime_config
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
<tr><td><b>Name</b></td><td><code>runtime_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.runtime_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the resource in the following format: `organizations/&#123;org&#125;/runtimeConfig`. |
| <CopyableCode code="analyticsBucket" /> | `string` | Cloud Storage bucket used for uploading Analytics records. |
| <CopyableCode code="tenantProjectId" /> | `string` | Output only. Tenant project ID associated with the Apigee organization. The tenant project is used to host Google-managed resources that are dedicated to this Apigee organization. Clients have limited access to resources within the tenant project used to support Apigee runtime instances. Access to the tenant project is managed using SetSyncAuthorization. It can be empty if the tenant project hasn't been created yet. |
| <CopyableCode code="traceBucket" /> | `string` | Cloud Storage bucket used for uploading Trace records. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="organizations_get_runtime_config" /> | `SELECT` | <CopyableCode code="organizationsId" /> |
