---
title: user_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - user_settings
  - cloud_shell
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
<tr><td><b>Name</b></td><td><code>user_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cloud_shell.user_settings" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="userSettingsName" /> | Get current user settings for current signed in user. This operation returns settings for the user's cloud shell preferences including preferred location, storage profile, shell type, font and size settings. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="userSettingsName" /> | Delete cloud shell settings for current signed in user |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="userSettingsName" /> | Patch cloud shell settings for current signed in user |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="userSettingsName, data__properties" /> | Create or update cloud shell settings for current signed in user |
