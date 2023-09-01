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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.endpoint_attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the endpoint attachment. Use the following structure in your request: `organizations/&#123;org&#125;/endpointAttachments/&#123;endpoint_attachment&#125;` |
| `connectionState` | `string` | Output only. State of the endpoint attachment connection to the service attachment. |
| `host` | `string` | Output only. Host that can be used in either the HTTP target endpoint directly or as the host in target server. |
| `location` | `string` | Required. Location of the endpoint attachment. |
| `serviceAttachment` | `string` | Format: projects/*/regions/*/serviceAttachments/* |
| `state` | `string` | Output only. State of the endpoint attachment. Values other than `ACTIVE` mean the resource is not ready to use. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_endpoint_attachments_get` | `SELECT` | `endpointAttachmentsId, organizationsId` | Gets the endpoint attachment. |
| `organizations_endpoint_attachments_list` | `SELECT` | `organizationsId` | Lists the endpoint attachments in an organization. |
| `organizations_endpoint_attachments_create` | `INSERT` | `organizationsId` | Creates an endpoint attachment. **Note:** Not supported for Apigee hybrid. |
| `organizations_endpoint_attachments_delete` | `DELETE` | `endpointAttachmentsId, organizationsId` | Deletes an endpoint attachment. |
| `_organizations_endpoint_attachments_list` | `EXEC` | `organizationsId` | Lists the endpoint attachments in an organization. |
