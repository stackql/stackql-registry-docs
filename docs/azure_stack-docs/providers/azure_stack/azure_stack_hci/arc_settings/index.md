---
title: arc_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - arc_settings
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
<tr><td><b>Name</b></td><td><code>arc_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.arc_settings" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Get ArcSetting resource details of HCI Cluster. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get ArcSetting resources of HCI Cluster. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Create ArcSetting for HCI cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Delete ArcSetting resource details of HCI Cluster. |
| <CopyableCode code="consent_and_install_default_extensions" /> | `EXEC` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Add consent time for default extensions and initiate extensions installation |
| <CopyableCode code="generate_password" /> | `EXEC` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Generate password for arc settings. |
| <CopyableCode code="initialize_disable_process" /> | `EXEC` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Initializes ARC Disable process on the cluster |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="arcSettingName, clusterName, resourceGroupName, subscriptionId" /> | Update ArcSettings for HCI cluster. |
