---
title: clusters_jwks
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_jwks
  - container
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
<tr><td><b>Name</b></td><td><code>clusters_jwks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.container.clusters_jwks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cacheHeader" /> | `object` | RFC-2616: cache control support |
| <CopyableCode code="keys" /> | `array` | The public component of the keys used by the cluster to sign token requests. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_clusters_get_jwks" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId" /> |
