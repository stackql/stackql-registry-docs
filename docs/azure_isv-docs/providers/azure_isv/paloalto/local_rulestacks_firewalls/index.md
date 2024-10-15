---
title: local_rulestacks_firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - local_rulestacks_firewalls
  - paloalto
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

Creates, updates, deletes, gets or lists a <code>local_rulestacks_firewalls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_rulestacks_firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.local_rulestacks_firewalls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | List of Firewalls associated with Rulestack |

## `SELECT` examples

List of Firewalls associated with Rulestack


```sql
SELECT
column_anon
FROM azure_isv.paloalto.local_rulestacks_firewalls
WHERE localRulestackName = '{{ localRulestackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```