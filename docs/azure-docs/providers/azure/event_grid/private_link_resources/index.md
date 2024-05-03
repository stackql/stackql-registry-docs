---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - event_grid
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.private_link_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="parentName, parentType, privateLinkResourceName, resourceGroupName, subscriptionId" /> | Get properties of a private link resource. |
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="parentName, parentType, resourceGroupName, subscriptionId" /> | List all the private link resources under a topic, domain, or partner namespace or namespace. |
| <CopyableCode code="_list_by_resource" /> | `EXEC` | <CopyableCode code="parentName, parentType, resourceGroupName, subscriptionId" /> | List all the private link resources under a topic, domain, or partner namespace or namespace. |
