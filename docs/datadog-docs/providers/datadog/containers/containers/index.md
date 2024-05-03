---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
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
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.containers.containers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Container ID. |
| <CopyableCode code="ContainerGroup_attributes" /> | `object` | Attributes for a container group. |
| <CopyableCode code="ContainerGroup_id" /> | `string` | Container Group ID. |
| <CopyableCode code="ContainerGroup_type" /> | `string` | Type of container group. |
| <CopyableCode code="attributes" /> | `object` | Attributes for a container. |
| <CopyableCode code="relationships" /> | `object` | Relationships to containers inside a container group. |
| <CopyableCode code="type" /> | `string` | Type of container. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_containers" /> | `SELECT` | <CopyableCode code="dd_site" /> |
| <CopyableCode code="_list_containers" /> | `EXEC` | <CopyableCode code="dd_site" /> |
