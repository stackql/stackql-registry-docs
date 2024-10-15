---
title: long_term_retention_managed_instance_backups_by_resource_group_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - long_term_retention_managed_instance_backups_by_resource_group_instances
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

Creates, updates, deletes, gets or lists a <code>long_term_retention_managed_instance_backups_by_resource_group_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>long_term_retention_managed_instance_backups_by_resource_group_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.long_term_retention_managed_instance_backups_by_resource_group_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a long term retention backup |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationName, managedInstanceName, resourceGroupName, subscriptionId" /> | Lists the long term retention backups for a given managed instance. |

## `SELECT` examples

Lists the long term retention backups for a given managed instance.


```sql
SELECT
properties
FROM azure.sql.long_term_retention_managed_instance_backups_by_resource_group_instances
WHERE locationName = '{{ locationName }}'
AND managedInstanceName = '{{ managedInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```