---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - containers
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.containers.images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Container Image ID. |
| <CopyableCode code="ContainerImageGroup_attributes" /> | `object` | Attributes for a Container Image Group. |
| <CopyableCode code="ContainerImageGroup_id" /> | `string` | Container Image Group ID. |
| <CopyableCode code="ContainerImageGroup_type" /> | `string` | Type of Container Image Group. |
| <CopyableCode code="attributes" /> | `object` | Attributes for a Container Image. |
| <CopyableCode code="relationships" /> | `object` | Relationships inside a Container Image Group. |
| <CopyableCode code="type" /> | `string` | Type of Container Image. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_container_images" /> | `SELECT` | <CopyableCode code="dd_site" /> |
| <CopyableCode code="_list_container_images" /> | `EXEC` | <CopyableCode code="dd_site" /> |
