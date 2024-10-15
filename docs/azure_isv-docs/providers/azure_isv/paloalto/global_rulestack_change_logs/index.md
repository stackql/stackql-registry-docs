---
title: global_rulestack_change_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - global_rulestack_change_logs
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

Creates, updates, deletes, gets or lists a <code>global_rulestack_change_logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_rulestack_change_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.global_rulestack_change_logs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="changes" /> | `array` | list of changes |
| <CopyableCode code="lastCommitted" /> | `string` | lastCommitted timestamp |
| <CopyableCode code="lastModified" /> | `string` | lastModified timestamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="globalRulestackName" /> | Get changelog |

## `SELECT` examples

Get changelog


```sql
SELECT
changes,
lastCommitted,
lastModified
FROM azure_isv.paloalto.global_rulestack_change_logs
WHERE globalRulestackName = '{{ globalRulestackName }}';
```