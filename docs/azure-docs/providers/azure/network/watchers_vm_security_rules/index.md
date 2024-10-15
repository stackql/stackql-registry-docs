---
title: watchers_vm_security_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_vm_security_rules
  - network
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

Creates, updates, deletes, gets or lists a <code>watchers_vm_security_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchers_vm_security_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.watchers_vm_security_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="networkInterfaces" /> | `array` | List of network interfaces on the specified VM. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__targetResourceId" /> | Gets the configured and effective security group rules on the specified VM. |

## `SELECT` examples

Gets the configured and effective security group rules on the specified VM.


```sql
SELECT
networkInterfaces
FROM azure.network.watchers_vm_security_rules
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__targetResourceId = '{{ data__targetResourceId }}';
```