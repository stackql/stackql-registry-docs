---
title: elastic_pool_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_pool_operations
  - sql
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

Creates, updates, deletes, gets or lists a <code>elastic_pool_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>elastic_pool_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.elastic_pool_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a elastic pool operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_elastic_pool" /> | `SELECT` | <CopyableCode code="elasticPoolName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of operations performed on the elastic pool. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="elasticPoolName, operationId, resourceGroupName, serverName, subscriptionId" /> | Cancels the asynchronous operation on the elastic pool. |

## `SELECT` examples

Gets a list of operations performed on the elastic pool.


```sql
SELECT
properties
FROM azure.sql.elastic_pool_operations
WHERE elasticPoolName = '{{ elasticPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```