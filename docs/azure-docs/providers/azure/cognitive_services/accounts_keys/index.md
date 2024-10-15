---
title: accounts_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_keys
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>accounts_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.accounts_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key1" /> | `string` | Gets the value of key 1. |
| <CopyableCode code="key2" /> | `string` | Gets the value of key 2. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the account keys for the specified Cognitive Services account. |

## `SELECT` examples

Lists the account keys for the specified Cognitive Services account.


```sql
SELECT
key1,
key2
FROM azure.cognitive_services.accounts_keys
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```