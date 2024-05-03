---
title: address_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - address_groups
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
<tr><td><b>Name</b></td><td><code>address_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.address_groups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_address_groups_get" /> | `SELECT` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Gets details of a single address group. |
| <CopyableCode code="organizations_locations_address_groups_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists address groups in a given project and location. |
| <CopyableCode code="projects_locations_address_groups_get" /> | `SELECT` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Gets details of a single address group. |
| <CopyableCode code="projects_locations_address_groups_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists address groups in a given project and location. |
| <CopyableCode code="organizations_locations_address_groups_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a new address group in a given project and location. |
| <CopyableCode code="projects_locations_address_groups_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new address group in a given project and location. |
| <CopyableCode code="organizations_locations_address_groups_delete" /> | `DELETE` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Deletes an address group. |
| <CopyableCode code="projects_locations_address_groups_delete" /> | `DELETE` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Deletes a single address group. |
| <CopyableCode code="_organizations_locations_address_groups_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists address groups in a given project and location. |
| <CopyableCode code="_projects_locations_address_groups_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists address groups in a given project and location. |
| <CopyableCode code="organizations_locations_address_groups_clone_items" /> | `EXEC` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Clones items from one address group to another. |
| <CopyableCode code="organizations_locations_address_groups_patch" /> | `EXEC` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Updates parameters of an address group. |
| <CopyableCode code="projects_locations_address_groups_clone_items" /> | `EXEC` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Clones items from one address group to another. |
| <CopyableCode code="projects_locations_address_groups_patch" /> | `EXEC` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Updates the parameters of a single address group. |
