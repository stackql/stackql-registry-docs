---
title: address_groups_items
hide_title: false
hide_table_of_contents: false
keywords:
  - address_groups_items
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
<tr><td><b>Name</b></td><td><code>address_groups_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="networksecurity.address_groups_items" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_address_groups_add_items" /> | `EXEC` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Adds items to an address group. |
| <CopyableCode code="organizations_locations_address_groups_remove_items" /> | `EXEC` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Removes items from an address group. |
| <CopyableCode code="projects_locations_address_groups_add_items" /> | `EXEC` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Adds items to an address group. |
| <CopyableCode code="projects_locations_address_groups_remove_items" /> | `EXEC` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Removes items from an address group. |
