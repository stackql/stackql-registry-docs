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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="securitycenter.sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The relative resource name of this source. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name Example: "organizations/&#123;organization_id&#125;/sources/&#123;source_id&#125;" |
| <CopyableCode code="description" /> | `string` | The description of the source (max of 1024 characters). Example: "Web Security Scanner is a web security scanner for common vulnerabilities in App Engine applications. It can automatically scan and detect four common vulnerabilities, including cross-site-scripting (XSS), Flash injection, mixed content (HTTP in HTTPS), and outdated or insecure libraries." |
| <CopyableCode code="canonicalName" /> | `string` | The canonical name of the finding source. It's either "organizations/&#123;organization_id&#125;/sources/&#123;source_id&#125;", "folders/&#123;folder_id&#125;/sources/&#123;source_id&#125;", or "projects/&#123;project_number&#125;/sources/&#123;source_id&#125;", depending on the closest CRM ancestor of the resource associated with the finding. |
| <CopyableCode code="displayName" /> | `string` | The source's display name. A source's display name must be unique amongst its siblings, for example, two sources with the same parent can't share the same display name. The display name must have a length between 1 and 64 characters (inclusive). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_sources_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists all sources belonging to an organization. |
| <CopyableCode code="organizations_sources_get" /> | `SELECT` | <CopyableCode code="organizationsId, sourcesId" /> | Gets a source. |
| <CopyableCode code="organizations_sources_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all sources belonging to an organization. |
| <CopyableCode code="projects_sources_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists all sources belonging to an organization. |
| <CopyableCode code="organizations_sources_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a source. |
| <CopyableCode code="_folders_sources_list" /> | `EXEC` | <CopyableCode code="foldersId" /> | Lists all sources belonging to an organization. |
| <CopyableCode code="_organizations_sources_list" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Lists all sources belonging to an organization. |
| <CopyableCode code="_projects_sources_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists all sources belonging to an organization. |
| <CopyableCode code="organizations_sources_patch" /> | `EXEC` | <CopyableCode code="organizationsId, sourcesId" /> | Updates a source. |
