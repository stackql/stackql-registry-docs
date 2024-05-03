---
title: database_advanced_threat_protection_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - database_advanced_threat_protection_settings
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
<tr><td><b>Name</b></td><td><code>database_advanced_threat_protection_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.database_advanced_threat_protection_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an Advanced Threat Protection state. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="advancedThreatProtectionName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a database's Advanced Threat Protection state. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of database's Advanced Threat Protection states. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="advancedThreatProtectionName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a database's Advanced Threat Protection state. |
| <CopyableCode code="_list_by_database" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of database's Advanced Threat Protection states. |
