---
title: global_rulestack_predefined_url_categories
hide_title: false
hide_table_of_contents: false
keywords:
  - global_rulestack_predefined_url_categories
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

Creates, updates, deletes, gets or lists a <code>global_rulestack_predefined_url_categories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_rulestack_predefined_url_categories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.global_rulestack_predefined_url_categories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="action" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="globalRulestackName" /> | List predefined URL categories for rulestack |

## `SELECT` examples

List predefined URL categories for rulestack


```sql
SELECT
name,
action
FROM azure_isv.paloalto.global_rulestack_predefined_url_categories
WHERE globalRulestackName = '{{ globalRulestackName }}';
```