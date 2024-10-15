---
title: host_pools_registration_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - host_pools_registration_tokens
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>host_pools_registration_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_pools_registration_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.host_pools_registration_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expirationTime" /> | `string` | Expiration time of registration token. |
| <CopyableCode code="token" /> | `string` | The registration token base64 encoded string. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Operation to list the RegistrationTokens associated with the HostPool. |

## `SELECT` examples

Operation to list the RegistrationTokens associated with the HostPool.


```sql
SELECT
expirationTime,
token
FROM azure.desktop_virtualization.host_pools_registration_tokens
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```