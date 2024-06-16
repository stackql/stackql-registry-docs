---
title: linkers_dryrun
hide_title: false
hide_table_of_contents: false
keywords:
  - linkers_dryrun
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
<tr><td><b>Name</b></td><td><code>linkers_dryrun</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_connector.linkers_dryrun" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dryrunName, resourceUri" /> | get a dryrun job |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | list dryrun jobs |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dryrunName, resourceUri" /> | create a dryrun job to do necessary check before actual creation |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dryrunName, resourceUri" /> | delete a dryrun job |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dryrunName, resourceUri" /> | add a dryrun job to do necessary check before actual creation |
