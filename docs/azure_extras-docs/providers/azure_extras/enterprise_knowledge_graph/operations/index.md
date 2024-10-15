---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - enterprise_knowledge_graph
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.enterprise_knowledge_graph.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Operation name: {provider}/{resource}/{operation}. |
| <CopyableCode code="display" /> | `object` | The operation supported by EnterpriseKnowledgeGraph Service Management. |
| <CopyableCode code="origin" /> | `string` | The origin of the operation. |
| <CopyableCode code="properties" /> | `object` | Additional properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all the available EnterpriseKnowledgeGraph services operations. |

## `SELECT` examples

Lists all the available EnterpriseKnowledgeGraph services operations.


```sql
SELECT
name,
display,
origin,
properties
FROM azure_extras.enterprise_knowledge_graph.operations
;
```