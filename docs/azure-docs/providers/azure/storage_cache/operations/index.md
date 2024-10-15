---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - storage_cache
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation name: {provider}/{resource}/{operation} |
| <CopyableCode code="display" /> | `object` | The object that represents the operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | The flag that indicates whether the operation applies to data plane. |
| <CopyableCode code="origin" /> | `string` | Origin of the operation. |
| <CopyableCode code="properties" /> | `object` | Additional details about an operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available Resource Provider operations. |
| <CopyableCode code="check_aml_fs_subnets" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Check that subnets will be valid for AML file system create calls. |

## `SELECT` examples

Lists all of the available Resource Provider operations.


```sql
SELECT
name,
display,
isDataAction,
origin,
properties
FROM azure.storage_cache.operations
;
```