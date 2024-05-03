---
title: managed_database_sensitivity_labels_current_by_database
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_sensitivity_labels_current_by_database
  - sql
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
<tr><td><b>Name</b></td><td><code>managed_database_sensitivity_labels_current_by_database</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_sensitivity_labels_current_by_database" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | Resource that manages the sensitivity label. |
| <CopyableCode code="properties" /> | `object` | Properties of a sensitivity label. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> |
