---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - sql_vm
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql_vm.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation being performed on this particular object. |
| <CopyableCode code="display" /> | `object` | Display metadata associated with the operation. |
| <CopyableCode code="origin" /> | `string` | The intended executor of the operation. |
| <CopyableCode code="properties" /> | `object` | Additional descriptions for the operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available SQL Virtual Machine Rest API operations. |

## `SELECT` examples

Lists all of the available SQL Virtual Machine Rest API operations.


```sql
SELECT
name,
display,
origin,
properties
FROM azure.sql_vm.operations
;
```