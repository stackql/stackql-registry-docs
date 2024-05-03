---
title: incident_relations
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_relations
  - sentinel
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
<tr><td><b>Name</b></td><td><code>incident_relations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.incident_relations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Relation property bag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="incidentId, relationName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a relation for a given incident. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets all relations for a given incident. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="incidentId, relationName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a relation for a given incident. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="incidentId, relationName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a relation for a given incident. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets all relations for a given incident. |
