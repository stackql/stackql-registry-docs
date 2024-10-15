---
title: databases_inaccessible_by_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - databases_inaccessible_by_servers
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

Creates, updates, deletes, gets or lists a <code>databases_inaccessible_by_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases_inaccessible_by_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.databases_inaccessible_by_servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="kind" /> | `string` | Kind of database. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="managedBy" /> | `string` | Resource that manages the database. |
| <CopyableCode code="properties" /> | `object` | The database's properties. |
| <CopyableCode code="sku" /> | `object` | An ARM Resource SKU. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of inaccessible databases in a logical server |

## `SELECT` examples

Gets a list of inaccessible databases in a logical server


```sql
SELECT
identity,
kind,
location,
managedBy,
properties,
sku,
tags
FROM azure.sql.databases_inaccessible_by_servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```