---
title: endpoint_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_attachments
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
<tr><td><b>Name</b></td><td><code>endpoint_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.endpoint_attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the endpoint attachment. Use the following structure in your request: `organizations/&#123;org&#125;/endpointAttachments/&#123;endpoint_attachment&#125;` |
| <CopyableCode code="connectionState" /> | `string` | Output only. State of the endpoint attachment connection to the service attachment. |
| <CopyableCode code="host" /> | `string` | Output only. Host that can be used in either the HTTP target endpoint directly or as the host in target server. |
| <CopyableCode code="location" /> | `string` | Required. Location of the endpoint attachment. |
| <CopyableCode code="serviceAttachment" /> | `string` | Format: projects/*/regions/*/serviceAttachments/* |
| <CopyableCode code="state" /> | `string` | Output only. State of the endpoint attachment. Values other than `ACTIVE` mean the resource is not ready to use. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_endpoint_attachments_get" /> | `SELECT` | <CopyableCode code="endpointAttachmentsId, organizationsId" /> | Gets the endpoint attachment. |
| <CopyableCode code="organizations_endpoint_attachments_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists the endpoint attachments in an organization. |
| <CopyableCode code="organizations_endpoint_attachments_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates an endpoint attachment. **Note:** Not supported for Apigee hybrid. |
| <CopyableCode code="organizations_endpoint_attachments_delete" /> | `DELETE` | <CopyableCode code="endpointAttachmentsId, organizationsId" /> | Deletes an endpoint attachment. |
| <CopyableCode code="_organizations_endpoint_attachments_list" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Lists the endpoint attachments in an organization. |
