---
title: url_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - url_lists
  - networksecurity
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
<tr><td><b>Name</b></td><td><code>url_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.url_lists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the resource provided by the user. Name is of the form projects/&#123;project&#125;/locations/&#123;location&#125;/urlLists/&#123;url_list&#125; url_list should match the pattern:(^[a-z]([a-z0-9-]&#123;0,61&#125;[a-z0-9])?$). |
| <CopyableCode code="description" /> | `string` | Optional. Free-text description of the resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the security policy was created. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the security policy was updated. |
| <CopyableCode code="values" /> | `array` | Required. FQDNs and URLs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_url_lists_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, urlListsId" /> | Gets details of a single UrlList. |
| <CopyableCode code="projects_locations_url_lists_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists UrlLists in a given project and location. |
| <CopyableCode code="projects_locations_url_lists_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new UrlList in a given project and location. |
| <CopyableCode code="projects_locations_url_lists_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, urlListsId" /> | Deletes a single UrlList. |
| <CopyableCode code="_projects_locations_url_lists_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists UrlLists in a given project and location. |
| <CopyableCode code="projects_locations_url_lists_patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, urlListsId" /> | Updates the parameters of a single UrlList. |
