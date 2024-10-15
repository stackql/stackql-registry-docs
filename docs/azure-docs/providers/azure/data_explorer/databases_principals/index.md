---
title: databases_principals
hide_title: false
hide_table_of_contents: false
keywords:
  - databases_principals
  - data_explorer
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

Creates, updates, deletes, gets or lists a <code>databases_principals</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases_principals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.databases_principals" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Database principal name. |
| <CopyableCode code="appId" /> | `string` | Application id - relevant only for application principal type. |
| <CopyableCode code="email" /> | `string` | Database principal email if exists. |
| <CopyableCode code="fqn" /> | `string` | Database principal fully qualified name. |
| <CopyableCode code="role" /> | `string` | Database principal role. |
| <CopyableCode code="tenantName" /> | `string` | The tenant name of the principal |
| <CopyableCode code="type" /> | `string` | Database principal type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Returns a list of database principals of the given Kusto cluster and database. |

## `SELECT` examples

Returns a list of database principals of the given Kusto cluster and database.


```sql
SELECT
name,
appId,
email,
fqn,
role,
tenantName,
type
FROM azure.data_explorer.databases_principals
WHERE clusterName = '{{ clusterName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```