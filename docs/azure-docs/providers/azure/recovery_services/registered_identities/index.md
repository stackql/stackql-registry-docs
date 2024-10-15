---
title: registered_identities
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_identities
  - recovery_services
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

Creates, updates, deletes, gets or lists a <code>registered_identities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registered_identities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services.registered_identities" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="identityName, resourceGroupName, subscriptionId, vaultName" /> | Unregisters the given container from your Recovery Services vault. |

## `DELETE` example

Deletes the specified <code>registered_identities</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services.registered_identities
WHERE identityName = '{{ identityName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
