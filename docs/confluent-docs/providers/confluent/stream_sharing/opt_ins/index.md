---
title: opt_ins
hide_title: false
hide_table_of_contents: false
keywords:
  - opt_ins
  - stream_sharing
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>opt_ins</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>opt_ins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.stream_sharing.opt_ins" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="stream_share_enabled" /> | `boolean` | Enable stream sharing for the organization |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cdx_v1opt_in" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Returns the organization's stream sharing opt-in settings. |
| <CopyableCode code="update_cdx_v1opt_in" /> | `UPDATE` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Updates the organization's stream sharing opt-in settings. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Returns the organization's stream sharing opt-in settings.


```sql
SELECT
api_version,
kind,
stream_share_enabled
FROM confluent.stream_sharing.opt_ins
;
```
## `UPDATE` example

Updates a <code>opt_ins</code> resource.

```sql
/*+ update */
UPDATE confluent.stream_sharing.opt_ins
SET 
stream_share_enabled = true|false
WHERE 
;
```
