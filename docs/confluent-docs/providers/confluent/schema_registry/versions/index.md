---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - schema_registry
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

Creates, updates, deletes, gets or lists a <code>versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="subject" /> | `string` | Name of the subject |
| <CopyableCode code="version" /> | `integer` | Version number |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_versions" /> | `SELECT` | <CopyableCode code="id" /> | Get all the subject-version pairs associated with the input ID. |
| <CopyableCode code="list_versions" /> | `SELECT` | <CopyableCode code="subject" /> | Retrieves a list of versions registered under the specified subject. |

## `SELECT` examples

Get all the subject-version pairs associated with the input ID.


```sql
SELECT
subject,
version
FROM confluent.schema_registry.versions
WHERE id = '{{ id }}';
```