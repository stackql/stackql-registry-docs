---
title: delegated_provider_offers
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_provider_offers
  - user_subscriptions
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

Creates, updates, deletes, gets or lists a <code>delegated_provider_offers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delegated_provider_offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.user_subscriptions.delegated_provider_offers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The offer ID |
| <CopyableCode code="name" /> | `string` | The name of the offer. |
| <CopyableCode code="description" /> | `string` | Description of offer. |
| <CopyableCode code="displayName" /> | `string` | Display name of offer. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="delegatedProviderId, offerName" /> | Get the specified offer for the delegated provider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="delegatedProviderId" /> | Get the list of offers for the specified delegated provider. |

## `SELECT` examples

Get the list of offers for the specified delegated provider.


```sql
SELECT
id,
name,
description,
displayName
FROM azure_stack.user_subscriptions.delegated_provider_offers
WHERE delegatedProviderId = '{{ delegatedProviderId }}';
```