---
title: available_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - available_operations
  - powerbi_embedded
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

Creates, updates, deletes, gets or lists a <code>available_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>available_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_embedded.available_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation being performed on this particular object. This name should match the action name that appears in RBAC / the event service. |
| <CopyableCode code="display" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Indicates which operations can be performed by the Power BI Resource Provider. |

## `SELECT` examples

Indicates which operations can be performed by the Power BI Resource Provider.


```sql
SELECT
name,
display
FROM azure.powerbi_embedded.available_operations
;
```