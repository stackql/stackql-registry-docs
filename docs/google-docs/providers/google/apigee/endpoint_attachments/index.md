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
| `endpointAttachments` | `array` | Endpoint attachments in the specified organization. |
| `nextPageToken` | `string` | Page token that you can include in an `ListEndpointAttachments` request to retrieve the next page. If omitted, no subsequent pages exist. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_endpoint_attachments_get` | `SELECT` | `endpointAttachmentsId, organizationsId` | Gets the endpoint attachment. |
| `organizations_endpoint_attachments_list` | `SELECT` | `organizationsId` | Lists the endpoint attachments in an organization. |
| `organizations_endpoint_attachments_create` | `INSERT` | `organizationsId` | Creates an endpoint attachment. **Note:** Not supported for Apigee hybrid. |
| `organizations_endpoint_attachments_delete` | `DELETE` | `endpointAttachmentsId, organizationsId` | Deletes an endpoint attachment. |
