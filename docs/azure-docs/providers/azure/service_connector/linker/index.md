---
title: linker
hide_title: false
hide_table_of_contents: false
keywords:
  - linker
  - service_connector
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
<tr><td><b>Name</b></td><td><code>linker</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_connector.linker" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of the Linker. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="linkerName, resourceUri" /> | Returns Linker resource for a given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Returns list of Linkers which connects to the resource. which supports to config both application and target service during the resource provision. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="linkerName, resourceUri, data__properties" /> | Create or update Linker resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="linkerName, resourceUri" /> | Delete a Linker. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceUri" /> | Returns list of Linkers which connects to the resource. which supports to config both application and target service during the resource provision. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="linkerName, resourceUri" /> | Operation to update an existing Linker. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="linkerName, resourceUri" /> | Validate a Linker. |
