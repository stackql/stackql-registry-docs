---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - image_builder
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.image_builder.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | This is of the format {provider}/{resource}/{operation} |
| <CopyableCode code="display" /> | `object` |  |
| <CopyableCode code="isDataAction" /> | `boolean` |  |
| <CopyableCode code="origin" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists available operations for the Microsoft.VirtualMachineImages provider |

## `SELECT` examples

Lists available operations for the Microsoft.VirtualMachineImages provider


```sql
SELECT
name,
display,
isDataAction,
origin,
properties
FROM azure.image_builder.operations
;
```