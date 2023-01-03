---
title: sources
hide_title: false
hide_table_of_contents: false
keywords:
  - sources
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The relative resource name of this source. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name Example: "organizations/{organization_id}/sources/{source_id}" |
| `description` | `string` | The description of the source (max of 1024 characters). Example: "Web Security Scanner is a web security scanner for common vulnerabilities in App Engine applications. It can automatically scan and detect four common vulnerabilities, including cross-site-scripting (XSS), Flash injection, mixed content (HTTP in HTTPS), and outdated or insecure libraries." |
| `canonicalName` | `string` | The canonical name of the finding. It's either "organizations/{organization_id}/sources/{source_id}", "folders/{folder_id}/sources/{source_id}" or "projects/{project_number}/sources/{source_id}", depending on the closest CRM ancestor of the resource associated with the finding. |
| `displayName` | `string` | The source's display name. A source's display name must be unique amongst its siblings, for example, two sources with the same parent can't share the same display name. The display name must have a length between 1 and 64 characters (inclusive). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_sources_list` | `SELECT` | `foldersId` | Lists all sources belonging to an organization. |
| `organizations_sources_get` | `SELECT` | `organizationsId, sourcesId` | Gets a source. |
| `organizations_sources_list` | `SELECT` | `organizationsId` | Lists all sources belonging to an organization. |
| `projects_sources_list` | `SELECT` | `projectsId` | Lists all sources belonging to an organization. |
| `organizations_sources_create` | `INSERT` | `organizationsId` | Creates a source. |
| `organizations_sources_patch` | `EXEC` | `organizationsId, sourcesId` | Updates a source. |
