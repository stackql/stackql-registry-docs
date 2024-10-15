---
title: databases_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - databases_keys
  - redis_enterprise
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

Creates, updates, deletes, gets or lists a <code>databases_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis_enterprise.databases_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="primaryKey" /> | `string` | The current primary key that clients can use to authenticate |
| <CopyableCode code="secondaryKey" /> | `string` | The current secondary key that clients can use to authenticate |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Retrieves the access keys for the Redis Enterprise database. |

## `SELECT` examples

Retrieves the access keys for the Redis Enterprise database.


```sql
SELECT
primaryKey,
secondaryKey
FROM azure_isv.redis_enterprise.databases_keys
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```