---
title: developers_balance
hide_title: false
hide_table_of_contents: false
keywords:
  - developers_balance
  - apigee
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

Creates, updates, deletes, gets or lists a <code>developers_balance</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>developers_balance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.developers_balance" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="wallets" /> | `array` | Output only. List of all wallets. Each individual wallet stores the account balance for a particular currency. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_developers_get_balance" /> | `SELECT` | <CopyableCode code="developersId, organizationsId" /> | Gets the account balance for the developer. |

## `SELECT` examples

Gets the account balance for the developer.

```sql
SELECT
wallets
FROM google.apigee.developers_balance
WHERE developersId = '{{ developersId }}'
AND organizationsId = '{{ organizationsId }}'; 
```
