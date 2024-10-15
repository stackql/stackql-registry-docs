---
title: iot_dps_resource_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resource_operation_results
  - iot_hub_device_provisioning
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

Creates, updates, deletes, gets or lists a <code>iot_dps_resource_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_dps_resource_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub_device_provisioning.iot_dps_resource_operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="error" /> | `object` | Error response containing message and code. |
| <CopyableCode code="status" /> | `string` | current status of a long running operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="asyncinfo, operationId, provisioningServiceName, resourceGroupName, subscriptionId" /> | Gets the status of a long running operation, such as create, update or delete a provisioning service. |

## `SELECT` examples

Gets the status of a long running operation, such as create, update or delete a provisioning service.


```sql
SELECT
error,
status
FROM azure.iot_hub_device_provisioning.iot_dps_resource_operation_results
WHERE asyncinfo = '{{ asyncinfo }}'
AND operationId = '{{ operationId }}'
AND provisioningServiceName = '{{ provisioningServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```