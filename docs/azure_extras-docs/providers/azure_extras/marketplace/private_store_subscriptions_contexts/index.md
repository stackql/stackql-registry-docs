---
title: private_store_subscriptions_contexts
hide_title: false
hide_table_of_contents: false
keywords:
  - private_store_subscriptions_contexts
  - marketplace
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

Creates, updates, deletes, gets or lists a <code>private_store_subscriptions_contexts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_store_subscriptions_contexts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.private_store_subscriptions_contexts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="subscriptionsIds" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateStoreId" /> | List all the subscriptions in the private store context |

## `SELECT` examples

List all the subscriptions in the private store context


```sql
SELECT
subscriptionsIds
FROM azure_extras.marketplace.private_store_subscriptions_contexts
WHERE privateStoreId = '{{ privateStoreId }}';
```