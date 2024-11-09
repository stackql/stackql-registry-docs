---
title: cluster_config
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_config
  - schema_registry
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>cluster_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.cluster_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="maxRequestsPerSec" /> | `integer` | Maximum number of allowed requests per second |
| <CopyableCode code="maxSchemas" /> | `integer` | Maximum number of registered schemas allowed |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cluster_config" /> | `SELECT` | <CopyableCode code="" /> | Retrieves cluster config information. |

## `SELECT` examples

Retrieves cluster config information.


```sql
SELECT
maxRequestsPerSec,
maxSchemas
FROM confluent.schema_registry.cluster_config
;
```