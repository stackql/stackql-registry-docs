---
title: offers_access_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - offers_access_tokens
  - edge_marketplace
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

Creates, updates, deletes, gets or lists a <code>offers_access_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>offers_access_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edge_marketplace.offers_access_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accessToken" /> | `string` | The access token. |
| <CopyableCode code="diskId" /> | `string` | The disk id. |
| <CopyableCode code="status" /> | `string` | The access token creation status. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="offerId, resourceUri, data__requestId" /> | get access token. |

## `SELECT` examples

get access token.


```sql
SELECT
accessToken,
diskId,
status
FROM azure_extras.edge_marketplace.offers_access_tokens
WHERE offerId = '{{ offerId }}'
AND resourceUri = '{{ resourceUri }}'
AND data__requestId = '{{ data__requestId }}';
```