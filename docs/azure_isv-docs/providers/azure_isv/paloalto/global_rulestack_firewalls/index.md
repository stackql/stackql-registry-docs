---
title: global_rulestack_firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - global_rulestack_firewalls
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

Creates, updates, deletes, gets or lists a <code>global_rulestack_firewalls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_rulestack_firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.global_rulestack_firewalls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="globalRulestackName" /> | List of Firewalls associated with Rulestack |

## `SELECT` examples

List of Firewalls associated with Rulestack


```sql
SELECT
column_anon
FROM azure_isv.paloalto.global_rulestack_firewalls
WHERE globalRulestackName = '{{ globalRulestackName }}';
```