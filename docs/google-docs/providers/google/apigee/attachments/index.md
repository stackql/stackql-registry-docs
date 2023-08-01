---
title: attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - attachments
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
<tr><td><b>Name</b></td><td><code>attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. ID of the attachment. |
| `createdAt` | `string` | Output only. Time the attachment was created in milliseconds since epoch. |
| `environment` | `string` | ID of the attached environment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_envgroups_attachments_get` | `SELECT` | `attachmentsId, envgroupsId, organizationsId` | Gets an environment group attachment. |
| `organizations_envgroups_attachments_list` | `SELECT` | `envgroupsId, organizationsId` | Lists all attachments of an environment group. |
| `organizations_instances_attachments_get` | `SELECT` | `attachmentsId, instancesId, organizationsId` | Gets an attachment. **Note:** Not supported for Apigee hybrid. |
| `organizations_instances_attachments_list` | `SELECT` | `instancesId, organizationsId` | Lists all attachments to an instance. **Note:** Not supported for Apigee hybrid. |
| `organizations_envgroups_attachments_create` | `INSERT` | `envgroupsId, organizationsId` | Creates a new attachment of an environment to an environment group. |
| `organizations_instances_attachments_create` | `INSERT` | `instancesId, organizationsId` | Creates a new attachment of an environment to an instance. **Note:** Not supported for Apigee hybrid. |
| `organizations_envgroups_attachments_delete` | `DELETE` | `attachmentsId, envgroupsId, organizationsId` | Deletes an environment group attachment. |
| `organizations_instances_attachments_delete` | `DELETE` | `attachmentsId, instancesId, organizationsId` | Deletes an attachment. **Note:** Not supported for Apigee hybrid. |
