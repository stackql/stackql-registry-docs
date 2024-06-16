---
title: autonomous_database_national_character_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_database_national_character_sets
  - oracle
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>autonomous_database_national_character_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.autonomous_database_national_character_sets" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="adbsncharsetname, location, subscriptionId" /> | Get a AutonomousDatabaseNationalCharacterSet |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List AutonomousDatabaseNationalCharacterSet resources by Location |
