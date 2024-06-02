---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - config
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
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="config.resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/deployments/&#123;deployment&#125;/revisions/&#123;revision&#125;/resources/&#123;resource&#125;` |
| <CopyableCode code="caiAssets" /> | `object` | Output only. Map of Cloud Asset Inventory (CAI) type to CAI info (e.g. CAI ID). CAI type format follows https://cloud.google.com/asset-inventory/docs/supported-asset-types |
| <CopyableCode code="intent" /> | `string` | Output only. Intent of the resource. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the resource. |
| <CopyableCode code="terraformInfo" /> | `object` | Terraform info of a Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentsId, locationsId, projectsId, resourcesId, revisionsId" /> | Gets details about a Resource deployed by Infra Manager. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deploymentsId, locationsId, projectsId, revisionsId" /> | Lists Resources in a given revision. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="deploymentsId, locationsId, projectsId, revisionsId" /> | Lists Resources in a given revision. |
