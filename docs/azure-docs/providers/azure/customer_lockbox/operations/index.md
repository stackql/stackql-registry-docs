---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - customer_lockbox
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.customer_lockbox.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Gets or sets action name |
| <CopyableCode code="display" /> | `object` | Contains the localized display information for this particular operation / action. |
| <CopyableCode code="isDataAction" /> | `string` | Gets or sets a value indicating whether it is a data plane action |
| <CopyableCode code="origin" /> | `string` | Gets or sets origin |
| <CopyableCode code="properties" /> | `string` | Gets or sets properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all the available REST API operations. |

## `SELECT` examples

Lists all the available REST API operations.


```sql
SELECT
name,
display,
isDataAction,
origin,
properties
FROM azure.customer_lockbox.operations
;
```