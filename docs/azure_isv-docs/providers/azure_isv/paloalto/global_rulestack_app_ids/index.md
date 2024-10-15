---
title: global_rulestack_app_ids
hide_title: false
hide_table_of_contents: false
keywords:
  - global_rulestack_app_ids
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

Creates, updates, deletes, gets or lists a <code>global_rulestack_app_ids</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_rulestack_app_ids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.global_rulestack_app_ids" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="globalRulestackName" /> | List of AppIds for GlobalRulestack ApiVersion |

## `SELECT` examples

List of AppIds for GlobalRulestack ApiVersion


```sql
SELECT
column_anon
FROM azure_isv.paloalto.global_rulestack_app_ids
WHERE globalRulestackName = '{{ globalRulestackName }}';
```