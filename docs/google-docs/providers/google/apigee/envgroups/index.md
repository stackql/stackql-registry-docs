---
title: envgroups
hide_title: false
hide_table_of_contents: false
keywords:
  - envgroups
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
<tr><td><b>Name</b></td><td><code>envgroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.envgroups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | ID of the environment group. |
| `state` | `string` | Output only. State of the environment group. Values other than ACTIVE means the resource is not ready to use. |
| `createdAt` | `string` | Output only. The time at which the environment group was created as milliseconds since epoch. |
| `hostnames` | `array` | Required. Host names for this environment group. |
| `lastModifiedAt` | `string` | Output only. The time at which the environment group was last updated as milliseconds since epoch. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_envgroups_get` | `SELECT` | `envgroupsId, organizationsId` | Gets an environment group. |
| `organizations_envgroups_list` | `SELECT` | `organizationsId` | Lists all environment groups. |
| `organizations_envgroups_create` | `INSERT` | `organizationsId` | Creates a new environment group. |
| `organizations_envgroups_delete` | `DELETE` | `envgroupsId, organizationsId` | Deletes an environment group. |
| `organizations_envgroups_patch` | `EXEC` | `envgroupsId, organizationsId` | Updates an environment group. |
