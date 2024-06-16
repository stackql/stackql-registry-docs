---
title: spacecrafts_available_contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - spacecrafts_available_contacts
  - orbital
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
<tr><td><b>Name</b></td><td><code>spacecrafts_available_contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.orbital.spacecrafts_available_contacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="groundStationName" /> | `string` | Name of Azure Ground Station. |
| <CopyableCode code="properties" /> | `object` | Properties of Contact resource. |
| <CopyableCode code="spacecraft" /> | `object` | The reference to the spacecraft resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, spacecraftName, subscriptionId, data__contactProfile, data__endTime, data__groundStationName, data__startTime" /> |
