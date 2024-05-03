---
title: connector_dryrun
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_dryrun
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
<tr><td><b>Name</b></td><td><code>connector_dryrun</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_connector.connector_dryrun" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dryrunName, location, resourceGroupName, subscriptionId" /> | get a dryrun job |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | list dryrun jobs |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dryrunName, location, resourceGroupName, subscriptionId" /> | create a dryrun job to do necessary check before actual creation |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dryrunName, location, resourceGroupName, subscriptionId" /> | delete a dryrun job |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | list dryrun jobs |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dryrunName, location, resourceGroupName, subscriptionId" /> | update a dryrun job to do necessary check before actual creation |
