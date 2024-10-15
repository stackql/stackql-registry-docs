---
title: online_endpoints_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - online_endpoints_tokens
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>online_endpoints_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>online_endpoints_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.online_endpoints_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessToken" /> | `string` | Access token for endpoint authentication. |
| <CopyableCode code="expiryTimeUtc" /> | `integer` | Access token expiry time (UTC). |
| <CopyableCode code="refreshAfterTimeUtc" /> | `integer` | Refresh access token after time (UTC). |
| <CopyableCode code="tokenType" /> | `string` | Access token type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, resourceGroupName, subscriptionId, workspaceName" /> |  |

## `SELECT` examples




```sql
SELECT
accessToken,
expiryTimeUtc,
refreshAfterTimeUtc,
tokenType
FROM azure.ml_services.online_endpoints_tokens
WHERE endpointName = '{{ endpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```