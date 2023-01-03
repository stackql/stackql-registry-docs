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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.endpoint_attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the endpoint attachment. Use the following structure in your request: `organizations/{org}/endpointAttachments/{endpoint_attachment}` |
| `location` | `string` | Required. Location of the endpoint attachment. |
| `serviceAttachment` | `string` | Format: projects/*/regions/*/serviceAttachments/* |
| `state` | `string` | Output only. State of the endpoint attachment. Values other than `ACTIVE` mean the resource is not ready to use. |
| `host` | `string` | Output only. Host that can be used in either the HTTP target endpoint directly or as the host in target server. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_endpointAttachments_get` | `SELECT` | `endpointAttachmentsId, organizationsId` | Gets the endpoint attachment. |
| `organizations_endpointAttachments_list` | `SELECT` | `organizationsId` | Lists the endpoint attachments in an organization. |
| `organizations_endpointAttachments_create` | `INSERT` | `organizationsId` | Creates an endpoint attachment. **Note:** Not supported for Apigee hybrid. |
| `organizations_endpointAttachments_delete` | `DELETE` | `endpointAttachmentsId, organizationsId` | Deletes an endpoint attachment. |
