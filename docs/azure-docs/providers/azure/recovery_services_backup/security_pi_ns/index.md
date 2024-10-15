---
title: security_pi_ns
hide_title: false
hide_table_of_contents: false
keywords:
  - security_pi_ns
  - recovery_services_backup
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

Creates, updates, deletes, gets or lists a <code>security_pi_ns</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_pi_ns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.security_pi_ns" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expiryTimeInUtcTicks" /> | `integer` | Expiry time of token. |
| <CopyableCode code="securityPIN" /> | `string` | Security PIN |
| <CopyableCode code="token" /> | `string` | Token value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Get the security PIN. |

## `SELECT` examples

Get the security PIN.


```sql
SELECT
expiryTimeInUtcTicks,
securityPIN,
token
FROM azure.recovery_services_backup.security_pi_ns
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```