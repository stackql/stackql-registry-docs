---
title: services_test_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - services_test_keys
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>services_test_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.services_test_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="enabled" /> | `boolean` | Indicates whether the test endpoint feature enabled or not |
| <CopyableCode code="primaryKey" /> | `string` | Primary key |
| <CopyableCode code="primaryTestEndpoint" /> | `string` | Primary test endpoint |
| <CopyableCode code="secondaryKey" /> | `string` | Secondary key |
| <CopyableCode code="secondaryTestEndpoint" /> | `string` | Secondary test endpoint |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> |
