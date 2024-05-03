---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - azure_stack_hci
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.extensions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId" /> | Get particular Arc Extension of HCI Cluster. |
| <CopyableCode code="list_by_arc_setting" /> | `SELECT` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | List all Extensions under ArcSetting resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId" /> | Create Extension for HCI cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId" /> | Delete particular Arc Extension of HCI Cluster. |
| <CopyableCode code="_list_by_arc_setting" /> | `EXEC` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | List all Extensions under ArcSetting resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId" /> | Update Extension for HCI cluster. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId" /> | Upgrade a particular Arc Extension of HCI Cluster. |
