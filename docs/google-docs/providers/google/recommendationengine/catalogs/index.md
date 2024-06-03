---
title: catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs
  - recommendationengine
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
<tr><td><b>Name</b></td><td><code>catalogs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.recommendationengine.catalogs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The fully qualified resource name of the catalog. |
| <CopyableCode code="catalogItemLevelConfig" /> | `object` | Configures the catalog level that users send events to, and the level at which predictions are made. |
| <CopyableCode code="defaultEventStoreId" /> | `string` | Required. The ID of the default event store. |
| <CopyableCode code="displayName" /> | `string` | Required. The catalog display name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the catalog configurations associated with the project. |
| <CopyableCode code="projects_locations_catalogs_patch" /> | `UPDATE` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Updates the catalog configuration. |
| <CopyableCode code="_projects_locations_catalogs_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all the catalog configurations associated with the project. |
