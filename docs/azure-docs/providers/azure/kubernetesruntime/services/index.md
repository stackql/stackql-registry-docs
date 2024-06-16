---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - kubernetesruntime
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetesruntime.services" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri, serviceName" /> | Get a ServiceResource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List ServiceResource resources by parent |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceUri, serviceName" /> | Create a ServiceResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri, serviceName" /> | Delete a ServiceResource |
