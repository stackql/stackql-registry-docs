---
title: scheduled_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions
  - computeschedule
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

Creates, updates, deletes, gets or lists a <code>scheduled_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.computeschedule.scheduled_actions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="virtual_machines_cancel_operations" /> | `EXEC` | <CopyableCode code="locationparameter, subscriptionId, data__correlationid, data__operationIds" /> | virtualMachinesCancelOperations: cancelOperations for a virtual machine |
| <CopyableCode code="virtual_machines_execute_deallocate" /> | `EXEC` | <CopyableCode code="locationparameter, subscriptionId, data__correlationid, data__executionParameters, data__resources" /> | virtualMachinesExecuteDeallocate: executeDeallocate for a virtual machine |
| <CopyableCode code="virtual_machines_execute_hibernate" /> | `EXEC` | <CopyableCode code="locationparameter, subscriptionId, data__correlationid, data__executionParameters, data__resources" /> | virtualMachinesExecuteHibernate: executeHibernate for a virtual machine |
| <CopyableCode code="virtual_machines_execute_start" /> | `EXEC` | <CopyableCode code="locationparameter, subscriptionId, data__correlationid, data__executionParameters, data__resources" /> | virtualMachinesExecuteStart: executeStart for a virtual machine |
| <CopyableCode code="virtual_machines_get_operation_errors" /> | `EXEC` | <CopyableCode code="locationparameter, subscriptionId, data__operationIds" /> | virtualMachinesGetOperationErrors: getOperationErrors associated with an operation on a virtual machine |
| <CopyableCode code="virtual_machines_get_operation_status" /> | `EXEC` | <CopyableCode code="locationparameter, subscriptionId, data__correlationid, data__operationIds" /> | virtualMachinesGetOperationStatus: getOperationStatus for a virtual machine |
| <CopyableCode code="virtual_machines_submit_deallocate" /> | `EXEC` | <CopyableCode code="locationparameter, subscriptionId, data__correlationid, data__executionParameters, data__resources, data__schedule" /> | virtualMachinesSubmitDeallocate: submitDeallocate for a virtual machine |
| <CopyableCode code="virtual_machines_submit_hibernate" /> | `EXEC` | <CopyableCode code="locationparameter, subscriptionId, data__correlationid, data__executionParameters, data__resources, data__schedule" /> | virtualMachinesSubmitHibernate: submitHibernate for a virtual machine |
| <CopyableCode code="virtual_machines_submit_start" /> | `EXEC` | <CopyableCode code="locationparameter, subscriptionId, data__correlationid, data__executionParameters, data__resources, data__schedule" /> | virtualMachinesSubmitStart: submitStart for a virtual machine |
