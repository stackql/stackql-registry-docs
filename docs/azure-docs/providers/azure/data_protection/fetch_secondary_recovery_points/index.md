---
title: fetch_secondary_recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - fetch_secondary_recovery_points
  - data_protection
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

Creates, updates, deletes, gets or lists a <code>fetch_secondary_recovery_points</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fetch_secondary_recovery_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.fetch_secondary_recovery_points" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Resource name associated with the resource. |
| <CopyableCode code="properties" /> | `object` | Azure backup recoveryPoint |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | Returns a list of Secondary Recovery Points for a DataSource in a vault, that can be used for Cross Region Restore. |

## `SELECT` examples

Returns a list of Secondary Recovery Points for a DataSource in a vault, that can be used for Cross Region Restore.


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_protection.fetch_secondary_recovery_points
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```