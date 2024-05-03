---
title: dimensions_adds_dimensions
hide_title: false
hide_table_of_contents: false
keywords:
  - dimensions_adds_dimensions
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
<tr><td><b>Name</b></td><td><code>dimensions_adds_dimensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.dimensions_adds_dimensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activeAlerts" /> | `integer` | The count of alerts that are currently active for the service. |
| <CopyableCode code="additionalInformation" /> | `string` | The additional information related to the service. |
| <CopyableCode code="displayName" /> | `string` | The display name of the service. |
| <CopyableCode code="health" /> | `string` | The health status for the domain controller. |
| <CopyableCode code="lastUpdated" /> | `string` | The date or time , in UTC, when the service properties were last updated. |
| <CopyableCode code="resolvedAlerts" /> | `integer` | The total count of alerts that has been resolved for the service. |
| <CopyableCode code="signature" /> | `string` | The signature of the service. |
| <CopyableCode code="simpleProperties" /> | `object` | List of service specific configuration properties. |
| <CopyableCode code="type" /> | `string` | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dimension, serviceName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="dimension, serviceName" /> |
