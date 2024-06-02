---
title: clusters_certificate_authority
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_certificate_authority
  - redis
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
<tr><td><b>Name</b></td><td><code>clusters_certificate_authority</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="redis.clusters_certificate_authority" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Unique name of the resource in this scope including project, location and cluster using the form: `projects/&#123;project&#125;/locations/&#123;location&#125;/clusters/&#123;cluster&#125;/certificateAuthority` |
| <CopyableCode code="managedServerCa" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_certificate_authority" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId" /> |
