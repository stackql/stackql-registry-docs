---
title: user_shared_access_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - user_shared_access_tokens
  - api_management
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

Creates, updates, deletes, gets or lists a <code>user_shared_access_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_shared_access_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.user_shared_access_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="value" /> | `string` | Shared Access Authorization token for the User. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, userId" /> | Gets the Shared Access Authorization Token for the User. |

## `SELECT` examples

Gets the Shared Access Authorization Token for the User.


```sql
SELECT
value
FROM azure.api_management.user_shared_access_tokens
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userId = '{{ userId }}';
```