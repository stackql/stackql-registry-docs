---
title: monitor_vm_host_updates
hide_title: false
hide_table_of_contents: false
keywords:
  - monitor_vm_host_updates
  - logz
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

Creates, updates, deletes, gets or lists a <code>monitor_vm_host_updates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitor_vm_host_updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.logz.monitor_vm_host_updates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Request of a list vm host update operation. |
| <CopyableCode code="agentVersion" /> | `string` | Version of the Logz agent installed on the VM. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
agentVersion
FROM azure_isv.logz.monitor_vm_host_updates
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```