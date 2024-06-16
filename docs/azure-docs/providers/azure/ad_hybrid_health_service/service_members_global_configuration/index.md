---
title: service_members_global_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_global_configuration
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>service_members_global_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.service_members_global_configuration" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="featureSet" /> | `array` | The list of additional feature sets. |
| <CopyableCode code="numSavedPwdEvent" /> | `integer` | The number of saved password events. |
| <CopyableCode code="passwordSyncEnabled" /> | `boolean` | Indicates if password sync is enabled or not. |
| <CopyableCode code="schemaXml" /> | `string` | The schema for the configuration. |
| <CopyableCode code="version" /> | `integer` | The version for the global configuration. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceMemberId, serviceName" /> |
