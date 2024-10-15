---
title: managed_databases_inaccessible_by_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_databases_inaccessible_by_instances
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

Creates, updates, deletes, gets or lists a <code>managed_databases_inaccessible_by_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_databases_inaccessible_by_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_databases_inaccessible_by_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The managed database's properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a list of inaccessible managed databases in a managed instance |

## `SELECT` examples

Gets a list of inaccessible managed databases in a managed instance


```sql
SELECT
location,
properties,
tags
FROM azure.sql.managed_databases_inaccessible_by_instances
WHERE managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```