---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - sap_workloads
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation, as per Resource-Based Access Control (RBAC). Examples: "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action" |
| <CopyableCode code="actionType" /> | `string` | Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs. |
| <CopyableCode code="display" /> | `object` | Localized display information for this particular operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Whether the operation applies to data-plane. This is "true" for data-plane operations and "false" for ARM/control-plane operations. |
| <CopyableCode code="origin" /> | `string` | The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit logs UX. Default value is "user,system" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all the available API operations under this PR |
| <CopyableCode code="sap_availability_zone_details" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__appLocation, data__databaseType, data__sapProduct" /> | Get the recommended SAP Availability Zone Pair Details for your region. |
| <CopyableCode code="sap_disk_configurations" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__appLocation, data__databaseType, data__dbVmSku, data__deploymentType, data__environment, data__sapProduct" /> | Get the SAP Disk Configuration Layout prod/non-prod SAP System. |
| <CopyableCode code="sap_sizing_recommendations" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__appLocation, data__databaseType, data__dbMemory, data__deploymentType, data__environment, data__sapProduct, data__saps" /> | Get SAP sizing recommendations by providing input SAPS for application tier and memory required for database tier |
| <CopyableCode code="sap_supported_sku" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__appLocation, data__databaseType, data__deploymentType, data__environment, data__sapProduct" /> | Get a list of SAP supported SKUs for ASCS, Application and Database tier. |

## `SELECT` examples

Lists all the available API operations under this PR


```sql
SELECT
name,
actionType,
display,
isDataAction,
origin
FROM azure_isv.sap_workloads.operations
;
```