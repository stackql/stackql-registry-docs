---
title: location_based_capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - location_based_capabilities
  - mysql
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
<tr><td><b>Name</b></td><td><code>location_based_capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.location_based_capabilities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="supportedFlexibleServerEditions" /> | `array` | A list of supported flexible server editions. |
| <CopyableCode code="supportedGeoBackupRegions" /> | `array` | supported geo backup regions |
| <CopyableCode code="supportedHAMode" /> | `array` | Supported high availability mode |
| <CopyableCode code="zone" /> | `string` | zone name |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationName, subscriptionId" /> |
