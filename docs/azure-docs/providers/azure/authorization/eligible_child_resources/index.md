---
title: eligible_child_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - eligible_child_resources
  - authorization
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

Creates, updates, deletes, gets or lists a <code>eligible_child_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>eligible_child_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.eligible_child_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource scope Id. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="type" /> | `string` | The resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="scope" /> | Get the child resources of a resource on which user has eligible access |

## `SELECT` examples

Get the child resources of a resource on which user has eligible access


```sql
SELECT
id,
name,
type
FROM azure.authorization.eligible_child_resources
WHERE scope = '{{ scope }}';
```